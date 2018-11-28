#include<cstdio>
#include<vector>
#include<map>
#include<algorithm>
#include<queue>

using namespace std;

typedef pair<int,int> PII;

map<vector<PII>, int> dmap;

int r,c;

bool e[20][20];

vector<PII> sv;
vector<PII> ev;

queue<vector<PII> > q;

int dy[] = {0,0,1,-1};
int dx[] = {1,-1,0,0};

bool vis[20];

bool connected(vector<PII>& v){
	for(int i=0;i<v.size();i++) vis[i] = 0;
	vis[0] = 1;
	int cv = 1;
	while(cv < v.size()){
		bool ok = 0;
		for(int i=0;i<v.size();i++){
			if(!vis[i]) continue;
			for(int j=0;j<v.size();j++){
				if(!vis[j]){
					if(abs(v[i].first - v[j].first) + abs(v[i].second - v[j].second) == 1){
						vis[j] = 1;
						++cv;
						ok = 1;
					}
				}
			}
		}
		if(!ok) return 0;
	}
	return 1;
}

void checkmove2(vector<PII>& v,int dst){
	for(int i=0;i<v.size();i++){
		int y = v[i].first;
		int x = v[i].second;
		for(int j=0;j<4;j++){
			int yf = y + dy[j];
			int xf = x + dx[j];
			int yb = y - dy[j];
			int xb = x - dx[j];
			if(!e[yf][xf] || !e[yb][xb]) continue;
			v[i].first += dy[j];
			v[i].second += dx[j];
			if(connected(v)){
				vector<PII> v2 = v;
				sort(v2.begin(),v2.end());
				if(dmap.find(v2) == dmap.end()){
					dmap[v2] = dst + 2;
					q.push(v2);
				}
			}
			v[i].first -= dy[j];
			v[i].second -= dx[j];
		}
	}
}

void checkmoves(vector<PII>& v,int dst){
	for(int i=0;i<v.size();i++) e[v[i].first][v[i].second] = 0;
	for(int i=0;i<v.size();i++){
		int y = v[i].first;
		int x = v[i].second;
		for(int j=0;j<4;j++){
			int yf = y + dy[j];
			int xf = x + dx[j];
			int yb = y - dy[j];
			int xb = x - dx[j];
			if(!e[yf][xf] || !e[yb][xb]) continue;
			e[y][x] = 1;
			e[yf][xf] = 0;
			v[i].first += dy[j];
			v[i].second += dx[j];
			if(!connected(v)) checkmove2(v,dst);
			else{
				vector<PII> v2 = v;
				sort(v2.begin(),v2.end());
				if(dmap.find(v2) == dmap.end()){
					dmap[v2] = dst + 1;
					q.push(v2);
				}
			}
			e[y][x] = 0;
			e[yf][xf] = 1;
			v[i].first -= dy[j];
			v[i].second -= dx[j];
		}
	}
	for(int i=0;i<v.size();i++) e[v[i].first][v[i].second] = 1;
}

int bfs(){
	while(!q.empty()) q.pop();
	q.push(sv);
	dmap[sv] = 0;
	while(!q.empty()){
		vector<PII> c = q.front(); q.pop();
		if(c == ev) return dmap[c];
		checkmoves(c,dmap[c]);
	}
	return -1;
}

void alg(){
	sv.clear();
	ev.clear();
	dmap.clear();
	scanf("%d%d",&r,&c);
	for(int i=0;i<=r+1;i++) for(int j=0;j<=c+1;j++) e[i][j] = 0;
	for(int i=1;i<=r;i++){
		for(int j=1;j<=c;j++){
			char s[2];
			scanf("%1s",s);
			if(s[0] == '.'){
				e[i][j] = 1;
			}else if(s[0] == 'o'){
				e[i][j] = 1;
				sv.push_back(make_pair(i,j));
			}else if(s[0] == 'x'){
				e[i][j] = 1;
				ev.push_back(make_pair(i,j));
			}else if(s[0] == 'w'){
				e[i][j] = 1;
				sv.push_back(make_pair(i,j));
				ev.push_back(make_pair(i,j));
			}
		}
	}
	sort(sv.begin(),sv.end());
	sort(ev.begin(),ev.end());
	printf("%d\n",bfs());
}

int main(){
	int d;
	scanf("%d",&d);
	for(int i=1;i<=d;i++){
		printf("Case #%d: ",i);
		alg();
	}
}

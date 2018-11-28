#include <iostream>
#include <vector>
#include <queue>
using namespace std;

int h,w;
int z='a';
vector <vector <int> > a;
vector <vector <bool> > b;
vector <vector < vector <pair <int,int> > > > r;
vector <vector <char> > g;

pair <int,int> fnd(int i,int j){
	int m=1000000;
	pair <int,int> r;
	r.first=-1;
	r.second=-1;
	bool b=false;
	if (i+1<h && a[i+1][j]<a[i][j]) b=true;
	if (j+1<w && a[i][j+1]<a[i][j]) b=true;
	if (j-1>=0 && a[i][j-1]<a[i][j]) b=true;
	if (i-1>=0 && a[i-1][j]<a[i][j]) b=true;
	if (!b) return r;
	if (i+1<h && a[i+1][j]<=m) m=min(m,a[i+1][j]),r.first=i+1,r.second=j;
	if (j+1<w && a[i][j+1]<=m) m=min(m,a[i][j+1]),r.first=i,r.second=j+1;
	if (j-1>=0 && a[i][j-1]<=m) m=min(m,a[i][j-1]),r.first=i,r.second=j-1;
	if (i-1>=0 && a[i-1][j]<=m) m=min(m,a[i-1][j]),r.first=i-1,r.second=j;
	return r;
}

void bfs(int i,int j){
	queue <pair <int,int> > q;
	pair <int,int> t;
	t=make_pair(i,j);
	q.push(t);
	while (!q.empty()){
		b[q.front().first][q.front().second]=true;
		g[q.front().first][q.front().second]=z;
		for (int k=0;k<r[q.front().first][q.front().second].size();k++){
			t=make_pair(r[q.front().first][q.front().second][k].first,r[q.front().first][q.front().second][k].second);
			if (!b[t.first][t.second]) q.push(t);
		}
		q.pop();
	}
}


void getdata(){
	scanf("%d %d\n",&h,&w);
	a.erase(a.begin(),a.end());
	r.erase(r.begin(),r.end());
	b.erase(b.begin(),b.end());
	g.erase(g.begin(),g.end());
	a.resize(h);
	r.resize(h);
	b.resize(h);
	g.resize(h);
	for (int i=0;i<h;i++){
		b[i].resize(w);
		a[i].resize(w);
		r[i].resize(w);
		g[i].resize(w);
		for (int j=0;j<w;j++) scanf("%d ",&a[i][j]);
	}
}


void solve(){
	z='a';
	getdata();
	pair <int,int> p;
	for (int i=0;i<h;i++) {
		for (int j=0;j<w;j++){
			p=fnd(i,j);
			if (p.first!=-1 && p.second!=-1){
				r[i][j].push_back(p);
				r[p.first][p.second].push_back(make_pair(i,j));
			}
		}
	}

	for (int i=0;i<h;i++){
		for (int j=0;j<w;j++){
			if (!b[i][j]){
				bfs(i,j);
				z++;
			}
		}
	}

	for (int i=0;i<h;i++){
		for (int j=0;j<w;j++){
			printf("%c ",g[i][j]);
		}
		printf("\n");
	}

}


int main(){
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	int t;
	scanf("%d\n",&t);
	for (int i=1;i<=t;i++){
		printf("Case #%d:\n",i);
		solve();
	}
	return 0;
}
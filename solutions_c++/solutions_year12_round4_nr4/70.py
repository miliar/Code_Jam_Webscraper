#include<cstdio>
#include<algorithm>
#include<vector>
#include<queue>
#include<iostream>
#include<set>
#include<map>

#define N 10005
using namespace std;

int n,m;
char data[15][15];
int cn,table[15],table2[15],visit[15][15];
set<int> st,stt;
map<set<int>, int> mp;
struct ele{
	set<int> s;
	bool operator < (ele a) const{
		return s.size() > a.s.size();
	}
};
priority_queue<ele> q;
ele u;
int dir[4][2] = {-1,0,0,1,0,-1, 1, 0};
void dfs(int y,int x){
	int i,yy,xx;
	st.insert(y*m+x);
	visit[y][x]=1;
	for(i=0;i<3;i++){
		yy = y+dir[i][0];
		xx = x+dir[i][1];
		if (data[yy][xx]=='#') continue;
		if (visit[yy][xx]) continue;
		dfs(yy,xx);
	}
}
int main(){
	int i,j,k;
	int y,x;
	int tc;
	int ans;
	int er;
	FILE *out = fopen("output.txt", "w");
	freopen("input.txt", "r", stdin);
	scanf("%d", &tc);
	for(int tcc = 1; tcc<=tc; tcc++){
		memset(table2,0,sizeof(table2));
		cn = 0;
		scanf("%d %d", &n, &m);
		for(i=0;i<n;i++){
			scanf("%s", &data[i]);
			for(j=0;j<m;j++){
				if (data[i][j]>= '0' && data[i][j]<='9'){
					cn = max(cn, data[i][j]-'0'+1);
				}
			}
		}
		printf("case %d %d\n", tcc, cn);
		set<int>::iterator it;
		for(i=0;i<n;i++){
			for(j=0;j<m;j++){
				if (!(data[i][j]>='0' && data[i][j]<='9')) continue;
				printf("%d\n", data[i][j]-'0');
				memset(visit,0,sizeof(visit));
				mp.clear();
				st.clear();
				dfs(i,j);
				table[data[i][j]-'0']=st.size();
				mp[st] = 1;
				while(!q.empty())
					q.pop();
				u.s = st;
				q.push(u);
				while(!q.empty()){
					st = q.top().s;
					q.pop();
					//printf("--%d ", st.size());
					if (st.size()==1){
						it = st.begin();
						y = (*it)/m;
						x = (*it)%m;
						if (y==i && x==j){
							table2[data[i][j]-'0']=1;
							break;
						}
					}
					for(k=1;k<=3;k++){
						er = 0;
						stt.clear();
						for(it =st.begin();it!=st.end();it++){
							y = (*it)/m+dir[k][0];
							x = (*it)%m+dir[k][1];
							if (data[y][x]=='#'){
								stt.insert(*it);
							} else {
								if (y > i || visit[y][x]!=1) {
									er = 1;
									break;
								}
								stt.insert(y*m+x);
							}
						}
						if (er) continue;
						if (mp.find(stt)!=mp.end()) continue;
						mp[stt] = 1;
						u.s = stt;
						q.push(u);
					}
				}
				printf("%d\n", data[i][j]-'0');
			}
		}
		fprintf(out, "Case #%d:\n", tcc);
		for(i=0;i<cn;i++){
			fprintf(out, "%d: %d %s\n", i, table[i], (table2[i]==1)? "Lucky":"Unlucky");
		}
	}
	return 0;
}
#include <stdio.h>
#include <algorithm>
#include <vector>
#include <map>

using namespace std;

int n;
class DAT{
public:
	int U, V ,dif;
	const bool operator < (const DAT &t)const{
		return dif < t.dif;
	}
} dat[2005];

bool check[2005];
int next[2005], ntype[2005];
vector<int> cycle[2005], edge[2005];

int ccnt;
int color[2005];

		/*
		color_i [  cycle[i][j]  ] = {
			j  if j < sol
			sol-2 + {(j-sol) % 2}   otherwise
		}
		*/


int sol;
int change[2005];
void dfs(int x){
	if(check[x]) return;
	check[x] = true;
	int i, j, n, tco;
	n = cycle[x].size();
	for(i=0;i<sol;i++) change[i] = i;
	for(i=0;i<n;i++){
		if(i < sol) tco = i;
		else tco = sol-2 + (i-sol)%2;
		if(color[ cycle[x][i] ] != -1){
			for(j=0;j<sol;j++) if(change[j] == color[ cycle[x][i] ]) break;
			int temp;
			temp = change[tco];
			change[tco] = change[j];
			change[j] = temp;
		}
	}
	for(i=0;i<n;i++){
		
		if(i < sol) tco = i;
		else tco = sol-2 + (i-sol)%2;color[ cycle[x][i] ] = change[tco];
	}

	for(i=0;i<edge[x].size();i++) dfs( edge[x][i] );
}
int main(){
	freopen("C-large.in","r",stdin);
	freopen("result.txt","w",stdout);
	int T, m;
	scanf("%d",&T);
	while(T>0){T--;
		scanf("%d %d",&n, &m);
		int i;
		for(i=0;i<n;i++) cycle[i] = vector<int>();
		for(i=0;i<n;i++) edge[i] = vector<int>();
		for(i=0;i<n;i++) color[i] = -1;

		for(i=0;i<m;i++){
			scanf("%d",&dat[i].U); dat[i].U--;
		}
		for(i=0;i<m;i++){
			scanf("%d",&dat[i].V); dat[i].V--;
		}
		
		for(i=0;i<m;i++){
			dat[i].dif = dat[i].U - dat[i].V;

			if(dat[i].dif < 0) dat[i].dif += n;
			dat[i].dif = min(dat[i].dif, n-dat[i].dif);
		}
		sort(dat, dat+m);
		for(i=0;i<n;i++){
			next[i] = (i+1)%n;
			ntype[i] = -1;
		}
		int start, now, end;
		int res, tmp;

		int remain = 0;
		ccnt = 0;
		for(i=0;i<m;i++){
			int dif;
			dif = dat[i].V - dat[i].U;
			if(dif < 0) dif = dif + n;
			if(dif < n - dif){
				start = dat[i].U;
				end = dat[i].V;
				dif = n - dif;
			}
			else{
				start = dat[i].V;
				end = dat[i].U;
			}

			
			now = start;
			while(now != end){
				cycle[ccnt].push_back(now);
				if(ntype[now] != -1){
					edge[ntype[now]].push_back(ccnt);
					edge[ccnt].push_back(ntype[now]);
				}
				now = next[now];
			}
			cycle[ccnt].push_back(end);
			next[start] = end;
			ntype[start] = ccnt;
			remain = start;
			ccnt ++;
		}

		
		memset(check, 0,sizeof(check));
		now = remain;
		for(i=0; ;i++){
			if(check[now]) break;
			check[now] = true;
			cycle[ccnt].push_back(now);
			if(ntype[now] != -1){
				edge[ntype[now]].push_back(ccnt);
				edge[ccnt].push_back(ntype[now]);
			}
			now = next[now];
		}
		
		ccnt ++;

		for(i=0;i<ccnt;i++){
			if(i == 0 || sol > cycle[i].size()) sol = cycle[i].size();
		}

		memset(check, 0,sizeof(check));
		dfs(0);
		static int cs = 1;
		printf("Case #%d: %d\n", cs++, sol);
		for(i=0;i<n;i++){
			printf("%d " , color[i]+1);
		}
		printf("\n");

	}

	return 0;
}
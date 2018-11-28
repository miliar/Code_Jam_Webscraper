#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <sstream>
#include <string>
#include <set>
#include <map>
#include <algorithm>

using namespace std;

#define MAXN 4000

int m,n;
bool adj[MAXN][2*MAXN];

int like[MAXN][2*MAXN];
int deg[MAXN];

int umalt[MAXN][MAXN];
int udeg[MAXN];

int malt[MAXN][MAXN];
int mdeg[MAXN];

bool ismalt[MAXN];
int num[MAXN];

int main(){
	
	int tst,lp;
	int i,j,k,t;
	int a,b;
	int ret;
	
	scanf("%d",&tst);
	
	for(lp=1;lp<=tst;lp++){
		scanf("%d %d",&n,&m);
		for(i=0;i<n;i++){
			mdeg[i] = 0;
			udeg[i] = 0;
			ismalt[i] = false;
		}
		
		for(i=0;i<m;i++){
			/*
			for(j=0;j<2*n;j++){
				adj[i][j] = false;	
			}
			*/
			deg[i] = 0;
		}
		
		for(i=0;i<m;i++){
			scanf("%d",&t);
			k = -1;
			for(j=0;j<t;j++){
				scanf("%d %d",&a,&b);
				a--;
				if(b) k = a;
				else{
					like[i][deg[i]++] = a;
					umalt[a][udeg[a]++] = i;
					//adj[i][a] = true;
				}
			}
			if(k >= 0){
				like[i][deg[i]] = k;
				malt[k][mdeg[k]++] = i;
			}
			else{
				like[i][deg[i]] = -1;
			}
		}
		
		for(i=0;i<m;i++){
			num[i] = deg[i];
		}
		
		for(ret=0;ret<=n;ret++){
			bool ok = true;
			for(i=0;i<m;i++){
				if(num[i] <= 0){
					k = like[i][deg[i]];
					ok = false;
					break;
				}
			}
			if(ok) break;
			
			if(k < 0){
				ret = 2*n;
				break;
			}
			
			ismalt[k] = true;
			
			for(i=0;i<udeg[k];i++){
				num[umalt[k][i]]--;
			}
			
			for(i=0;i<mdeg[k];i++){
				num[malt[k][i]] += 2*n;
			}
			
		}
		
		printf("Case #%d:",lp);
		
		if(ret > n){
			printf(" IMPOSSIBLE\n");
		}
		else{
			for(i=0;i<n;i++){
				if(ismalt[i]) printf(" 1");
				else printf(" 0");
			}
			printf("\n");
		}
		
	}
	
	return 0;
	
}

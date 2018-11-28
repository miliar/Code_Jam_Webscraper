#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <iostream>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <algorithm>

using namespace std;

#define MAXN 11
#define INF -1000000000

int m,n;
char tab[MAXN][MAXN];

int resp[MAXN][1<<MAXN];
bool valid[1<<MAXN];
int q[1<<MAXN];
int msk[MAXN];

int main(){
	
	int t,lp;
	int i,j,k,h;
	bool ok;
	int ret;
	
	scanf("%d",&t);
	
	for(lp=1;lp<=t;lp++){
		scanf("%d %d",&m,&n);
		ret = INF;
		for(i=0;i<m;i++){
			scanf("%s",tab[i]);
			msk[m-i-1] = 0;
			for(j=0;j<n;j++){
				if(tab[i][j] == 'x') msk[m-i-1] |= (1<<j);
			}
		}
		
		for(i=0;i<m;i++){
			for(j=0;j<(1<<n);j++){
				resp[i][j] = INF;
			}
		}
		
		for(j=0;j<(1<<n);j++){
			valid[j] = true;
			q[j] = 0;
			for(i=0;i<n;i++){
				if(j & (1<<i)) q[j]++;
			}
			for(i=0;i<n-1;i++){
				if((j & (1<<i)) && (j & (1<<(i+1)))){
					valid[j] = false;
					break;
				}
			}
			if(!valid[j]) continue;
			//printf("%d\n",j);
			if((j & msk[0]) == 0){
				//printf("%d\n",j);
				resp[0][j] = q[j];
			}
		}
		
		for(i=0;i<m-1;i++){
			for(j=0;j<(1<<n);j++){
				if(resp[i][j] <= INF) continue;
				for(k=0;k<(1<<n);k++){
					if(k & msk[i+1]) continue;
					if(!valid[k]) continue;
					
					ok = true;
					for(h=0;h<n;h++){
						if((j & (1<<h)) == 0) continue;
						if(h > 0){
							if(k & (1<<(h-1))){
								ok = false;
								break;
							}
						}
						if(h < n-1){
							if(k & (1<<(h+1))){
								ok = false;
								break;
							}
						}
					}
					
					if(ok){
						resp[i+1][k] = max(resp[i+1][k],resp[i][j]+q[k]);
					}
					
				}
			}
		}
		
		for(i=0;i<m;i++){
			for(j=0;j<(1<<n);j++){
				ret = max(ret,resp[i][j]);
			}
		}
		
		printf("Case #%d: %d\n",lp,ret); 
		
	}
	
	return 0;
	
}
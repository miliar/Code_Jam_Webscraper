//code jam Problem B. Magicka

#include <stdio.h>
#include <string.h>
#include <algorithm>
using namespace std;

const int N = 250;
char Pairv[N][N];
bool Pairf[N][N];
bool opposed[N][N];
int main(){
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	int T,C,D,n,len;
	char op[150];
	scanf("%d",&T);
	for(int cas = 1; cas <= T; cas ++){
		memset(Pairf,false,sizeof(Pairf));
		memset(opposed,false,sizeof(opposed));
		scanf("%d",&C);
		for(int i = 0; i < C; i ++){
			scanf("%s",op);
			Pairv[op[0]][op[1]]=op[2];
			Pairv[op[1]][op[0]]=op[2];
			Pairf[op[0]][op[1]]=true;
			Pairf[op[1]][op[0]]=true;
		}
		scanf("%d",&D);
		for(int i = 0; i < D; i ++){
			scanf("%s",op);
			opposed[op[0]][op[1]]=true;
			opposed[op[1]][op[0]]=true;
		}
		scanf("%d",&n);
		scanf("%s",op);
		bool res[101];
		memset(res,true,sizeof(res));
		//res[0] = true;
		bool now;
		for(int i = 1; i < n; i ++){
			now = true;
			for(int j = i - 1; j >=0; j--){
				
					if(now && res[j]){
							now = false;
							if(Pairf[op[i]][op[j]]){
							op[i]=Pairv[op[i]][op[j]];
							res[j] = false;
							res[i] = true;
							break;
						}
					}
				
				if(res[j]){
					now = false;
					if(opposed[op[i]][op[j]]){
						for(int k = 0;k <=i ; k ++){
							res[k]=false;
						}
						break;
					}
				}
				
			}
		}
		printf("Case #%d: [",cas);
		bool ab=false;
		for(int i = 0; i < n; i ++){
			if(res[i]){
				if(!ab){
					printf("%c",op[i]);
					ab = true;
				}else{
					printf(", %c",op[i]);
				}
			}
		}
		printf("]\n");
	}
	return 0;
}

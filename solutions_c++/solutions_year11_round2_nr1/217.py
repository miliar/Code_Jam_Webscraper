#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;

int T,N;
int G[105][105],W[105],TOT[105];
long double WP[105],OWP[105],OOWP[105];
char c;

int main(){
	scanf("%d",&T);
	for(int testcase = 1;testcase <= T;++testcase){
		scanf("%d",&N);
		memset(G,-1,sizeof(G));
		memset(W,0,sizeof(W));
		memset(TOT,0,sizeof(TOT));
		memset(WP,0,sizeof(WP));
		memset(OWP,0,sizeof(OWP));
		memset(OOWP,0,sizeof(OOWP));
		for(int i=1;i<=N;++i){
			for(int j=1;j<=N;++j){
				scanf(" %c",&c);
				if(c != '.'){
					++TOT[i];
					if(c == '1'){
						G[i][j] = 1;
						++W[i];
					}
					else G[i][j] = 0;
				}
			}
			WP[i] = (long double)(W[i])/(long double)(TOT[i]);
		//	printf("WP[%d] = %Lf\n",i,WP[i]);
		}
		for(int a=1;a<=N;++a){
	//		printf("A = %d!!!!!!!!!!!\n",a);
			for(int i=1;i<=N;++i)
				if(i != a){
					if(G[i][a] == 0){
						//if(a == 4) printf("AAA%d: adding %Lf\n",i,(long double)(W[i])/(long double)(TOT[i]-1));
						OWP[a] += (long double)(W[i])/(long double)(TOT[i]-1);
					}
					else if(G[i][a] == 1){
				//		if(a == 4) printf("AAA%d: adding %Lf\n",i,(long double)(W[i]-1)/(long double)(TOT[i]-1));
						OWP[a] += (long double)(W[i]-1)/(long double)(TOT[i]-1);
					}
				}
			OWP[a] /= (long double)(TOT[a]);
		}
		for(int a=1;a<=N;++a){
			for(int i=1;i<=N;++i)
				if(G[a][i] != -1) OOWP[a] += OWP[i];
			OOWP[a] /= (long double)(TOT[a]);
		//	printf("OOWP[%d] = %Lf\n",a,OOWP[a]);
		}
		printf("Case #%d:\n",testcase);
		for(int i=1;i<=N;++i) printf("%Lf\n",0.25*WP[i] + 0.50*OWP[i] + 0.25*OOWP[i]);
	}
}

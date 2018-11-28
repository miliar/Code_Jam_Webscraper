#include <stdio.h>
#include <stdlib.h>

#include <string>
#include <vector>

using namespace std;

#define ll long long

int abs(int n){
	return n<0?-n:n;
}
int sgn(int n){
	return n<0?-1:(n>0?1:0);
}
int main(){
	int T;
	scanf("%d\n",&T);
	for(int Case=0;Case<T;Case++){
		int N;
		scanf("%d\n",&N);
		int plays[N][N];
		pair<ll,ll>wp[N];
		double owp[N],oowp[N];
		
		for(int a=0;a<N;a++,scanf("\n")){
			wp[a]=pair<ll,ll>(0,0);
			for(int b=0;b<N;b++){
				char ch;
				scanf("%c",&ch);
				plays[a][b]=(ch=='.'?-1:ch-'0');
				if(plays[a][b]>=0){
					wp[a].first+=plays[a][b];
					wp[a].second++;
				}
			}
		}
		
		for(int a=0;a<N;a++){
			owp[a]=0;
			ll denom=0;
			for(int b=0;b<N;b++){
				if(plays[b][a]<0)continue;
				owp[a]+=(wp[b].first-plays[b][a])/(wp[b].second-1.0);
				denom++;
			}
			owp[a]/=denom;
		}
		
		for(int a=0;a<N;a++){
			oowp[a]=0;
			ll denom=0;
			for(int b=0;b<N;b++){
				if(plays[b][a]<0)continue;
				oowp[a]+=owp[b];
				denom++;
			}
			oowp[a]/=denom;
		}
		
		printf("Case #%d:\n",Case+1);
		
		for(int t=0;t<N;t++)
			printf("%.10f\n",0.25*wp[t].first/wp[t].second+0.5*owp[t]+0.25*oowp[t]);
	}
	return 0;
}
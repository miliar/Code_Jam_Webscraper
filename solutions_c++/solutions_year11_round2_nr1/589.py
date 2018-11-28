#include<cstdio>
#include<cstring>
#include<iostream>
#include<string>
#include<algorithm>
typedef long long ll;
#define see(x) //(cerr<<"Line:["<<__LINE__<<"]:"<<#x<<"="<<x<<"\n")
using namespace std;
char G[120][120];
double WP[120],OWP[120],OOWP[120];
int main(){
	int T,cas=0;
	scanf("%d",&T);
	while(T--){
		cas++;
		int n;
		scanf("%d",&n);
		for(int r=0;r<n;r++)
			for(int c=0;c<n;c++){
				scanf(" %c",&G[r][c]);
			}
		printf("Case #%d:\n",cas);
		for(int i=0;i<n;i++){
			double all=0,ret=0;
			for(int j=0;j<n;j++){
				if(G[i][j]=='1'){
					ret++;
				}
				if(G[i][j]!='.')all++;
			}
			WP[i]=ret/all;
			OWP[i]=0;
			for(int j=0;j<n;j++)if(G[i][j]!='.'){
				all=ret=0;
				for(int k=0;k<n;k++)if(k!=i){
					if(G[j][k]!='.'){
						all++;
						if(G[j][k]=='1')
							ret++;
					}
				}
				OWP[i]+=ret/all;
			}
			all=0;
			for(int j=0;j<n;j++)
				if(G[i][j]!='.')
					all++;
			OWP[i]/=all;
		}
		for(int i=0;i<n;i++){
			OOWP[i]=0;
			int cnt=0;
			for(int j=0;j<n;j++){
				if(G[i][j]!='.'){
					OOWP[i]+=OWP[j];
					cnt++;
				}
			}
			OOWP[i]/=cnt;
			see(WP[i]);
			see(OWP[i]);
			see(OOWP[i]);
			printf("%.11lf\n",0.25*WP[i]+0.5*OWP[i]+0.25*OOWP[i]);
		}
		
	}
}

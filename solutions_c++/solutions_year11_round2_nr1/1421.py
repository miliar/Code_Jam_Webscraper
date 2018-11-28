#include<iostream>
#include<cstdio>
#include<string>
#include<vector>
#include<map>
#include<list>
using namespace std;
#define EPS 0.000001
int main(void){
	int T, N;
	char games[100][100];
	cin >> T;
	for(int tc=1;tc<=T;tc++){	
		scanf("%d",&N);
		for(int i=0;i<N;i++)
			for(int j=0;j<N;j++)
				cin >> games[i][j];
			
		double res;
		double WP[N][3];
		for(int i=0;i<N;i++){
			double cwp = 0.0, den = 0.0;
			for(int j=0;j<N;j++){
				if(games[i][j]!='.'){
					den += 1.0;
					if(games[i][j]=='1') cwp += 1.0;				
				}
			}
			WP[i][2] = cwp/den;
			WP[i][1] = den;
			WP[i][0] = cwp;
		}
		double OPWP[N], OOWP[N];
		for(int i=0;i<N;i++){
			double curowp = 0.0, den = 0.0;
			for(int j=0;j<N;j++){
				if(games[i][j]!='.'){
					den += 1.0;
					if(games[i][j] == '1')  curowp += (WP[j][0]/(WP[j][1]-1));
					else curowp += (WP[j][0]-1)/(WP[j][1]-1);				
				}
			}
			OPWP[i] = curowp/den;		
		}
		for(int i=0;i<N;i++){
			double oowp = 0.0, den = 0.0;
			for(int j=0;j<N;j++)
				if(games[i][j]!='.'){
					oowp += OPWP[j];
					den += 1.0;					
				}
			OOWP[i] = oowp/den;
		}
		printf("Case #%d:\n",tc);
		for(int i=0;i<N;i++){
			printf("%.12lf\n",0.25*WP[i][2]+0.5*OPWP[i]+0.25*OOWP[i]);
		}
	}
}

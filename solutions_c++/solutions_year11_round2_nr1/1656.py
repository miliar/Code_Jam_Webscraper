/*	Author       :	Muntasir Muzahid Chowdhury
	Problem Name :	
	Algorithm    :	
	Complexity   :	*/

//HEADERFILE
#include<iostream>
#include<stack>
#include<queue>
#include<list>
#include<vector>
#include<set>
#include<map>
#include<cstdio>
#include<cstdlib>
#include<cmath>
#include<cctype>
#include<cstring>
#include<ctime>
#include<cassert>
#include<string>
#include<algorithm>

using namespace std;

const double EPS = 1e-11;

int N;

struct s{ double wins,games; }WP[110];

int main(){
		//freopen("A-large.in","r",stdin);
		//freopen("A-large.out","w",stdout);
	int cases,caseno=0,i,j,result;
	int ar[110][110];
	double OWP[110],OOWP[110];
	char temp;
	scanf("%d",&cases);
	while(cases--){
		scanf("%d",&N);
		for(i=0;i<N;i++){
			getchar();WP[i].wins=WP[i].games=0;
			for(j=0;j<N;j++){
				scanf("%c",&temp);
				if(temp=='.') ar[i][j]=-1;
				else ar[i][j]=temp-48 , WP[i].wins+=ar[i][j], ++WP[i].games;
			}
		}
		double cnt;
		for(i=0;i<N;i++){
			OWP[i]=0;
			for(j=0,cnt=0;j<N;j++) {
				if(i!=j && ar[i][j]!=-1){
					++cnt;
					OWP[i]+=(WP[j].wins-ar[j][i])/(WP[j].games-1);
				}
			}
			OWP[i]/=cnt;
		}
		for(i=0;i<N;i++){
			OOWP[i]=0;
			for(j=0,cnt=0;j<N;j++){
				if(i!=j && ar[i][j]!=-1) OOWP[i]+=OWP[j], ++cnt;
			}
			OOWP[i]/=cnt;
		}
		printf("Case #%d:\n",++caseno);
		for(i=0;i<N;i++){
			double RPI=(0.25*(WP[i].wins/WP[i].games)) + (0.5*OWP[i] ) + (0.25*OOWP[i]);
			printf("%.10lf\n",RPI);
		}
	}
	return 0;
}


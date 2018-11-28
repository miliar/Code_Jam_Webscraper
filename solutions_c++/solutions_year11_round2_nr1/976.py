#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<algorithm>
#include<cmath>
#include<string>

using namespace std;

char Map[110][110];
double wp[110];
double owp[110];
double oowp[110];

double rip[110];

int main(){
	freopen("D://A-large.in","r",stdin);
    freopen("D://A-large.out","w",stdout);
	int t ; 
	scanf("%d",&t);
	for(int cases = 1 ; cases<=t;++cases){
		int n ; 
		scanf("%d",&n);
		for(int i = 0 ; i<n ;++i)
			for(int j = 0 ; j<n;++j){
				scanf(" %c",&Map[i][j]);
			}
		for(int i = 0 ; i<n ;++i){
			int w = 0 , sum = 0 ; 
			for(int j = 0 ; j<n ;++j){
				if( Map[i][j] != '.')
					sum++;
				if( Map[i][j] =='1')
					w++;
			}
			wp[i] = 1.0 * w / sum;
		}

		for(int i = 0 ; i<n ;++i){
			double tres = 0 ; 
			int sum = 0; 
			for(int j = 0 ; j<n ;++j){
				if( Map[i][j] !='.'){
					sum++;
					int w = 0 , tsum = 0 ; 
					for(int k = 0 ; k<n ;++k){
						if( k == i )continue; 
						if( Map[j][k] !='.')
							tsum++;
						if( Map[j][k] =='1')
							w++;
					}
					tres += 1.0 * w / tsum;
				}
			}
			owp[i] = tres / sum ;
		}

		for(int i = 0 ; i<n ;++i){
			int sum = 0;  
			double res = 0.0 ; 
			for(int j = 0 ; j<n;++j)
				if( Map[i][j] !='.'){sum++,res +=owp[j];}
			oowp[i] = res / sum ;
		}
		for(int i = 0 ; i<n ;++i)
			rip[i] = 0.25 * wp[i] + 0.50*owp[i]  + 0.25*oowp[i];
		printf("Case #%d:\n",cases);
		for(int i = 0 ; i<n ;++i)
			printf("%.10f\n",rip[i]);
	}
	return 0 ;
}
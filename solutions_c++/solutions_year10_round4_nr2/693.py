#include<stdio.h>
#include<stdlib.h>
long long int m[513];
long long int price[11][513];
long long int dptake[11][513][11];
long long int dpnotake[11][513][11];
double mymax(double a,double b){
	return a > b ? a : b;
}
long long int mymax(long long int a,long long int b){
	return a > b ? a : b;
}
long long int mymin(long long int a,long long int b){
	return a > b ? b : a;
}
long long int mymin(long long int a,long long int b,long long int c,long long int d){
	long long int min = 21474836470000LL;
	min = mymin(min,a);
	min = mymin(min,b);
	min = mymin(min,c);
	min = mymin(min,d);
	return min;
}
int main(){
	int ca;
	scanf("%d",&ca);
	for(int t=0;t<ca;t++){
		long long int p;
		scanf("%lld",&p);
		long long int n = (1 << p);
		long long int a[2];
		for(long long int i=0;i<n;i++){
			scanf("%lld",&a[i % 2]);
			a[i % 2] = p - a[i % 2]; 
			if(i % 2 == 1){
				m[i / 2] = mymax(a[0],a[1]);
			}
		}
		n = (1 << (p-1));
		for(long long int i=0;i<p;i++){
			long long int upper = (1 << ( p - 1 - i));
			for(long long int j=0;j<upper;j++){
				scanf("%lld",&price[i][j]);
			}
		}
		for(long long int j=0;j< (1 << (p-1));j++){
			for(long long int k=0;k<=p;k++){
				dptake[0][j][k] = dpnotake[0][j][k] = 10474836470000LL;
			}
			dptake[0][j][m[j] - 1] = price[0][j];
			dpnotake[0][j][m[j]] = 0;
		}
		for(long long int i=1;i<p;i++){
			long long int upper = (1 << ( p - 1 - i));
			for(long long int j=0;j<upper;j++){
				for(long long int k=0;k<=p;k++){
					long long int min = 214748364700000LL;
					for(long long int l=0;l<=k;l++){
						min = mymin(min,  dptake[i-1][j * 2 ][k] + dptake[i-1][j * 2 + 1][l] );
					}
					for(long long int l=0;l<=k;l++){
						min = mymin(min,  dpnotake[i-1][j * 2 ][k] + dptake[i-1][j * 2 + 1][l] );
					}
					for(long long int l=0;l<=k;l++){
						min = mymin(min,  dpnotake[i-1][j * 2 ][k] + dpnotake[i-1][j * 2 + 1][l] );
					}
					for(long long int l=0;l<=k;l++){
						min = mymin(min,  dptake[i-1][j * 2 ][k] + dpnotake[i-1][j * 2 + 1][l] );
					}
					for(long long int l=0;l<=k;l++){
						min = mymin(min,  dptake[i-1][j * 2 + 1][k] + dptake[i-1][j * 2][l] );
					}
					for(long long int l=0;l<=k;l++){
						min = mymin(min,  dpnotake[i-1][j * 2 + 1 ][k] + dptake[i-1][j * 2][l] );
					}
					for(long long int l=0;l<=k;l++){
						min = mymin(min,  dpnotake[i-1][j * 2 + 1][k] + dpnotake[i-1][j * 2][l] );
					}
					for(long long int l=0;l<=k;l++){
						min = mymin(min,  dptake[i-1][j * 2 + 1][k] + dpnotake[i-1][j * 2][l] );
					}
					dpnotake[i][j][k] = min;
					if(dpnotake[i][j][k] > 10474836470000LL){
						dpnotake[i][j][k] = 10474836470000LL;
					}
				}
				for(long long int k=0;k<p - 1;k++){
					dptake[i][j][k] = dpnotake[i][j][k + 1] + price[i][j];
				}
			}
		}/*
		for(long long int i=0;i<p;i++){
			long long int upper = (1 << ( p - 1 - i));
			for(long long int j=0;j<upper;j++){
				for(long long int k=0;k<=p;k++){
					prlong long intf("%d %d %d (%d,%d)\n",i,j,k,dptake[i][j][k],dpnotake[i][j][k]);
				}
			}
			
		}*/
		printf("Case #%d: %lld\n",t + 1,mymin(dptake[p-1][0][0],dpnotake[p-1][0][0]));
	}
	return 0;
}

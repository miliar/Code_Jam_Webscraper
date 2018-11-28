#include <iostream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <vector>
#include <set>
#include <map>

using namespace std;

int a[1<<10],p[1<<10];
int N,T;


long double P[1<<11],F[1<<11];

/*
void prework(){
	F[1] = 0;
	F[2] = 0.5;
	for (int i=3;i<=(1<<10);i++)
		F[i] = (F[i-2]+F[i-1]*(i-1))/i;
	P[0] = 
	P[1] = 1;
	P[2] = 2;
	for (int i=3;i<=(1<<5);i++){
		long double sigma = 0;
		for (int j=0;j<i;j++){
			long double tmp = F[j] * P[j];
			for (int k=1;k<=(i-j);k++)
				tmp /= k;
			sigma += tmp;
		}
		P[i] = (sigma + 1)/ (1-F[i]);
		cout << i <<" "<< P[i] << " "<< F[i] << endl;
	}
}
*/
int main(){
	
//	prework();

	scanf("%d",&T);

	for (int Test=1;Test<=T;Test++){
		scanf("%d",&N);
		memset(p,0,sizeof(p));
		for (int i=1;i<=N;i++)
			scanf("%d",a+i);
		for (int i=1;i<=N;i++)
			for (int j=1;j<=N;j++)
				if (a[i]>=a[j]) ++p[i];
		long double ans =0;
		for (int i=1;i<=N;i++)
			if (p[i]!=i){
				/*
				int k = p[i], tot = 0;
				while (p[i]!=i){
					swap(p[k],k);
					++tot;
				}
				*/
				++ans;
			}
		printf("Case #%d: %.8f\n",Test,(double)ans);
	}


	return 0;
}
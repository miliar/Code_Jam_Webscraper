/*
 *  B.cpp
 *  
 *
 *  Created by Pro.hessam on ۸۹/۳/۱.
 *  Copyright 2010 __MyCompanyName__. All rights reserved.
 *
 */

#include <iostream>

using namespace std;

const int MaxN= 100 + 4, MaxS= 300, INF= 1e9;

int d, p, m, n;
int a[MaxN];
int dyn[MaxN][MaxS];

int ABS(int k){
	return k>0 ? k : -k;
}
/*************************/
inline void SetDyn(){
	for (int i=1 ; i<=n ; i++){
		int s= a[i-1];
		for (int j=0 ; j<MaxS ; j++){
			dyn[i][j]= dyn[i-1][j] + d;
			if (m!=0){
				for (int r=j%m ; r<=256 ; r+= m)
					for (int k=max(0, r-m) ; k<=min(r+m, 256) ; k++)
						if (dyn[i][j] > dyn[i-1][k] + ABS(k-s) + ABS(r-j)/m*p)
							dyn[i][j] = dyn[i-1][k] + ABS(k-s) + ABS(r-j)/m*p;
			}else{
				int r= j;
				for (int k=max(0, r-m) ; k<=min(r+m, 256) ; k++)
					if (dyn[i][j] > dyn[i-1][k] + ABS(k-s))
						dyn[i][j] = dyn[i-1][k] + ABS(k-s);
			}
			
							
			
		}
	}
}
/*************************/
int main(){
	int test;
	cin >> test;
	for (int t=1 ; t<=test ; t++){
		cin >> d >> p >> m >> n;
		for (int i=0 ; i<n ; i++)
			cin >> a[i];
		SetDyn();
		int mini= INF;
		for (int i=0 ; i<=256 ; i++)
			if (dyn[n][i] < mini)
				mini= dyn[n][i];
		printf("Case #%d: %d\n", t, mini);
	}
	
	return 0;
}


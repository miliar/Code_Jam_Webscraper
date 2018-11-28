/*
 *  C.cpp
 *  
 *
 *  Created by Pro.hessam on ۸۹/۲/۱۸.
 *  Copyright 2010 __MyCompanyName__. All rights reserved.
 *
 */

#include <iostream>

using namespace std;

const int MaxN= 1000 + 5;

int g[MaxN], h[MaxN], p[MaxN];

int main(){
	int test;
	cin >> test;
	for (int t=1 ; t<=test ; t++){
		int r, k, n;
		cin >> r >> k >> n;
		for (int i=0 ; i<n ; i++)
			cin >> g[i];
		for (int i=0 ; i<n ; i++){
			p[i]= g[i];
			h[i]= 1;
			while(h[i]<n && p[i]+g[(i+h[i])%n] <= k){
				p[i]+= g[(i+h[i])%n];
				h[i]++;
			}
		}
		int now= 0, res= 0;
		while(r--){
			res+= p[now];
			now+= h[now];
			now%= n;
		}
		printf("Case #%d: %d\n", t, res);
	}
	
	return 0;
}


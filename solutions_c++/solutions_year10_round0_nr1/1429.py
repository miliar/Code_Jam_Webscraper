/*
 *  A.cpp
 *  
 *
 *  Created by Pro.hessam on ۸۹/۲/۱۸.
 *  Copyright 2010 __MyCompanyName__. All rights reserved.
 *
 */

#include <iostream>

using namespace std;

inline bool ON(int n, int k){
	for (int i=0 ; i<n ; i++){
		if (k%2 == 0)
			return false;
		k/= 2;
	}
	return true;
}
/***************************/
int main(){
	int test;
	cin >> test;
	for (int t=1 ; t<=test ; t++){
		int n, k;
		cin >> n >> k;
		if (ON(n, k))
			printf("Case #%d: ON\n", t);
		else
			printf("Case #%d: OFF\n", t);
	}
	return 0;
}


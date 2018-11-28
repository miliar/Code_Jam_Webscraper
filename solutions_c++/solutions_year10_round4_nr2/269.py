/*
 *  B.cpp
 *  
 *
 *  Created by Pro.hessam on ۸۹/۳/۱۵.
 *  Copyright 2010 __MyCompanyName__. All rights reserved.
 *
 */

#include <iostream>

using namespace std;

typedef long long ll;

const ll MaxN= 2024 + 5, INF= 1e8;
ll n, p;
ll m[MaxN];

ll MIN(ll r, ll now= 0){
	if (r<n)
		return min(MIN(2*r, now+1) + MIN(2*r+1, now+1), MIN(2*r, now) + MIN(2*r+1, now) + m[r]);
	else{
		if (now<=m[r])
			return 0;
		else
			return INF;
	}
}
/***********************/
int main(){
	int test;
	cin >>test;
	for (int t=1 ; t<=test ; t++){
		cin >> p;
		n= (1 << p);
		for (ll i=n ; i<2*n ; i++)
			cin >> m[i];
		reverse(m+n, m+2*n);
		for (ll i=n-1 ; i>=1 ; i--)
			cin >> m[i];
		ll res= MIN(1);
		printf("Case #%d: ", t);
		cout << res << endl;
	}
	
	return 0;
}


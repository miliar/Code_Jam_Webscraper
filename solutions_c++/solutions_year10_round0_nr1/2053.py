/*
 * A.cpp
 *
 *  Created on: May 8, 2010
 *      Author: Yasser
 */


#include<iostream>
#include<cstring>
#include<algorithm>
#include<vector>
#include<set>
#include<queue>
#include<map>
#include<sstream>
#include<cstdio>
#include<cmath>
#include<stack>
#include<complex>

using namespace std;

int main(){
#ifndef ONLINE_JUDGE
	freopen("test.in","rt",stdin);
	freopen("out.txt","wt",stdout);
#endif

	int TC,n,k;
	scanf("%d",&TC);
	for(int tt=0;tt<TC;tt++){
		scanf("%d %d",&n,&k);
		printf("Case #%d: %s\n",tt+1 , ((k+1)%(1<<n) == 0 ? "ON" : "OFF"));
	}
	return 0;
}

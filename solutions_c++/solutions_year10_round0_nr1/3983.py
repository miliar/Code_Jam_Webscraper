#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cmath>

using namespace std;

int t, n, k;
int main(){

	scanf("%d", &t);

	int ini;
	bool on;
	for(int i=1; i<=t; i++){
		scanf("%d%d", &n, &k);
		ini = pow(2, n);
		on = ((k-(ini-1))%ini)==0;		
		printf("Case #%d: %s\n", i, (on?"ON":"OFF"));
	}

	return(0);
}



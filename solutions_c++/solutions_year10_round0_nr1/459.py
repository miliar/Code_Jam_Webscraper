#include <stdio.h>
#include <iostream>
using namespace std;

int n, k, test;

bool solve(){
	while (n--){
		if (k%2==0) return false;
		k/=2;
	}
	return true;
}

int main(){
	scanf("%d", &test);
	for (int cas=1; cas<=test; cas++){
		scanf("%d%d", &n, &k);
		printf("Case #%d: ", cas);
		if (solve()) printf("ON\n"); else printf("OFF\n");
	}
	return 0;
}

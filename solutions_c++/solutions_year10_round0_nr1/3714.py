#include<cstdio>
#include<vector>
#include<iostream>

using namespace std;

main(){

	int T;
	int n,k;
	vector<int> Ns, Ks;
	int potegi[32];
	scanf("%d", &T);
	Ns.resize(T);
	Ks.resize(T);

	for(int i=0; i<T; i++){
		scanf("%d %d", &Ns[i], &Ks[i]);	
	}
	//
	potegi[0] = 1;
	for(int i=1; i<32; i++){
		potegi[i] = potegi[i-1]*2;
	}	
	//Liczenie
	for(int i=0; i<T; i++){
		k = Ks[i];
		n = potegi[Ns[i]];
		k %= n;
		printf("Case #%d: %s \n", (i+1), k==n-1?"ON":"OFF");
	}




}

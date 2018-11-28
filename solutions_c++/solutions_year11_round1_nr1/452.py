#include <cstdio>
#include <iostream>
#include <algorithm>
using namespace std;

int T,Pd,Pg;
long long N;

int gcd(int a, int b){
	if (b == 0)
       return a;
    else
       return gcd(b, a % b);
}

int main(){
	scanf("%d",&T);
	for (int a=1;a<=T;++a){
		cin >> N >> Pd >> Pg;
		printf("Case #%d: ",a);
		if (Pg == 100 && Pd < 100){
			printf("Broken\n");
			continue;
		}
		else if (Pg == 0 && Pd > 0){
			printf("Broken\n");
			continue;
		}	
		int f = 100/gcd(Pd,100);
		if (N < f){
			printf("Broken\n");
			continue;
		}
		printf("Possible\n");
	}
}

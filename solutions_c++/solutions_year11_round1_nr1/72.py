#include <stdio.h>
#include <string.h>
#include <iostream>
using namespace std;
int pD, pG;
int cp,tn;
long long n;
inline int gcd(int a, int b){return b==0?a:gcd(b,a%b);}
inline int check(){
	int g = gcd(pD, 100), pA = 100 / g;
	if (pA > n) return 0;
	if (pG == 0 && pD != 0) return 0;
	if (pG == 100 && pD != 100) return 0;
	return 1;
}
int main(){
	for (scanf("%d",&tn),cp=1;cp<=tn;cp++){
		cin>>n>>pD>>pG;
		if (check()) 
			printf("Case #%d: Possible\n", cp);
		else 
			printf("Case #%d: Broken\n", cp);
	}
	return 0;
}

#include <cstdio>
#include <cstring>
#include <algorithm>
#include <cmath>
#include <cctype>
#include <iostream>
#include <vector>

using namespace std;

typedef long long LL;

#define PB push_back
#define MP make_pair

int T;
LL n,d,g;

LL gcd(LL a,LL b) {
	if (a==0ll) return b;
	if (a>b) return gcd(b,a);
	return gcd(b%a,a);
}

int main(){
	scanf("%d",&T);
	
	for (int t=1;t<=T;t++) {
		printf("Case #%d: ",t);
		
		cin >> n >> d >> g ;
		
		LL x=100LL/gcd(d,100LL);
/*	
		cout << x << endl ;
*/
		if (n<x) {
			puts("Broken"); continue;
		}
		
		if (g==100ll&&d<100ll||g==0ll&&d>0ll) {
			puts("Broken"); continue;
		}
		
		puts("Possible");
	}

	return 0;
}

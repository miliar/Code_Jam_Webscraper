#include <cstdio>
#include <cmath>
#include <algorithm>
#include <iostream>
#include <cstring>

#define INF 100000000
#define MAX 1048576

using namespace std;

FILE *in = fopen("C-large.in", "r"), *out = fopen("results.txt", "w");

long long a, b, c, d, f;

int main() {
    scanf("%lld", &a);
    
    for (int t=0; t<a; t++) {
	f = 0;
	scanf("%lld%lld%lld", &b, &c, &d);
	if (b > 100) b = 100;
	
	for (int i=1; i<=b; i++) {
	    if (i*c % 100 == 0) f = 1;
	}
	if (c != 100 && d == 100) f = 0;
	if (c != 0 && d == 0) f = 0;
	
	if (f) {
	    printf("Case #%d: Possible\n", t+1);
	}
	else printf("Case #%d: Broken\n", t+1);
    }
   
    return 0;
}
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <iostream>
#include <cstring>

#define INF 100000000
#define MAX 1048576

using namespace std;

int n, a, b, c, s;

int maxScore(int p) {
    if (p == 0) return 0;
    return (p + 2) / 3;
}
int maxSScore(int p) {
    if (p == 0) return 0;
    return (p + 4) / 3;
}

int main() {
    scanf("%d", &n);
    
    for (int r=0; r<n; ++r) {
	int t = 0;
	
	scanf("%d%d%d", &a, &b, &c);
	for (int i=0; i<a; ++i) {
	    scanf("%d", &s);
	    
	    if (maxScore(s) >= c) ++t;
	    else if (b > 0 && maxSScore(s) >= c) ++t, --b;
	}
	printf("Case #%d: %d\n", r+1, t);
    }
   
    return 0;
}
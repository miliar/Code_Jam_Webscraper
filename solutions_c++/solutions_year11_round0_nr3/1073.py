#include <cstdio>
#include <cmath>
#include <algorithm>
#include <iostream>
#include <cstring>

#define INF 100000000
#define MAX 1048576

using namespace std;

FILE *in = fopen("C-large.in", "r"), *out = fopen("results.txt", "w");

int a, b, c, best[2][MAX], x, m;
long long t;

int main() {
    fscanf(in, "%d", &a);
    
    for (int i=0; i<a; i++) {
	fscanf(in, "%d", &b);
	m = INF;
	//memset(best[0], -1, sizeof(best[0]));
	t = x = best[0][0] = 0;
	for (int j=0; j<b; j++) {
	    fscanf(in, "%d", &c), x ^= c;
	    t += c, m = min(m, c);
	    /*memcpy(best[1], best[0], sizeof(best[0]));
	    for (int i=0; i<MAX; i++) {
		if (best[1][i] != -1) {
		    cout << (i^c) << "," << i << "," << best[1][i] << "," << c << endl;
		    best[0][i ^ c] = max(best[0][i ^ c], best[1][i] + c);
		    t = max(t, best[0][i ^ c]);
		}
	    }*/
	}
	if (x) printf("Case #%d: NO\n", i+1);
	else printf("Case #%d: %lld\n", i+1, t-m);
    }
    return 0;
}
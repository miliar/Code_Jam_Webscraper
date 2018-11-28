#include <cstdio>
#include <cmath>
#include <algorithm>
#include <iostream>
#include <cstring>

#define INF 100000000
#define MAX 1048576

using namespace std;

FILE *in = fopen("D-large.in", "r"), *out = fopen("results.txt", "w");

int a, b, c, n;
pair<int, int> p[1005];

int main() {
    fscanf(in, "%d", &a);
    
    for (int i=0; i<a; i++) {
	fscanf(in, "%d", &b), n = b;
	for (int j=0; j<b; j++) {
	    fscanf(in, "%d", &c);
	    p[j] = make_pair(c, j);
	}
	sort(p, p + b);
	for (int j=0; j<b; j++) {
	    if (j == p[j].second) n--;
	}
	printf("Case #%d: %f\n", i+1, (float)(n == 1 ? 0 : n));
    }
    return 0;
}
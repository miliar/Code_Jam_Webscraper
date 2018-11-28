#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <string>
#include <cstdlib>
#include <sstream>
#include <algorithm>
using namespace std;

int i, j, k;
int T, cs = 0;
int tot;
int X, S, R, t, N;
struct STRUCT{
    int S, E, W, L;
}w[1024];
bool operator<(const STRUCT& x, const STRUCT& y) {
     return x.W < y.W;
}
int main() {
    freopen("a2.in", "r", stdin);freopen("a.out", "w", stdout);
    scanf("%d", &T);
    while(T--){
       scanf("%d%d%d%d%d", &X, &S, &R, &t, &N);
       tot = X;
       for(i = 0; i < N; ++i){
           scanf("%d%d%d", &w[i].S, &w[i].E, &w[i].W);
           w[i].L = w[i].E - w[i].S;
           tot -= w[i].L;
       }
       w[N].L = tot;
       w[N].W = 0;
       N++;
       sort(w, w + N);
       
       
       double rest = t, ans = 0;
       for(i = 0; i < N; ++i) {
           double tt = w[i].L * 1.0 / (R + w[i].W);
           tt = min(tt, rest);
           ans += tt + (w[i].L - tt * (R + w[i].W)) * 1.0 / (S + w[i].W);
           rest -= tt;
       }
       
       printf("Case #%d: %.6lf\n", ++cs, ans);
    }
	return 0;
}


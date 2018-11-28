#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <inttypes.h>
#include <ctype.h>
#include <algorithm>
#include <utility>
#include <iostream>
using namespace std;
#define TRACE(x...)
#define PRINT(x...) TRACE(printf(x))
#define WATCH(x) TRACE(cout << #x" = " << x << "\n")
#define _inline(f...) f() __attribute__((always_inline)); f
#define _foreach(it, b, e) for (typeof(b) it = (b); it != (e); it++)
#define foreach(x...) _foreach(x)
#define all(v) (v).begin(), (v).end()
#define rall(v) (v).rbegin(), (v).rend()
const int INF = 0x3F3F3F3F;
const int NULO = -1;
const double EPS = 1e-10;
_inline(int cmp)(double x, double y = 0, double tol = EPS) {
  return (x <= y + tol) ? (x + tol < y) ? -1 : 0 : 1;
}

int tipo[10010];
int pode[10010];
int val[10010];
int M, V;
#define FOLHA(i) ((i) > (M-1)/2)
void acha(int v) {
     if (FOLHA(v))
        return;
     acha(2*v);
     acha(2*v+1);
     val[v] = val[2*v];
     if (tipo[v] == 1)
        val[v] &= val[2*v+1];
     else
         val[v] |= val[2*v+1];
}

int mini(int no, int valor) {
    if (val[no] == valor)
       return 0;
    if (FOLHA(no))
       return -1;
    int m1 = mini(2*no, valor);
    int m2 = mini(2*no+1, valor);
    int m;
    if (m1 == -1 && m2 == -1)
       return -1;
    if (m1 != -1 && (m2 == -1 || m1 < m2))
        m = m1;
    else
        m = m2;
    if (tipo[no] == valor) { // Preciso dos 2
       if (m1 == -1 || m2 == -1) {
          if (pode[no])
              return 1 + m;
          else
              return -1;
       }
       int r = m1 + m2;
       if (pode[no])
          r = min(r, 1 + m);
       return r;
    }
    return m;
}

int main() {
  TRACE(setbuf(stdout, NULL));
	int _43;
	scanf("%d", &_43);
	foreach(_42, 1, _43+1) {
		printf("Case #%d:", _42);
		scanf("%d %d", &M, &V);
		foreach(i, 1, (M-1)/2 + 1) {
                  scanf("%d %d", &tipo[i], &pode[i]);
        }
        foreach(i, (M-1)/2 + 1, M+1) {
                   scanf("%d", &val[i]);
        }
        acha(1);
        int r = mini(1, V);
        if (r == -1)
           printf(" IMPOSSIBLE\n");
        else
            printf(" %d\n", r);
	}
  return 0;
}

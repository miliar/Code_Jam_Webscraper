#include <stdio.h>
#include <algorithm>
using namespace std;

#define max(a,b) (a>b?a:b)

struct node {
    int p, v;
}we[300];

int n, d;


int cmp(node a,node b) {
    return a.p < b.p;
}

bool ok(long long tim) {
     int i;
     long long cur = 10000000;
     cur *= cur*(-1);
     for (i = 0; i < n; i++) {
         long long x = max(cur,we[i].p-tim);
         long long y = we[i].p+tim;
         if (y < x) return false;
         if ( (y-x)/d+1 < we[i].v ) return false;
         cur = x+we[i].v*d;
     }
     return true;
}

int main () {
    int kase,  i, h = 1;
    freopen("B-small-attempt0.in","r",stdin);
    freopen("b.out","w",stdout);
    scanf("%d", &kase);
    while (kase--) {
          scanf("%d %d", &n, &d);
          for (i = 0; i < n; i++) {
              scanf("%d %d", &we[i].p , &we[i].v);
              we[i].p *= 2;
          }
          d*=2;
          sort(we,we+n,cmp);
          long long head, tail = 10000000;
           head = 0; tail = tail*tail*2;
           while ( head < tail) {
                 long long mid = (head+tail)/2;
                 if ( ok(mid) ) tail = mid;
                 else head = mid+1;
           }
           printf("Case #%d: %1f\n",h++, head*1.0/2);
    }
    return 0;
}

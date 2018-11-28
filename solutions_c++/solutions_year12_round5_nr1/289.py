#include <stdio.h>
#include <string.h>
#include <math.h>
#include <algorithm>
using namespace std;

struct node {
       int a;
       int b;
       int k;
}all[1011];

#define ep 1e-8

bool equal(double a,double b) {
     if ( fabs(a-b) < ep ) return true;
     return false;
}

int cmp(node aa,node bb) {
    if (aa.b == 0 && bb.b == 0) {
       return aa.k < bb.k;
    }
    if (aa.b == 0) {
       return 0;
    }
    if (bb.b == 0) {
       return 1;
    }
    double a = bb.a*1.0/(100-aa.b);
    double b = aa.a*1.0/(100-bb.b);
    if ( equal(a,b) ) {
       return aa.k < bb.k;
    }
    return a > b;
}

int main () {
    int kase;
    int h = 1;
    int n;
    freopen("A-small-attempt0.in","r",stdin);
    freopen("out.txt","w",stdout);
    scanf("%d", &kase);
    while (kase--) {
          scanf("%d", &n);
          for (int i = 0; i < n; ++i) {
              scanf("%d",&all[i].a);    
              all[i].k = i;
          }
          for (int i = 0; i < n; ++i) {
              scanf("%d",&all[i].b);   
          }
          sort(all,all+n,cmp);
          
          printf("Case #%d: ",h++);
          for (int i = 0; i < n; ++i) {
              printf(" %d",all[i].k);
          }
          printf("\n");
    }
    return 0;
}

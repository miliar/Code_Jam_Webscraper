#include <stdio.h>
#include <string.h>
#include <algorithm>
using namespace std;

#define max(a,b) (a>b?a:b)
#define min(a,b) (a>b?b:a)

struct node{
   int k;
   int v;
}a[1010];
int x[1010],y[1010];
int used[1010];
int w, l;

int cmp(node a,node b) {
     return a.v > b.v;
}

int sum = 0;
int n;
void fen(int tx,int ty,int leftx,int lefty) {
     if (sum == n) return;
     for (int i = 0; i < n; ++i) {
         if (used[i] == 0) {
             bool isok = true;
             if (tx == 0) {
                if (leftx == 2*w || leftx >= a[i].v)
                   x[i] = tx;
             } 
             else if (leftx >= 2*a[i].v) {
                 x[i] = tx+a[i].v;
             }
             else if (tx+leftx==2*w && leftx >= a[i].v) {
                  x[i] = tx+leftx;
             }
             else {
                  isok = false;
             }
             if (ty == 0) {
                if (lefty==2*l || lefty >= a[i].v)
                        y[i] = ty; 
             } 
             else if (lefty >= 2*a[i].v) {
                 y[i] = ty+a[i].v;
             }
             else if (ty+lefty==2*l && lefty >= a[i].v) {
                  y[i] = ty+lefty;
             }
             else {
                  isok = false;
             }
             if (isok) {
                used[i] = true;
                sum++;
                if (x[i]+a[i].v >= 2*w && y[i]+a[i].v >= 2*l) continue;
                if (x[i]+a[i].v >= 2*w) {
                    fen(tx,ty+a[i].v,leftx,lefty-(y[i]-ty)-a[i].v); 
                    continue;
                }
                else if (y[i]+a[i].v >= 2*l) {
                     fen(tx+a[i].v,ty,leftx-(x[i]-tx)-a[i].v,lefty);
                     continue;
                }
                int a1 = max(min(leftx,lefty-(y[i]-ty)-a[i].v),min(leftx-(x[i]-tx)-a[i].v,(y[i]-ty)+a[i].v));
                int a2 = max(min(leftx-(x[i]-tx)-a[i].v,lefty),min(lefty-(y[i]-ty)-a[i].v,(x[i]-tx)+a[i].v));
                if (a1>a2){
                   fen(tx,ty+a[i].v,leftx,lefty-(y[i]-ty)-a[i].v);
                   fen(tx+a[i].v,ty,leftx-(x[i]-tx)-a[i].v,(y[i]-ty)+a[i].v);
                }
                else {
                     fen(tx+a[i].v,ty,leftx-(x[i]-tx)-a[i].v,lefty);
                     fen(tx,ty+a[i].v,(x[i]-tx)+a[i].v,lefty-(y[i]-ty)-a[i].v);
                }
             }
         }
     }
}

int main () {
    int kase;
    freopen("B-small-attempt0.in","r",stdin);
 //   freopen("b.txt","w",stdout);
    scanf("%d", &kase);
    int h = 1;
    while (kase--) {
          scanf("%d %d %d", &n, &w, &l);
          int v;
          for (int i = 0; i < n; ++i) {
              scanf("%d", &v);
              a[i].v = v*2;
              a[i].k = i;
          }
          sort(a,a+n,cmp);
          sum = 0;
          memset(used,0,sizeof(used));
          fen(0,0,2*w,2*l);
         
      //    printf("Case #%d:",h++);
           if (sum != n)
                   printf("error\n");
          for (int i = 0; i < n; ++i) {
              for (int j = 0; j < n; ++j) {
                  if (a[j].k == i) {
                       //printf(" %lf %lf", x[j]/2.0, y[j]/2.0);
                       break;
                  }
              }
          }
//          printf("\n");
    }
    while (1);
    return 0;
}

#include <cstdio>
#include <iostream>
using namespace std;

const int maxn=128;

int dx[]={-1,0,0,1};
int dy[]={0,-1,1,0};

int a[maxn][maxn];
char label[maxn][maxn];
int qx[maxn*maxn], qy[maxn*maxn], qs, qf;
int px[maxn][maxn], py[maxn][maxn];
int n, m;


int main() {
 freopen("b-large.in", "r", stdin);
 freopen("b-large.out", "w", stdout);

 int T; scanf("%d", &T);
 for (int tc=1; tc<=T; ++tc) {
  scanf("%d %d", &n, &m);
  for (int i=0; i<n; ++i)
   for (int j=0; j<m; ++j)
    scanf("%d", &a[i][j]);

  memset(label, 0, sizeof(label));
  memset(px, 0xff, sizeof(px));
  memset(py, 0xff, sizeof(py));
  char key='a';
  for (int i=0; i<n; ++i)
   for (int j=0; j<m; ++j) if (!label[i][j]) {
    qs=qf=0;
    qx[qf]=i, qy[qf++]=j;
    int sx, sy;
    for (; qs<qf; ++qs) {
     int x=qx[qs], y=qy[qs];     
     int tx, ty, d=1000000000;
     for (int i=0; i<4; ++i) {
      int nx=x+dx[i], ny=y+dy[i];
      if (nx>=0 && nx<n && ny>=0 && ny<m && a[x][y]>a[nx][ny]) {       
       if (a[nx][ny]<d)
         d=a[nx][ny], tx=nx, ty=ny;       
      }
     }

     if (d==1000000000) {
       sx=x, sy=y;
       label[sx][sy]=key++;
       break;
     } {
       if (label[tx][ty]) {
         px[tx][ty]=x, py[tx][ty]=y;
         sx=tx, sy=ty;
         break;
       } else {
         px[tx][ty]=x, py[tx][ty]=y;
         qx[qf]=tx, qy[qf++]=ty;
       }
     }
    }

    char lab=label[sx][sy];
    for (; ; ) {
     int nx=px[sx][sy];
     int ny=py[sx][sy];
     if (nx==-1) break;
     sx=nx, sy=ny;
     label[sx][sy]=lab;
    }

   }

   printf("Case #%d:\n", tc);
   for (int i=0; i<n; ++i) {
    for (int j=0; j<m; ++j) {
     if (j) putchar(' ');
     putchar(label[i][j]);
    }
    puts("");
   }




 }

 return 0;
}

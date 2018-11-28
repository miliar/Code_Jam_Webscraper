#include <cstdio>
#include <vector>
#include <string>
using namespace std;

int di[4]={-1,0,0,1};
int dj[4]={0,0-1,1,0};

int H,W;
int A[128][128];
int B[128][128];
char C[128][128];

int Dif(int i, int j, int d)
  {
  int ni=i+di[d];
  int nj=j+dj[d];
  if (ni<0 || nj<0 || ni>=H || nj>=W) return 1000000;
  return A[ni][nj]-A[i][j];
  }

void Rec(int i, int j)
  {
  for(int d=0;d<4;++d)
    {
    int ni=i+di[d];
    int nj=j+dj[d];
    if (ni<0 || nj<0 || ni>=H || nj>=W) continue;
    if (C[ni][nj]!=' ') continue;
    if (B[ni][nj]==-1) continue;
    if (ni+di[B[ni][nj]]!=i || nj+dj[B[ni][nj]]!=j) continue;

    C[ni][nj]=C[i][j];
    Rec(ni,nj);
    }
  }

void FindSink(int h, int w, int &h2, int &w2)
  {
  while(true)
    {
    int d=B[h][w];
    if (d==-1) break;
    h=h+di[d];
    w=w+dj[d];
    }
  h2=h;
  w2=w;
  }

int main()
  {
  int T;

  scanf("%d\n",&T);
  for(int t=0;t<T;++t)
    {
    scanf("%d %d\n",&H,&W);
    for(int h=0;h<H;++h)
      {
      for(int w=0;w<W;++w)
        {
        scanf("%d",&A[h][w]);
        C[h][w]=' ';
        }
      }

    for(int h=0;h<H;++h)
      {
      for(int w=0;w<W;++w)
        {
        int num=-1;
        int best=10000001;
        for(int d=0;d<4;++d)
          {
          int dif=Dif(h,w,d);
          if (dif<best) {best=dif;num=d;}
          }
        if (best>=0) B[h][w]=-1; else B[h][w]=num;
        }
      }

    char let='a';
    for(int h=0;h<H;++h)
      for(int w=0;w<W;++w) if (C[h][w]==' ')
        {
        int h2,w2;
        FindSink(h,w,h2,w2);
        C[h2][w2]=let++;
        Rec(h2,w2);
        }

    printf("Case #%d:\n", t+1);
    for(int h=0;h<H;++h)
      {
      for(int w=0;w<W;++w) printf("%c ",C[h][w]);
      printf("\n");
      }
    }

  return 0;
  }
#include <cmath>
#include <map>
#include <set>
#include <algorithm>
#include <iostream>
#define MOD 10007

using namespace std; typedef unsigned long ulong; typedef long long llong;

char block[100][100];
int cont[100][100];

int h,w,R;

int doit(int x, int y)
{

  for(int i=h-1;i>=0;i--) for(int j=w-1;j>=0;j--)
  {
    if (block[i][j]) cont[i][j]=0;
    else
    {
      cont[i][j] = 0;
      if (i+2 < h && j+1 < w) cont[i][j] += cont[i+2][j+1];
      if (i+1 < h && j+2 < w) cont[i][j] += cont[i+1][j+2];
      cont[i][j] %= MOD;
    }
    cont[h-1][w-1]=1;
  }
  return cont[0][0];
}

int main()
{
int cases;

cin >> cases; getchar();

for(int loop=1;loop<=cases;loop++)
{
  int i,j,k;

  cin >> h >> w >> R;

  memset(block,0,sizeof(block));
  memset(cont,-1,sizeof(cont));

  for(i=0;i<R;i++) { int r,c; cin >> r >> c; block[r-1][c-1]=1; }

  printf("Case #%d: %d\n",loop,doit(0,0));

//  for(i=0;i<h;i++) { for(j=0;j<w;j++) printf("%c",cont[i][j]>0?('0'+cont[i][j]):'*'); putchar(10); }

 // puts("");
  fflush(stdout);
}

}

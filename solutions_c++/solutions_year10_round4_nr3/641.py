#include <cmath>
#include <vector>
#include <map>
#include <set>
#include <algorithm>
#include <iostream>

using namespace std; typedef unsigned long ul; typedef long long ll;
typedef unsigned long long ull;

int B[200][200];
int n;

int sim() { for(int x=100;x>0;x--) for(int y=100;y>0;y--) if(B[x-1][y]==B[x][y-1]) { n += (B[x-1][y]-B[x][y]); B[x][y]=B[x][y-1]; } }

int main()
{
int cases;

cin >> cases; getchar();

for(int loop=1;loop<=cases;loop++)
{
  int i,j,k;
  int r, x1, x2, y1, y2;
  memset(B,0,sizeof(B));

  n=0;

  cin >> r;
  for(int i=0;i<r;i++)
  {
    cin >> x1 >> y1 >> x2 >> y2;
    for(int x=x1; x<=x2; x++ )for(int y=y1;y<=y2;y++)
    { n += (1-B[x][y]); B[x][y]=1; }
  }

  int t=0;
  while(n>0) {t++; sim();}

  printf("Case #%d: ",loop);

  printf("%d",t);

  puts("");
  fflush(stdout);
}

}

#include <cmath>
#include <vector>
#include <map>
#include <set>
#include <algorithm>
#include <iostream>

using namespace std; typedef unsigned long ul; typedef long long ll;
typedef unsigned long long ull;

int main()
{
int cases;

cin >> cases; getchar();

for(int loop=1;loop<=cases;loop++)
{
  int tix[20][1000];
  int p,m,t;

  memset(tix,0,sizeof(tix));

  cin >> p;

  for(int i=0;i<(1<<p);i++)
  {
    cin >> m; m = p-m;
    for(int j=0;j<m;j++) tix[j][i>>(p-j)] = 1;
  }

  int z; for(int i=0;i<(1<<p)-1;i++) cin >> z;

  t= 0;
  for(int i=0;i<p;i++)
  {
    for(int j=0;j<(1<<i);j++) t+=tix[i][j];
  }

  printf("Case #%d: ",loop);
  printf("%d",t);

  puts("");
  fflush(stdout);
}

}

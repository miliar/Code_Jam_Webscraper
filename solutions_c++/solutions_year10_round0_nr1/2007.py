#include <cstdio>
#include <cstring>
using namespace std;

int n, k;

int main()
{
 //freopen("A-large.in","r",stdin);
 //freopen("A-large.out","w",stdout);
 int t;
 scanf("%d",&t);
 for(int i = 1; i <= t ; i++)
 { 
  scanf("%d%d",&n,&k);
  ((k+1)%(1<<n) == 0)? printf("Case #%d: ON\n",i):printf("Case #%d: OFF\n",i);
 }
  return 0;
}
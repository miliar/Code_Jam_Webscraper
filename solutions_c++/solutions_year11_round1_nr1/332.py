#include<iostream>
#include<algorithm>
#include<cstring>
#include<cstdio>
using namespace std;

long long n;
int pd, pg;
int z;
int cases;

int gcd(int x, int y) 
{
    if (!y) return x;
    return gcd(y, x%y);
}
int main()
{
    freopen("A2.in","r",stdin);
    freopen("A2.out","w",stdout);
    
    scanf("%d",&cases);
    for (int k = 1; k <= cases; ++k) {
      printf("Case #%d: ",k);
      scanf("%lld%d%d",&n,&pd,&pg);
      z = 100/gcd(100,pd);
      if (n/z == 0) printf("Broken");
      else {
        if (pd < 100 && pg == 100) printf("Broken");
        else if (pd && pg == 0) printf("Broken");
        else printf("Possible");
      }
      printf("\n");
    }
    return 0;
}

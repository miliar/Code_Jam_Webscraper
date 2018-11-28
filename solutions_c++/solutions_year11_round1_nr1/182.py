#include <algorithm>
#include <iostream>
#include <vector>
#include <map>

using namespace std;

typedef long long ll;
typedef unsigned long long ull;
typedef unsigned long ul;
typedef unsigned short us;
typedef unsigned char uc;

// Optimized for x<y
ull gcd(ull x,ull y){ull t;if(!x)return y;for(y%=x;y;t=y,y=x%y,x=t);return x;}

main()
{
  int cases;
  cin >> cases;
  for(int loop=1; loop<=cases; loop++)
  {
    printf("Case #%d: ",loop);

    ull n,pd,pg;
    cin >> n >> pd >> pg;
    int d = 100/gcd(100,pd);
    if (d > n) { puts("Broken"); continue; }
    if (pg==100 && pd<100) puts("Broken");
    else if (pg==0 && pd>0) puts("Broken");
    else puts("Possible");
    // puts("");
  }
}

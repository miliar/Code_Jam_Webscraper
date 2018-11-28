#include<iostream>
#include<cstdio>
using namespace std;

int gcd (int x, int y)
{
    if (y == 0 )
    return x;
    return gcd(y, x%y);
}

bool cal ()
{
     long long n;
     bool result = true;
     int minD, minG;
     int pd, pg;
     scanf ("%lld %d %d",&n, &pd, &pg);
     minD = 100 / gcd (100, pd); 
    // printf ("%d\n", minD);
     if (minD > n) 
     {
         result = false;
     }
     if (pg > pd)
     {
            if (pg == 100)
            result = false;
     }
     else if (pg < pd)
     {
             if (pg == 0)
             result = false;
     }
     return result;
}

int main()
{
   int T,i;
  //  freopen("A-large.in", "r", stdin);
  //   freopen("A-large.out", "w", stdout);
     scanf("%d", &T);
    for (i = 1; i<= T; i++)
    {
        if (cal())
        printf ("Case #%d: Possible\n", i);
        else 
        printf ("Case #%d: Broken\n", i);
    }
  
   // system("pause");
    return 0;
}

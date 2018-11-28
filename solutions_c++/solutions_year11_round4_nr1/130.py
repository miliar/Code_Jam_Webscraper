#include <algorithm>
#include <bitset>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <deque>
#include <fstream>
#include <functional>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <utility>
#include <vector>
using namespace std;

struct pal
{
  int u,v,speed;
} p[1005];

bool cmp(pal A,pal B)
{
     return A.speed < B.speed;
 }
 
int T,n;
double X,s,r,t;

int main()
{
    freopen("a.i2","r",stdin);
    freopen("a.o2","w",stdout);
    
    scanf("%d", &T);
    for (int it = 1; it <= T; it++)
    {
        scanf("%lf %lf %lf %lf %d", &X, &s, &r, &t, &n);
        double walkDist = X,runTime = t;
        for (int i = 0; i < n; i++) 
        {
            scanf("%d %d %d", &p[i].u, &p[i].v, &p[i].speed);  walkDist -= (p[i].v - p[i].u);
        }
        sort(p,p + n,cmp);        
        double ret = 0;
        if (walkDist/r <= runTime)
        {
          ret += walkDist/r;  runTime -= ret;  walkDist = 0;
        }
        else
        {
            runTime = 0;  walkDist -= t * r;  ret += t;
        }
        
        ret += walkDist/s;
        for (int i = 0; i < n; i++)
        {
            double L = p[i].v - p[i].u;
            double tmp = L/(r + p[i].speed);
            if (tmp <= runTime)
            {
              ret += tmp;  runTime -= tmp;  L = 0;
            }
            else
            {
                ret += runTime;  L -= runTime * (r + p[i].speed);  runTime = 0;
            }
            ret += 1.0 * L/(s + p[i].speed);
        }
        
        printf("Case #%d: %.9lf\n", it, ret);
    }
}

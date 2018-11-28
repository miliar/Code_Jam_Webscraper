#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <string>
#include <functional>
#include <numeric>
#include <utility>
#include <fstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>
#include <algorithm>

using namespace std;

typedef vector<int> vi; 
typedef vector<vi> vvi; 
typedef pair<int,int> ii; 
#define sz(a) int((a).size()) 
#define pb push_back 
#define all(c) (c).begin(),(c).end() 
#define tr(c,i) for(typeof((c).begin()) i = (c).begin(); i != (c).end(); i++) 
#define present(c,x) ((c).find(x) != (c).end()) 
#define cpresent(c,x) (find(all(c),x) != (c).end()) 

const int oo = 0x7fffffff;
const double PI = atan2(0.0, -1.0);
const double eps=(1.0e-9);

int gcd(int a, int b)
{
   if(b==0) return a;
   else return gcd(b,a%b);
}

inline bool equal(double a,double b)
{
    return a-b>=-eps&&a-b<=eps;
}

double cal(int x1,int y1,int x2,int y2)
{
    double a=sqrt( x1*x1+y1*y1 );
    double b=sqrt( x2*x2+y2*y2 );
    double c=sqrt( (x1-x2)*(x1-x2) + (y1-y2)*(y1-y2) );
    
    double cosa=0.5*(a*a+b*b-c*c)/a/b;
    double sina=sqrt(1.0-cosa*cosa);
    
    return a*b*sina;
}

int main()
{
    freopen("B-small.in","r",stdin);
    freopen("B-large.out","w",stdout);
   
   int cas,re,x1,x2,y1,y2,n,m,a;
   
   for(scanf("%d",&re),cas=1;re--;++cas){
       scanf("%d%d%d",&n,&m,&a);
       bool ans=false;
       for(x1=0;x1<=n;++x1)
           for(y1=0;y1<=m;++y1)
               for(x2=0;x2<=n;++x2)
                   for(y2=0;y2<=m;++y2)
                       if(equal(cal(x1,y1,x2,y2),a)){// printf("%lf %d  %d  %d  %d\n",cal(x1,y1,x2,y2),x1,y1,x2,y2);
                           ans=true;
                           goto over;
                       }
       over:
       if(ans)
           printf("Case #%d: 0 0 %d %d %d %d\n",cas,x1,y1,x2,y2);
       else
           printf("Case #%d: IMPOSSIBLE\n",cas);
   }
    
}
















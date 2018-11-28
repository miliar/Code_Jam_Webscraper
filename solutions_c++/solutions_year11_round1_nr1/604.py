#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <fstream>
#define MMset(a,b) memset(a,b,sizeof(a))
#define min(a,b)   ((a)<(b)?(a):(b))
#define max(a,b)   ((a)>(b)?(a):(b))
using namespace std;
long long gcd(long long a,long long b)
{
     if (b==0) return a;
     else      return gcd(b,a%b);
}
long long N,PD,PG;
int main()
{
    int T;
    cin>>T;
    freopen("test.out","w",stdout);
    for (int cas=1;cas<=T;cas++)
    {
        cin>>N>>PD>>PG;
        if ((PG==100 && PD!=100)||(PG==0 && PD!=0)) 
        {
           printf("Case #%d: Broken\n",cas);
           continue;
        }
        if (PD==0) 
        {
           printf("Case #%d: Possible\n",cas);
           continue;
        }
        long long minn=(100)/gcd(PD,100);
        if (minn<=N) printf("Case #%d: Possible\n",cas);
        else       printf("Case #%d: Broken\n",cas);
    }
}

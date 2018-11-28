#include <cstdlib>
#include <cctype>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <iostream>
#include <sstream>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <fstream>
#include <numeric>
#include <iomanip>
#include <bitset>
#include <list>
#include <stdexcept>
#include <functional>
#include <utility>
#include <ctime>

using namespace std;
long long a1,a2,b1,b2;

int main()
{
    freopen("c.in","r",stdin);
    freopen("c.out","w",stdout);
    int T;
    scanf("%d",&T);
    for (int j=1;j<=T;j++)
    {
        long long ans=0;
        cin >> a1 >> a2 >> b1 >> b2;
        for (long long i=a1;i<=a2;i++)
        {
            double p=0.618033988749;
            long long l=i*p+1,r=i/p;
            l=max(l,b1);r=min(r,b2);
            if (r>=l) ans+=r-l+1LL;
        }
        cout<< "Case #" << j << ": " << (a2-a1+1)*(b2-b1+1)-ans<< endl;;
    }
}

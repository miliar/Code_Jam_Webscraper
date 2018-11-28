#include <iostream>
#include <cstdio>
#include <cmath>
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
#include <string.h>

using namespace std;

#define PB push_back
#define MP make_pair
#define REP(i,n) for(i=0;i<(n);++i)
#define FOR(i,l,h) for(i=(l);i<=(h);++i)
#define FORD(i,h,l) for(i=(h);i>=(l);--i)

typedef vector<int> VI;
typedef vector<string> VS;
typedef vector<double> VD;
typedef long long LL;
typedef pair<int,int> PII;

bool solve(int a,int b)
{
    if (a == b)
        return false;
    else if (a < b)
    {
        return solve(b,a);
    }
    else
    {
        if (a >= 2*b)
            return true;
        else
            return !solve(a-b,b);
    }
}

int main()
{
    int T = 0;
    cin >> T;
    for (int t = 1;t <= T;t++)
    {
        int a1,a2,b1,b2;
        cin >> a1 >> a2 >> b1 >> b2;
        int cnt = 0;
        for (int a = a1;a <= a2;a++)
        {
            for (int b = b1;b <= b2;b++)
            {
                if (solve(a,b))
                {
                    //cout << a << " " << b << endl;
                    cnt++;
                }
            }
        }
        printf("Case #%d: %d\n",t,cnt);
    }
    return 0;
}

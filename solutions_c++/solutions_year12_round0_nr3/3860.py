#include <functional>
#include <algorithm>
#include <stdexcept>
#include <iostream>
#include <sstream>
#include <fstream>
#include <numeric>
#include <iomanip>
#include <cstdlib>
#include <cstring>
#include <utility>
#include <cctype>
#include <vector>
#include <string>
#include <bitset>
#include <cmath>
#include <queue>
#include <stdio.h>
#include <stack>
#include <ctime>
#include <list>
#include <map>
#include <set>
#include <assert.h>
#define REP(i,n) for(int i=0;i<n;i++)
#define TR(i,x) for(typeof(x.begin()) i=x.begin();i!=x.end();i++)
#define ALL(x) x.begin(),x.end()
#define SORT(x) sort(ALL(x))
#define CLEAR(x) memset(x,0,sizeof(x))
#define FILL(x,c) memset(x,c,sizeof(x))

using namespace std;

const double eps = 1e-8;

#define PB push_back
#define MP make_pair

typedef map<int,int> MII;
typedef map<string,int> MSI;
typedef vector<int> VI;
typedef vector<string> VS;
typedef vector<long double> VD;
typedef pair<int,int> PII;
typedef long long int64;
typedef long long ll;
typedef unsigned int UI;
typedef long double LD;
typedef unsigned long long ULL;

bool used[2000007];
int power[10];

int main()
{
    power[0] = 1;
    for (int i = 1; i < 10; ++i)
        power[i] = power[i-1] * 10;

    int cases, nowCase = 0;
    scanf("%d", &cases);
    while (cases--)
    {
        int a, b;
        scanf("%d%d", &a, &b);
        for (int i = a; i <= b; ++i)
            used[i] = false;
        long long ans = 0;
        int t[10];
        for (int i = a; i <= b; ++i)
            if (!used[i])
            {
                int now = 0, tmp = i;
                while (tmp)
                {
                    t[now++] = tmp%10;
                    tmp /= 10;
                }
                int co = 1;
                for (int j = 0; j < now-1; ++j)
                    if (t[j] != 0)
                    {
                        int cnt = i%power[j+1]*power[now-1-j]+i/power[j+1];
                        if (cnt != i && cnt >= a && cnt <= b && !used[cnt])
                        {
                            ++co;
                            used[cnt] = true;
                        }
                    }
                ans += (long long)co*(co-1)/2;
            }
        printf("Case #%d: ", ++nowCase);
        cout << ans << endl;
    }
    return 0;
}

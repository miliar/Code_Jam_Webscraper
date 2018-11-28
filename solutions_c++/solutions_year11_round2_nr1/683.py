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

typedef vector<int> VI;
typedef vector<string> VS;
typedef vector<long double> VD;
typedef pair<int,int> PII;
typedef long long LL;
typedef unsigned long long ULL;

char mp[128][128];
double a[127],b[127],c[127];
int total[127];

int main()
{
    int T;
    cin >> T;
    for (int cs = 0;cs < T;++cs)
    {
        int n;
        cin >> n;
        CLEAR(a);
        CLEAR(b);
        for (int i = 0;i < n;++i)
        {
            scanf("%s",mp[i]);
            int w = 0,t = 0;
            for (int j = 0;j < n;++j)
            {
                if (mp[i][j] == '1') ++w;
                if (mp[i][j] != '.') ++t;
            }
            a[i] = 0;
            if (t)
                a[i] = (double)w/t;
            total[i] = t;
        }
        for (int i = 0;i < n;++i)
            c[i] = a[i] * 0.25;
        for (int i = 0;i < n;++i)
        {
            b[i] = 0;
            if (!total[i]) continue;
            for (int j = 0;j < n;++j)
                if (mp[i][j] != '.')
                {
                    int t = 0,w = 0;
                    for (int k = 0;k < n;++k)
                        if (k != i && mp[j][k] != '.')
                        {
                            if (mp[j][k] == '1') ++w;
                            if (mp[j][k] != '.') ++t;
                        }
                    b[i] += (double)w/t;
                }
            b[i] /= (double)total[i];
        }
        for (int i = 0;i < n;++i)
        {
            c[i] += b[i] * 0.5;
            a[i] = b[i];
        }
        for (int i = 0;i < n;++i)
        {
            b[i] = 0;
            if (!total[i]) continue;
            for (int j = 0;j < n;++j)
                if (mp[i][j] != '.')
                {
                    b[i] += a[j];
                }
            b[i] /= (double)total[i];
        }
        for (int i = 0;i < n;++i)
        {
            c[i] += b[i] * 0.25;
            a[i] = b[i];
        }
        cout << "Case #" << cs+1 << ":\n";
        for (int i = 0;i < n;++i)
            printf("%.7f\n",c[i]);
    }

}

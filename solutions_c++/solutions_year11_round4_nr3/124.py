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
#define maxn 1000000
using namespace std;

bitset<maxn + 5> bs;
vector<int> prime;
int T;
long long n;

int main()
{
    freopen("c.i2","r",stdin);
    freopen("c.o2","w",stdout);
    
    for (int i = 2; i <= maxn; i++) if (!bs[i])
    {
        prime.push_back(i);
        for (int j = i + i; j <= maxn; j += i) bs[j] = 1;
    }
    
    scanf("%d", &T);
    for (int it = 1; it <= T; it++)
    {
        printf("Case #%d: ", it);
        cin >> n;
        cerr << it << endl;
        if (n == 1) printf("0\n"); else
        {
              int diff = 1;
              for (int i = 0; i < prime.size() && 1LL * prime[i] * prime[i] <= n; i++)
              {
                  int deg = 0;  long long x = n;
                  while (x >= prime[i])
                  {
                    deg++;  x /= prime[i];
                  }
                  diff += (deg - 1);
              }
              printf("%d\n", diff);
           }
    }
}

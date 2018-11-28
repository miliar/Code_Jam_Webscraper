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

bool square(string s)
{
    long long x = 0;
    for (int i = 0; i < s.size(); i++) x = x * 2LL + s[i] - '0';
    long long q = (long long) floor(sqrt(1.0 * x));
    return q * q == x;
}

int T,n;
string s;

int main()
{
    freopen("d.i1","r",stdin);
    freopen("d.o1","w",stdout);

    scanf("%d", &T);
    for (int it = 1; it <= T; it++)
    {
        cin >> s;  n = s.size();
        vector<int> ques;
        for (int i = 0; i < n; i++) if (s[i] == '?') ques.push_back(i);
        int sz = ques.size();
        printf("Case #%d: ", it);
        for (int mask = 0; mask < (1 << sz); mask++)
        {
            for (int i = 0; i < sz; i++) if (mask & (1 << i)) s[ques[i]] = '1'; else s[ques[i]] = '0';
            if (square(s))
            {
                cout << s << endl;  break;
            }
        }
    }
}

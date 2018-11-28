#include <vector>
#include <list>
#include <cassert>
#include <map>
#include <queue>
#include <string>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <utility>
#include <sstream>
#include <iostream>
#include <cstdio>
#include <cctype>
#include <cstring>
#include <cmath>
#include <cstdlib>

using namespace std;

typedef pair <int,int> pii;
typedef vector <int> vi;
typedef vector <string> vs;
typedef int ll;
const int INF = 0x3f3f3f3f;

inline int toInt(string& s)
{
    stringstream ss;
    int ret;
    ss << s;
    ss >> ret;
    return ret;
}

inline string toStr(int& i)
{
    stringstream ss;
    ss << i;
    return ss.str();
}

/************************************************************************
******************** Code written during the contest ********************
************************************************************************/

const int MAXN = 10010;
int pos[MAXN], len[MAXN];
int best[MAXN];
int n,d;

void solve()
{
    memset(best, -1, sizeof(best));
    cin >> n;
    for (int i=0; i<n; i++)
        cin >> pos[i] >> len[i];
    cin >> d;

    for (int i=1; i<n; i++)
    {
        if (pos[i] <= 2*pos[0])
            best[i] = 0;
    }
    for (int i=1; i<n; i++)
    {
        for (int end=i+1; end<n; end++)
        {
            if (best[i] != -1 && best[end] == -1)
            {
                if (min(len[i], pos[i]-pos[best[i]])+pos[i] >= pos[end])
                {
                    best[end] = i;
                }
            }
        }
    }
    for (int i=0; i<n; i++)
    {
        if (best[i] != -1 && min(len[i], pos[i]-pos[best[i]])+pos[i] >= d)
        {
            cout << "YES\n";
            return;
        }
    }
    if (pos[0]*2 >= d)
        cout << "YES\n";
    else
        cout << "NO\n";
}

int main()
{
    int t; cin >> t;
    for (int kase=1; kase<=t; kase++)
    {
        cout << "Case #" << kase << ": ";
        solve();
    }
    return 0;
}

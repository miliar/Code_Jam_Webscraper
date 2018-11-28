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
typedef long long ll;
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
const int MAXN = 1001;
int n,w,l;
pii rad[MAXN];
pii place[MAXN];
int p;

int miny(int x, int r)
{
    int ret = 0;
    for (int i=0; i<p; i++)
    {
        if ((x < place[i].first && x+r > place[i].first-rad[i].first) || (x > place[i].first && x-r < place[i].first+rad[i].first))
        {
            ret = max(ret, place[i].second+rad[i].first+r);
        }
    }
    assert(ret <= l);
    return ret;
}

void solve()
{
    cin >> n >> w >> l;
    for (int i=0; i<n; i++) cin >> rad[i].first, rad[i].second = i;
    sort(rad, rad+n);
    int x = p = 0;

    while (p < n)
    {
        bool down = false;
        while (p < n)
        {
            place[p] = make_pair(x,miny(x, rad[p].first));
            x += (down ? -rad[p].first : rad[p].first);
            if (p+1<n)
                x += (down ? -rad[p+1].first : rad[p+1].first);
            p++;

            if (x > w)
            {
                down = true;
                x = w;
            }
            if (x < 0)
            {
                down = false;
                x = 0;
            }
        }
    }
    for (int i=0; i<n; i++)
    {
        for (int j=0; j<n; j++)
        {
            if (rad[j].second == i)
            {
                cout << place[j].first << ' ' << place[j].second << ' ';
                break;
            }
        }
    }
    cout << endl;
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

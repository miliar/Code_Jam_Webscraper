#include <vector>
#include <string>
#include <iostream>
#include <iomanip>
#include <sstream>
#include <cstdlib>
#include <cstdio>
#include <cmath>
#include <ctime>

using namespace std;

int n,m;
vector<vector<pair<int, int> > > cus;
vector<int> make, now;
int ans, cur;

void search(int depth)
{
    if (cur >= ans) return;
    if (depth == n)
    {
        for(int i=0;i<m;++i)
        {
            bool ok = false;
            for (int j=0;j<cus[i].size();++j)
            {
                if (now[cus[i][j].first - 1] == cus[i][j].second)
                {
                    ok = true;
                    break;
                }
            }
            if (!ok) return;
        }
        ans = cur;
        make = now;
        return;
    }
    now[depth] = 0;
    search(depth + 1);
    now[depth] = 1;
    ++cur;
    search(depth + 1);
    --cur;
}

int main(int argc, char **argv)
{
    int NNNNN;
    cin >> NNNNN;
    for (int cccccc=1;cccccc<=NNNNN;++cccccc)
    {
        cout << "Case #" << cccccc << ": ";
        
        // CODE
        cin >> n >> m;
        cus.resize(m);
        for (int i=0;i<m;++i)
        {
            cus[i].clear();
            int t;
            cin >> t;
            for (int j=0;j<t;++j)
            {
                int x, y;
                cin >> x >> y;
                cus[i].push_back(make_pair(x, y));
            }
        }
        make.resize(n);now.resize(n);
        ans = n + 1;
        cur = 0;
        search(0);
        if (ans == n + 1) cout << "IMPOSSIBLE" << endl;
        else
        {
            for (int i=0;i<n;++i)
            {
                cout << make[i] << " ";
            }
            cout << endl;
        }
        // END OF CODE
    }
    return 0;
}
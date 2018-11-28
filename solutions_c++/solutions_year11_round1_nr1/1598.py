#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>

#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <queue>
#include <list>
#include <stack>
#include <map>
#include <set>
using namespace std;
 
#define DEBUG(x) //x
#define REP(i,a) for(int i=0;i<int(a);i++)
#define FOR(i,a,b) for(int i=a;i<int(b);i++)
#define VI vector<int>
#define size(x) int((x).size())
#define all(x) (x).begin(), (x).end()
#define MK(x, y) make_pair(x, y)
#define PB push_back
 
typedef pair<int, int> pii;

int main()
{
    int T;
    cin >> T;
    for (int t = 1; t <= T; t++)
    {
        int n, pd, pg, dpd = 100;
        cin >> n >> pd >> pg;

        for (int i = 2; i < 11 && pd; i++)
        {
            while (pd % i == 0 && dpd % i == 0)
            {
                pd /= i;
                dpd /= i;
            }
        }
        cout << "Case #" << t << ": ";
        if (pd == 0 && pg == 0)
            cout << "Possible" << endl;
        else if (dpd > n)
            cout << "Broken" << endl;
        else
        {
            if (pg == 100 && (pd != 1 || dpd != 1))
                cout << "Broken" << endl;
            else if (pg == 0 && pd != 0)
                cout << "Broken" << endl;
            else
                cout << "Possible" << endl;

        }
    }
    return 0;
}


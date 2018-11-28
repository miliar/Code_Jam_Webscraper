#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <queue>
#include <climits>

using namespace std;

#define MP make_pair
#define FF first
#define SS second
#define SZ size()
#define PB push_back
#define all(x) (x).begin(), (x).end()
#define FORZ(i, n) for(typeof(n) i = 0 ; i !=n ; i++)

typedef long long LL;
typedef pair <int, int> II;
typedef vector <int> VI;

int main()
{
    string Get();
    void unget(string);
    int t;
    cin >> t;
    FORZ(k, t)
    {
        int ns;
        cin >> ns;
        string tmp;
        map <string, int> indexOf;
        getchar();
        FORZ(i, ns)
        {
            getline(cin, tmp, '\n');
            indexOf[tmp] = i;
        }
        map <string, int> :: iterator it;
        int nq, i = 0, ans = 0;
        cin >> nq;
        getchar();
        int jj = -1;
        while(i < nq)
        {
            int j = 0;
            bool check[ns];
            memset (check, false, sizeof(check));
            if(jj != -1)
            {
                check[jj] = true;
                j++;
            }
            while(i < nq && j < ns)
            {
                getline(cin, tmp);
                i++;
                int index = indexOf[tmp];
                if(check[index] == false)
                {
                    check[index] = true;
                    j++;
                    jj = index;
                }
            }
            if(j == ns)
            {
                ans++;
            }
            if(i == nq)
                 break;

        }
        cout << "Case #" << k+1 << ": " << ans << endl;
    }
    return 0;
}

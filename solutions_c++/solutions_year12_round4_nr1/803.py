#include <iostream>
#include <vector>
#include <map>
#include <set>
#include <algorithm>
#include <string>
#include <list>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iomanip>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>
#include <cstdio>

using namespace std;

typedef vector<int> VI;
typedef vector<VI> VVI;
typedef pair<int, int> PII;
typedef long long ll;
#define PB push_back
#define SZ(a) int((a).size())
#define ALL(c) (c).begin(), (c).end()
#define TR(c, i) for(typeof((c).begin()) i = (c).begin(); i != (c).end(); i++)
#define present(c,x) ((c).find(x) != (c).end())
#define cpresent(c,x) (find(ALL(c),x) != (c).end())
#define debug(var) cout<<#var<<"="<<(var)<<endl

#define MAXN 10002
int MAXDIS = (int)10e9;

void func()
{
    int n;
    int ds[MAXN], len[MAXN], result[MAXN];
    cin >> n;
    ds[0] = len[0] = 0;
    for(int i = 1; i <= n; i++) {
        cin >> ds[i] >> len[i];
    }
    int dis;
    cin >> dis;   
    ds[n + 1] = dis;
    for(int i = 0; i < n + 2; i++) {
        result[i] = MAXDIS;
    }
    result[1] = 0;
    for(int i = 1; i <= n + 1; i++) {
        for(int j = i + 1; j <= n + 1; j++) {
            
            if(ds[i] - result[i] + ds[i] >= ds[j])
            {
                result[j] = min(result[j], max(ds[j] - len[j], ds[i]));
            }
            else break;
        }
    }
    
    if(result[n + 1] < MAXDIS) cout << "YES" << endl;
    else cout << "NO" << endl;
}

int main()
{
    int t;
    freopen("A-small-attempt0.in", "r", stdin);
    //freopen("A-large.in", "r", stdin);
    freopen("A-out.txt", "w", stdout);
    cin >> t;
    for(int ti = 1; ti <= t; ti++)
    {
        cout << "Case #" << ti << ": ";
        func();
    }
}
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

#define SZ(a) (int)(a).size()
#define PB push_back
#define ALL(a) (a).begin(),(a).end()
#define INF (int)1e9
#define vi vector<int>
#define vs vector<string>

using namespace std;

int main()
{
    int T;
    cin >> T;

    for(int t = 0; t < T; t++)
    {
        int N;
        cin >> N;

        long long small = 10e6 + 1, tot = 0, ans = 0, num;
        for(int i = 0; i < N; i++)
        {
            cin >> num;
            small = min(small, num);
            ans += num;
            tot ^= num;
        }

        cout << "Case #" << t + 1 << ": "; 
        if(tot == 0)
            cout << ans - small;
        else
            cout << "NO";
        cout << endl;
        
    }
    return 0;
}

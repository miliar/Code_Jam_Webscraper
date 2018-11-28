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

bool check(vi &notes, int n)
{
    for(int i = 0; i < SZ(notes); i++)
        if(notes[i] % n == 0 || n % notes[i] == 0)
            continue;
        else
            return false;
    return true;
}

int main()
{
    int T;
    cin >> T;
    
    for(int t = 0; t < T; t++)
    {
        int N, L, H;
        cin >> N >> L >> H;
        
        vi notes(N);
        for(int i = 0; i < N; i++)
            cin >> notes[i];
            
        int ans = L, poss = false;
        while(ans <= H)
        {
            poss = check(notes, ans);
            if(poss)
                break;
            ans++;
        }
        
        cout << "Case #" << t + 1 << ": ";
        if(ans > H)
            cout << "NO" << endl;
        else 
            cout << ans << endl;
        
    }
    return 0;
}

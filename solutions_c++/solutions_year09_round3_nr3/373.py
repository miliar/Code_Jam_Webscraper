#include <iostream>
#include <string>
#include <vector>
#include <set>
#include <queue>
#include <ctime>
#include <map>
#include <set>
#include <cstdio>
#include <algorithm>
#include <cmath>
#include <cassert>
using namespace std;
int dp[10001][10001];
char v[10001][10001];
set<int> st;
int Cnt = 1;
int solve(int a, int b)
{
    if(a >= b)
        return 0; 
    int& ref = dp[a][b];
    if(v[a][b] == Cnt)
        return ref;
    v[a][b] = Cnt;
    set<int>::iterator itr1 = st.lower_bound(a);
    bool f = 0;
    int mn = 1e9;
    for(; itr1 != st.end() && *itr1 <= b; ++itr1)
    {
        f = 1;
        int x = *itr1;
        mn = min(mn, solve(a, x - 1) + solve(x + 1, b));
    }

    if(f == 0)
        return ref = 0;
    return ref = mn + b - a;
}

int main()
{
    int kaseno, kases;
    for(scanf("%d",&kases), kaseno = 1; kaseno <= kases; ++kaseno)
    {
        int L;
        int P , Q;
        scanf("%d%d",&P,&Q);
        st.clear();
        while(Q--)
        {
            int a;
            scanf("%d",&a);
            st.insert(a);
        }
        Cnt++;
        printf("Case #%d: %d\n", kaseno, solve(1, P));
        
    }
}

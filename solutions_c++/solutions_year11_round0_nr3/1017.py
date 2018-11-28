#include <cstdio>
#include <cstdlib>
#include <iostream>
using namespace std;

const int maxc = 1000100;

void solve(int k)
{
    int result = 0;

    int min = maxc;
    int sum = 0;
    int n; cin >> n;
    for(int i=0;i<n;i++)
    {
        int c; cin >> c;
        if(c < min)
            min = c;
        sum += c;
        result ^= c;
    }

    if(result == 0)
        printf("Case #%d: %d\n", k, sum-min);
    else
        printf("Case #%d: NO\n", k);
}

int main()
{
    int t; cin >> t;
    for(int i=0;i<t;i++)
        solve(i+1);
    return 0;
}

#include <algorithm>
#include <iostream>
#include <cstring>
#include <cstdlib>
#include <cstdio>
#include <vector>
#include <string>
using namespace std;

int main()
{
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    int TestCase;
    cin >> TestCase;
    for(int CaseID = 1; CaseID <= TestCase; CaseID ++)
    {
        int n, sp, want;
        cin >> n >> sp >> want;
        int free = 2 * (want - 1) + want;
        int able = 2 * (want - 2) + want;
        int ans = 0;
        for(int i = 1; i <= n; i++)
        {
            int t;
            cin >> t;
            if(t < want)
                continue;
            if(t >= free)
                ans ++;
            else if(t >= able && sp > 0)
            {
                sp --;
                ans ++;
            }
        }
        cout << "Case #" << CaseID << ": " << ans << endl;
    }
    return 0;
}

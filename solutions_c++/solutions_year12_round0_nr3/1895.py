#include <algorithm>
#include <iostream>
#include <cstring>
#include <cstdlib>
#include <cstdio>
#include <string>
#include <map>
using namespace std;

map <int, bool> alreadyHave;
int A, B, n;

int len(int x)
{
    return x == 0 ? 0 : (len(x/10) + 1);
}

int digit[11];

int solve(int x)
{

    int t = x;
    for(int i = 0; i < n; i++)
    {
        digit[i] = t % 10;
        t /= 10;
    }
    alreadyHave.clear();
    int ret = 0;
    for(int start = 0; start < n; start ++)
    {
        int b = 0;
        for(int i = 0; i < n; i++)
            b = 10 * b + digit[(start-i + n) % n];
        if(b > x && b <= B)
        {
            if(!alreadyHave.count(b))
            {
                alreadyHave[b] = true;
                ret ++;
            }
        }
    }
    return ret;
}

int main()
{
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    int TestCase;
    cin >> TestCase;
    for(int CaseID = 1; CaseID <= TestCase; CaseID ++)
    {
        cin >> A >> B;
        n = len(A);
        long long ans = 0;
        for(int i = A; i <= B; i++)
            ans += solve(i);
        cout << "Case #" << CaseID << ": " << ans << endl;
    }
    return 0;
}

#include<algorithm>
#include<iomanip>
#include<iostream>
#include<vector>
#include<string>
using namespace std;

bool isprime[1000011];

void solve()
{
    long long n;
    cin >> n;
    long long ans = (n > 1);
    for(long long i = 2 ; i * i <= n ; i++)
        if(isprime[i])
        {
            long long t = i , u = 0;
            while(t <= n)
                u ++ , t *= i;
            ans += u - 1;
        }
    cout << ans << endl;
}

int main()
{
    freopen("in.txt" , "r" , stdin);
    freopen("out.txt" , "w" , stdout);
    memset(isprime , true , sizeof(isprime));
    for(int i = 2 ; i <= 1000010 ; i++)
        if(isprime[i])
            for(int j = i + i ; j <= 1000010 ; j += i)
                isprime[j] = false;
    int TestCase;
    cin >> TestCase;
    for(int CaseID = 1 ; CaseID <= TestCase ; CaseID ++)
    {
        cout << "Case #" << CaseID << ": ";
        solve();
    }
    return 0;
}

#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <queue>
#include <algorithm>
#include <vector>
#include <stack>
#include <set>
using namespace std;

long long int finddivisor(long long int n)
{
    int x = 2;
    while(n%x != 0)
    {
        x++;
        if(x * x > n)
            return n;
    }

    return x;
}

void solve(int k)
{
    int n, l, h; cin >> n >> l >> h;
    vector<int> v;
    for(int i=0;i<n;i++)
    {
        int tmp; cin >> tmp;
        v.push_back(tmp);
    }

    int res = -1;
    for(int i=l;i<=h;i++)
    {
        bool good = true;
        for(int j=0;j<v.size();j++)
        {
            if(i%v[j] != 0 && v[j]%i != 0)
            {
                good = false;
                break;
            }
        }
        if(good) {
            res = i;
            break;
        }
    }

    if(res != -1)
    {
        printf("Case #%d: ", k);
        cout << res << '\n';
    }
    else
        printf("Case #%d: NO\n", k);
}

int main()
{
    int n; cin >> n;
    for(int i=0;i<n;i++)
    {
        solve(i+1);
    }
    return 0;
}


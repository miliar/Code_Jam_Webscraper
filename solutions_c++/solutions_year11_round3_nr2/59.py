#include<iostream>
#include<map>
#include<math.h>
#include<vector>
#include<string>
#include<algorithm>
using namespace std;
typedef long long ll;
typedef vector<int>::iterator iv;
typedef map<string,int>::iterator im;

ll a[1000000];

bool cmp(ll q, ll w)
{
    return q > w;
}

int main()
{
    freopen("B-large.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    ll c=1, tt, n, m, i, j, t;
    ll L, ans;
    cin >> tt;
    while(tt--)
    {
        ans = 0;
        cin >> L >> t >> n >> m;
        for(i=0; i<m; i++)
            scanf("%I64d", &a[i]);
        for(i=m; i<n; i++)
            a[i] = a[i % m];
        for(i=0; i<n; i++)
        {
            ans += a[i] * 2;
            if(ans > t)
            {
                a[i] = (ans - t) / 2;
                ans = t;
                break;
            }
        }
        sort(a+i, a+n, cmp);
        for(j=0; j<L && i<n; j++, i++)
            ans += a[i];
        for(; i<n; i++)
            ans += a[i]*2;
        printf("Case #%I64d: %I64d\n", c++, ans);
    }
}

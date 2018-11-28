#include<iostream>
#include<cstdio>

using namespace std;

typedef long long ll;

ll l, t, n, c;
ll e[1000001];
ll s[1000001];

int main()
{
    freopen("B-large.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    int T;
    cin >> T;
    for(int Ti = 1; Ti <= T; ++Ti)
    {
        cin >> l >> t >> n >> c;
        for(int i = 0; i < c; ++i)
            cin >> e[i];
        for(int i = c; i < n; ++i)
            e[i] = e[i%c];
        
        ll sum = 0, lsum = 0;
        for(int i = 0; i < n; ++i)
        {
            lsum = sum;
            sum += e[i] *= 2;
            if     (sum <= t)
                s[i] = 0;
            else if(lsum < t && t < sum)
                s[i] = -(sum - t) / 2;
            else if(t <= lsum)
                s[i] = -e[i] / 2;
        }
        sort(s, s+n);
        
        ll sol = sum;
        for(int i = 0; i < l && i < n; ++i)
            sol += s[i];
        cout << "Case #" << Ti << ": " << sol << endl;
    }
    return 0;
}

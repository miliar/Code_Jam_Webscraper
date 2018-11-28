#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int gcd(int x, int y)
{
    if(!x)
        return y;
    if(!y)
        return x;

    int t;
    if(x > y)
    {
        t = x;
        x = y;
        y = t;
    }
    while(true)
    {
        t = y % x;
        if(!t)
            break;
        y = x;
        x = t;
    }
    return x;
}




int main()
{
    int C;
    cin >> C;
    for(int c = 0; c < C; c++)
    {
        int N;
        cin >> N;
        vector<int> v;
        for(int n = 0; n < N; n++)
        {
            int t;
            cin >> t;
            v.push_back(t);
        }
        sort(v.begin(), v.end());
        int g = v[1] - v[0];
        for(int n = 1; n < N - 1; n++)
            g = gcd(g, v[n+1] - v[n]);
        int ans;
        if( !(v[0] % g))
            ans = 0;
        else
            ans = g - v[0] % g;
        cout << "Case #" << c + 1 << ": " << ans << endl;
    }
    return 0;
}

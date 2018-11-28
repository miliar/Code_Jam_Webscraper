#include <iostream>
#include <cmath>
using namespace std;
const int maxn = 107;
int n;
int r[maxn];
int p[maxn];
int ai[2][maxn];
int cnt[2];
void init()
{
    cnt[0] = cnt[1] = 0;
    cin >> n;
    for (int i=0; i<n; i++)
    {
        char c[10];
        cin >> c;
        r[i] = c[0]=='O'?1:0;
        cin >> p[i]; 
        ai[r[i]][cnt[r[i]]++] = p[i];
    }
    
}
int calc()
{
    int t = 0;
    int i = 0;
    int now[2] = {0, 0};
    int pp[2] = {1, 1};
    while (now[0] < cnt[0] || now[1] < cnt[1])
    {
        int next_i = i;
        for (int k=0; k<2; k++)
        {
            if (r[i] == k && pp[k] == p[i])
            {
                now[k]++;
                next_i++;
                // t++;
                continue;
            }            
            int d = ai[k][now[k]] - pp[k];
            if (d != 0)
            {
                int sign = d / abs(d);
                // cout << "ai: " << sign << ' ' << d << ' ' << abs(d) << endl;
                pp[k] += sign;
            }
        }
        for (int k=0; k<2; k++)
        {

        }
        t++;
        i = next_i;
        // cout << t << ' ' << pp[0] << ' ' << pp[1] << endl;
        // cout << now[0] << ' ' << cnt[0] << ' ' << now[1] << ' ' << cnt[1] << endl;
    }

    // cout << t << endl;
    return t;
}   
int main()
{
    int T;
    cin >> T;
    for (int t=1; t<=T; t++)
    {
        init();
        int ans = calc();
        cout << "Case #" << t << ": " << ans << endl;
    }
    return 0;
}

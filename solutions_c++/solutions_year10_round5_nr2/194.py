#include <iostream>
#include <algorithm>
using namespace std;
#define tiao system("pause")

bool f[111111];
long long g[111111];
int t;
long long l;
int n;
int a[111];
int up = 111111;

int main(void)
{
    int i,j,k,ci,cici,cicici;
    
    freopen("B-small-attempt0.in","r",stdin);
    freopen("B-small-attempt0.out","w",stdout);
    
    cin >> t;
    for (cicici=1; cicici<=t; cicici++)
    {
        cin >> l >> n;
        for (i=1; i<=n; i++) cin >> a[i];
        
        sort(a+1, a+1+n);
        memset(f, 0, sizeof(f));
        fill(g+0, g+up, 1234567890234LL);
        
        f[0] = true; 
        g[0] = 0;
        
        for (i=1; i<=n; i++)
            for (j=0; j+a[i]<up; j++)
            {
                if (f[j]) 
                {
                    f[j+a[i]] = true;
                    if (g[j] + 1 < g[j+a[i]]) g[j+a[i]] = g[j] + 1;
                }
                            
            }
        
        long long ans = 0;
        if (l < up) 
        {
            if (!f[l]) cout << "Case #" << cicici << ": IMPOSSIBLE\n";
            else cout << "Case #" << cicici << ": " << g[l] << "\n";
        }
        else
        {
            long long cb = (l - up) / a[n] + 1;
            ans = cb;
            l -= cb * a[n];
            if (!f[l]) cout << "Case #" << cicici << ": IMPOSSIBLE\n";
            else cout << "Case #" << cicici << ": " << g[l] + ans << "\n";
        }
    }
//    tiao;
    return 0;
}

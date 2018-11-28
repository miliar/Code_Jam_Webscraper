#include <iostream>
#include <fstream>
#include <cstdio>
#include <cstdlib>
#include <set>

using namespace std;

int main()
{
    freopen("ss.in", "r", stdin);
    freopen("ss.out", "w", stdout);
    int t, l;
    cin >> t;
    for (l=0; l<t; l++)
    {
        int n, s, p, ans=0;;
        int a[300], i;
        cin >> n >> s >> p;
        for (i=0; i<n; i++)
        cin >> a[i];
        for (i=0; i<n; i++)
        {
            int x=a[i]/3;
            if (x>=p) 
            {
                ans++;
                continue;
            }
            int y=a[i]%3;
            if (y==1) 
                if (x+1>=p) 
                {
                    ans++;
                    continue;
                }
            if (y==2)
            {
                if (x+1>=p)
                {
                    ans++;
                    continue;
                }
                if (x+2>=p && s>0 && x>0)
                {
                    ans++;
                    s--;
                }
                continue;
            }
            if (y==0)
            {
                if (x+1>=p && s>0 && x>0)
                {
                    ans++;
                    s--;
                }
                continue;
            }
        }
        cout << "Case #" << l+1 << ": " << ans << endl;
    }
}

#include <iostream>
#include <cstring>
#include <string>

using namespace std;

int T;

int max(int a, int b)
{
    return (a > b) ? a : b;
}

int min(int a, int b)
{
    return (a < b) ? a : b; 
}

int main()
{
   // freopen("B-small.in", "r", stdin);
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);
    
    int n;
    int t[1000], a[1000][2];
    int f[200][200];
    int p, s;
    
    cin >> T;
    
    for (int tt = 1; tt <= T; ++tt)
    {
        cin >> n;
        cin >> s;
        cin >> p;
        for (int i = 0; i < n; ++i)
        {
            cin >> t[i];
            a[i][0] = a[i][1] = 0;
            if (t[i] > 0)
            {
            //not suprising
                if (t[i] % 3 == 0) a[i][0] = max(a[i][0], t[i] / 3);
                if ((t[i] + 1) % 3 == 0) a[i][0] = max(a[i][0], (t[i] + 1) / 3);
                if ((t[i] - 1) % 3 == 0) a[i][0] = max(a[i][0], (t[i] - 1) / 3 + 1);
            }
            if (a[i][0] >= p) a[i][0] = 1; else a[i][0] = 0;
            if (t[i] > 0) {
            //not suprising
                if (t[i] % 3 == 0) a[i][1] = max(a[i][1], t[i] / 3 + 1);
                if ((t[i] + 2) % 3 == 0) a[i][1] = max(a[i][1], (t[i] + 2) / 3);
                if ((t[i] - 2) % 3 == 0) a[i][1] = max(a[i][1], (t[i] - 2) / 3 + 2);
            } 
            if (a[i][1] >= p) a[i][1] = 1; else a[i][1] = 0;
        //    printf("%d %d\n", a[i][0], a[i][1]);
        }
        
        memset(f, 0, sizeof(f));
        for (int i = 1; i <= n; ++i)
            for (int j = 0; j <= min(i, s); ++j)
                if (j == 0)
                    f[i][j] = f[i - 1][j] + a[i - 1][0];
                else
                    f[i][j] = max(f[i - 1][j] + a[i - 1][0], f[i - 1][j - 1] + a[i - 1][1]);
        
        cout << "Case #" << tt << ": " << f[n][s] << endl;
    }
    
    return 0;
}

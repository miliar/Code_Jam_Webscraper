#include <iostream>
using namespace std;
const int MAXN = 100,MAXLEN = 500;
long long f[MAXLEN+1][20];
int main()
{
    freopen("C-small-attempt000.in","r",stdin);
    freopen("C-small-attempt000.out","w",stdout);
    int n;
    long long ans;
    string s;
    cin >> n;
    getchar();
    for (int k = 0;k < n;k++)
    {
        memset(f,0,sizeof(f));
        getline(cin,s);
        ans = 0;
        int m = s.size();
        for (int i = 0;i < m;i++)
        {
            if (s[i] == 'w')
            {
                f[i][0] = 1;
                continue;
            }
            if (s[i] == 'e')
            {
                for (int j = 0;j < i;j++)
                {
                    f[i][1] = (f[i][1] + f[j][0] - 1) % 1000 + 1;
                    f[i][6] = (f[i][6] + f[j][5] - 1) % 1000 + 1;
                    f[i][14] = (f[i][14] + f[j][13] - 1) % 1000 + 1;
                }
                continue;
            }
            if (s[i] == 'l')
            {
                for (int j = 0;j < i;j++)
                    f[i][2] = (f[i][2] + f[j][1] - 1) % 1000 + 1;
                continue;
            }
            if (s[i] == 'c')
            {
                for (int j = 0;j < i;j++)
                {
                    f[i][3] = (f[i][3] + f[j][2] - 1) % 1000 + 1;
                    f[i][11] = (f[i][11] + f[j][10] - 1) % 1000 + 1;
                }
                continue;
            }
            if (s[i] == 'o')
            {
                for (int j = 0;j < i;j++)
                {
                    f[i][4] = (f[i][4] + f[j][3] - 1) % 1000 + 1;
                    f[i][9] = (f[i][9] + f[j][8] - 1) % 1000 + 1;
                    f[i][12] = (f[i][12] + f[j][11] - 1) % 1000 + 1;
                }
                continue;
            }
            if (s[i] == 'm')
            {
                for (int j = 0;j < i;j++)
                {
                    f[i][5] = (f[i][5] + f[j][4] - 1) % 1000 + 1;;
                    f[i][18] = (f[i][18] + f[j][17] - 1) % 1000 + 1;;
                }
                continue;
            }
            if (s[i] == ' ')
            {
                for (int j = 0;j < i;j++)
                {
                    f[i][7] = (f[i][7] + f[j][6] - 1) % 1000 + 1;;
                    f[i][10] = (f[i][10] + f[j][9] - 1) % 1000 + 1;;
                    f[i][15] = (f[i][15] + f[j][14] - 1) % 1000 + 1;;
                }
                continue;
            }
            if (s[i] == 't')
            {
                for (int j = 0;j < i;j++)
                    f[i][8] = (f[i][8] + f[j][7] - 1) % 1000 + 1;
                continue;
            }
            if (s[i] == 'd')
            {
                for (int j = 0;j < i;j++)
                    f[i][13] = (f[i][13] + f[j][12] - 1) % 1000 + 1;;
                continue;
            }
            if (s[i] == 'j')
            {
                for (int j = 0;j < i;j++)
                    f[i][16] = (f[i][16] + f[j][15] - 1) % 1000 + 1;;
                continue;
            }
            if (s[i] == 'a')
            {
                for (int j = 0;j < i;j++)
                    f[i][17] = (f[i][17] + f[j][16] - 1) % 1000 + 1;;
                continue;
            }
        }
        for (int i = 0;i < m;i++)
        {
            ans += f[i][18];
            ans = (ans - 1) % 1000 + 1;
        }
        cout << "Case #" << k + 1 << ": ";
        if (ans < 1000) cout << '0';
        if (ans < 100) cout << '0';
        if (ans < 10) cout << '0';
        cout << ans << endl;
    }
}

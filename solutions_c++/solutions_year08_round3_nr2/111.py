#include <iostream>
#include <fstream>
using namespace std;

const int MaxN = 50;
const int mod = 2 * 3 * 5 * 7;

char num[MaxN];
int len;
int g[MaxN][MaxN];
long long f[MaxN][mod];

int cal(int start, int end)
{
    int ret = 0;
    for (int i = start; i <= end; i++)
    {
        ret = ret * 10 + num[i] - '0';
        ret %= mod;
    }
    return ret;
}

void init()
{
    for (int i = 0; i < len; i++) {
        for (int j = i; j < len; j++) {
            g[i][j] = cal(i, j);
            //cout << g[i][j] << " ";
        }
        //cout << endl;
    }
}

bool isUgly(int v)
{
    return v % 2 == 0 || v % 3 == 0 || v % 5 == 0 || v % 7 ==0;
}

long long run()
{
    len = strlen(num);
    init();
    for (int i = 0; i <= len; i++)
        for (int j = 0; j < mod; j++) f[i][j] = 0;
    f[0][0] = 1;

    for (int i = 0; i < len; i++)
    {
        for (int j = 0; j <= i; j++)
        {
            int v = g[j][i];
            for (int m = 0; m < mod; m++)
            {
                int p1 = (m + v) % mod;
                f[i+1][p1] += f[j][m];
                
                if (j > 0)
                {
                    int p2 = (m - v + mod) % mod;
                    f[i+1][p2] += f[j][m];
                }
            }
        }
    }
    long long ans = 0;
    for (int m = 0; m < mod; m++) {
        if (isUgly(m)) ans += f[len][m];
    }
    return ans;
}

int main()
{
    int n;
    cin >> n;
    ofstream output("d:\\output.txt");
    
    for (int i = 0; i < n; i++)
    {
        cin >> num;
        long long ans = run();
        cout << "Case #" << i + 1 << ": " << ans << endl;
        output << "Case #" << i + 1 << ": " << ans << endl;
    }
    output.flush();
    return 0;
}

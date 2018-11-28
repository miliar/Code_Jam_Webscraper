#include<algorithm>
#include<iomanip>
#include<iostream>
#include<vector>
#include<string>
using namespace std;

int n , m;
long long int Omass[501][501];
long long int mass[501][501];
long long int Xmass[501][501];
long long int Ymass[501][501];

bool check(int x , int y , int r)
{
    int x2 = x + r - 1, y2 = y + r - 1;
    int M = mass[x2][y2] - mass[x-1][y2] - mass[x2][y-1] + mass[x-1][y-1];
    int XM = Xmass[x2][y2] - Xmass[x-1][y2] - Xmass[x2][y-1] + Xmass[x-1][y-1];
    int YM = Ymass[x2][y2] - Ymass[x-1][y2] - Ymass[x2][y-1] + Ymass[x-1][y-1];
    
    M -= Omass[x][y] , XM -= Omass[x][y] * x , YM -= Omass[x][y] * y;
    M -= Omass[x][y2] , XM -= Omass[x][y2] * x , YM -= Omass[x][y2] * y2;
    M -= Omass[x2][y] , XM -= Omass[x2][y] * x2 , YM -= Omass[x2][y] * y;
    M -= Omass[x2][y2] , XM -= Omass[x2][y2] * x2 , YM -= Omass[x2][y2] * y2;
    
    long long int want2XM = M * (x + x2);
    long long int want2YM = M * (y + y2);

    if(XM * 2 == want2XM)
        if(YM * 2 == want2YM)
            return true;
    return false;
}

void solve()
{
    memset(mass , 0 , sizeof(mass));
    memset(Xmass , 0 , sizeof(Xmass));
    memset(Ymass , 0 , sizeof(Ymass));
    int M;
    cin >> n >> m >> M;
    for(int i = 1 ; i <= n ; i++)
    {
        string s;
        cin >> s;
        s = " " + s;
        for(int j = 1 ; j <= m ; j++)
            mass[i][j] = s[j] - '0' , Omass[i][j] = mass[i][j];
    }
    for(int i = 1 ; i <= n ; i++)
        for(int j = 1 ; j <= m ; j++)
        {
            Xmass[i][j] = mass[i][j] * i , Ymass[i][j] = mass[i][j] * j;
            mass[i][j] += mass[i-1][j] + mass[i][j-1] - mass[i-1][j-1];
            Xmass[i][j] += Xmass[i-1][j] + Xmass[i][j-1] - Xmass[i-1][j-1];
            Ymass[i][j] += Ymass[i-1][j] + Ymass[i][j-1] - Ymass[i-1][j-1];
        }
    int ans = 0;
    for(int i = 1 ; i <= n ; i++)
        for(int j = 1 ; j <= m ; j ++)
            for(int r = ans + 1 ; r <= min(n - i + 1 , m - j + 1) ; r ++)
                if(check(i , j , r))
                    ans = r;
    if(ans >= 3)
        cout << ans << endl;
    else
        cout << "IMPOSSIBLE" << endl;
}

int main()
{
    freopen("in.txt" , "r" , stdin);
    freopen("out.txt" , "w" , stdout);

    int TestCase;
    cin >> TestCase;
    for(int CaseID = 1 ; CaseID <= TestCase ; CaseID ++)
    {
        cout << "Case #" << CaseID << ": ";
        solve();
    }
    return 0;
}

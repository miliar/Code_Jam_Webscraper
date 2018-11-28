#include<cstdio>
#include<sstream>
#include<cstdlib>
#include<cctype>
#include<cmath>
#include<algorithm>
#include<set>
#include<queue>
#include<stack>
#include<list>
#include<iostream>
#include<fstream>
#include<numeric>
#include<string>
#include<vector>
#include<cstring>
#include<map>
#include<iterator>

#define SQR(x) ((x)*(x))
#define LL long long int
#define LLU long long unsigned
#define pb push_back
#define pp pop_back
#define MP make_pair
#define sz size()
#define VI vector<int>
#define QI queue<int>
#define SI stack<int>
#define ff first
#define ss second
#define MII map<int, int>
#define SD(a) scanf("%d", &a)
#define SD2(a, b) scanf("%d %d", &a, &b)
#define NL puts("")
#define CLR(a) memset(a, 0, sizeof(a))
#define SET(a) memset(a, -1, sizeof(a))
#define rep(i, init, n) for(i=init; i<n; i++)
#define repv(i, init, n) for(i=init; i>n; i--)
#define rep1(i, init, n) for(i=init; i<=n; i++)
#define repv1(i, init, n) for(i=init; i>=n; i--)
#define READ(f) freopen(f, "r", stdin)
#define WRITE(f) freopen(f, "w", stdout)

#define MAXN 10010
#define EPS 1e-9
#define INF 2147483647
#define MOD 747474747
#define pi acos(-1.0)
using namespace std;

char arr[4][4];
bool rowX(int i)
{
    if(arr[i][0]=='X' && arr[i][1]=='X' && arr[i][2]=='X' && (arr[i][3]=='X' || arr[i][3]=='T')) return 1;
    if(arr[i][0]=='T' && arr[i][1]=='X' && arr[i][2]=='X' && arr[i][3]=='X') return 1;
    return 0;
}
bool columnX(int i)
{
    if(arr[0][i]=='X' && arr[1][i]=='X' && arr[2][i]=='X' && (arr[3][i]=='X' || arr[3][i]=='T')) return 1;
    if(arr[0][i]=='T' && arr[1][i]=='X' && arr[2][i]=='X' && arr[3][i]=='X') return 1;
    return 0;
}
bool diagonalX()
{
    if(arr[0][0]=='X' && arr[1][1]=='X' && arr[2][2]=='X' && (arr[3][3]=='X' || arr[3][3]=='T')) return 1;
    if(arr[0][0]=='T' && arr[1][1]=='X' && arr[2][2]=='X' && arr[3][3]=='X') return 1;
    if(arr[0][3]=='X' && arr[1][2]=='X' && arr[2][1]=='X' && (arr[3][0]=='X' || arr[3][0]=='T')) return 1;
    if(arr[0][3]=='T' && arr[1][2]=='X' && arr[2][1]=='X' && arr[3][0]=='X') return 1;
    return 0;
}
bool rowO(int i)
{
    if(arr[i][0]=='O' && arr[i][1]=='O' && arr[i][2]=='O' && (arr[i][3]=='O' || arr[i][3]=='T')) return 1;
    if(arr[i][0]=='T' && arr[i][1]=='O' && arr[i][2]=='O' && arr[i][3]=='O') return 1;
    return 0;
}
bool columnO(int i)
{
    if(arr[0][i]=='O' && arr[1][i]=='O' && arr[2][i]=='O' && (arr[3][i]=='O' || arr[3][i]=='T')) return 1;
    if(arr[0][i]=='T' && arr[1][i]=='O' && arr[2][i]=='O' && arr[3][i]=='O') return 1;
    return 0;
}
bool diagonalO()
{
    if(arr[0][0]=='O' && arr[1][1]=='O' && arr[2][2]=='O' && (arr[3][3]=='O' || arr[3][3]=='T'))    return 1;
    if(arr[0][0]=='T' && arr[1][1]=='O' && arr[2][2]=='O' && arr[3][3]=='O') return 1;
    if(arr[0][3]=='O' && arr[1][2]=='O' && arr[2][1]=='O' && (arr[3][0]=='O' || arr[3][0]=='T')) return 1;
    if(arr[0][3]=='T' && arr[1][2]=='O' && arr[2][1]=='O' && arr[3][0]=='O') return 1;
    return 0;
}
int main()
{
    READ("A-small-attempt0.in");
    WRITE("output.txt");
    int ncase, tcase, i, j, flag;
    SD(ncase);
    rep1(tcase, 1, ncase)
    {
        rep(i, 0, 4) scanf("%s", arr[i]);
        printf("Case #%d: ", tcase);
        flag=0;
        rep(i, 0, 4)
        {
            if(rowX(i) || columnX(i) || diagonalX())
            {
                flag=1;
                break;
            }
            if(rowO(i) || columnO(i) || diagonalO())
            {
                flag=2;
                break;
            }
        }
        if(flag==1) printf("X won\n");
        else if(flag==2) printf("O won\n");
        else
        {
            rep(i, 0, 4)
            {
                rep(j, 0, 4)
                {
                    if(arr[i][j]=='.') break;
                }
                if(j!=4) break;
            }
            if(i==4) printf("Draw\n");
            else printf("Game has not completed\n");
        }
    }
    return 0;
}

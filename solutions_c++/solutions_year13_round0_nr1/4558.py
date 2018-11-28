/******************************
*	Sanad Saha                *
*	University of Dhaka       *
******************************/


#include<set>
#include<map>
#include<list>
#include<cmath>
#include<stack>
#include<queue>
#include<deque>
#include<bitset>
#include<cctype>
#include<cstdio>
#include<string>
#include<vector>
#include<sstream>
#include<fstream>
#include<cstring>
#include<cstdlib>
#include<iostream>
#include<algorithm>

#define EPS 1e-9
#define fi first
#define se second
#define MAX 100005
#define ins insert
#define pb push_back
#define mp make_pair
#define pi acos(-1.0)
#define mod 100000007
#define inf 1<<25
#define ll long long int
#define llu long long unsigned

#define sz(a) ((int)a.size())
#define gcd(a,b)    __gcd(a,b)
#define lcm(a,b) ((a)*((b)/gcd(a,b)))
#define FOR(i, n) for(i=0; i<n; i++)
#define FOR1(i, n) for(i=1; i<=n; i++)
#define mem(a) memset(a, 0, sizeof(a))
#define _set(a) memset(a,-1,sizeof(a))
#define all(a) sort(a.begin(), a.end())
#define FORI(i, a, b) for(i=a; i>=b; i--)
#define FORab(i, a, b) for(i=a; i<=b; i++)
#define popcount(n) __builtin_popcount(n)
#define popcountl(n) __builtin_popcountll(n)
#define foreach(i,n) for(__typeof((n).begin())i =(n).begin();i!=(n).end();i++)

//If Long Long (mask & (1LL << k))
#define check(mask, k) (mask & (1 << k))
#define set1(mask, k) (mask | (1 << k))
#define set0(mask ,k) (mask & (~(1<<k)))

#define SD(a) scanf("%d",&a)
#define SLF(a) scanf("%lf",&a)
#define SC(a) scanf("%c",&a)
#define SS(a) scanf("%s",a)
#define SLLD(a) scanf("%lld", &a)
#define SLLU(a) scanf("%llu", &a)
#define Si64(a) scanf("%I64d", &a)

#define READ(f) freopen(f, "r", stdin)
#define WRITE(f) freopen(f, "w", stdout)

using namespace std;

typedef pair <int, int> pii;
typedef vector <int> vi;
typedef vector <vi> vvi;
typedef map<string , int> msi;
typedef map<int , int> mii;
typedef map<int, string> mis;
typedef set<int> si;
typedef set<string> ss;

//int dx[] = {0,0,1,-1};
//int dy[] = {1,-1,0,0};
//int dx[] = {-1,-1,-1,0,0,1,1,1};
//int dy[] = {-1,0,1,-1,1,-1,0,1};

int main()
{
    READ("A-large.txt");
    WRITE("output.txt");
    string str[5];
    bool X_win, O_win, Dot;
    int t, tcase, o, x, i, j;
    SD(tcase);
    FOR(t, tcase)
    {
        X_win = O_win = Dot = false;
        FOR(i, 4)
        cin >> str[i];

        FOR(i, 4)
        {
            x = o = 0;
            FOR(j, 4)
            {
                if(str[i][j] == '.')
                {
                    Dot = true;
                }
                else if(str[i][j] == 'X')
                {
                    x ++;
                }
                else if(str[i][j] == 'T')
                {
                    x++;
                    o++;
                }
                else if(str[i][j] == 'O')
                {
                    o++;
                }
            }
            if(x == 4)X_win = true;
            else if(o == 4)O_win = true;
        }
        if(!X_win && !O_win)
        {
            FOR(i, 4)
            {
                x = o = 0;
                FOR(j, 4)
                {
                    if(str[j][i] == '.')
                    {
                        Dot = true;
                    }
                    else if(str[j][i] == 'X')
                    {
                        x ++;
                    }
                    else if(str[j][i] == 'T')
                    {
                        x++;
                        o++;
                    }
                    else if(str[j][i] == 'O')
                    {
                        o++;
                    }
                }
                if(x == 4)X_win = true;
                else if(o == 4)O_win = true;
            }
        }
        if(!X_win && !O_win)
        {
            x = o = 0;
            FOR(i, 4)
            {
                if(str[i][i] =='X')x++;
                else if(str[i][i] == 'O')o++;
                else if(str[i][i] == 'T')
                {
                    x++;
                    o++;
                }
            }
            if(x == 4)X_win = true;
            else if(o == 4)O_win = true;

            x = o = 0;
            FOR(i, 4)
            {
                if(str[i][3-i] =='X')x++;
                else if(str[i][3-i] == 'O')o++;
                else if(str[i][3-i] == 'T')
                {
                    x++;
                    o++;
                }
            }
            if(x == 4)X_win = true;
            else if(o == 4)O_win = true;

        }
        if(X_win)printf("Case #%d: X won\n", t+1);
        else if(O_win)printf("Case #%d: O won\n",t+1);
        else
        {
            if(Dot)printf("Case #%d: Game has not completed\n", t+1);
            else printf("Case #%d: Draw\n", t+1);
        }


    }
    return 0;
}


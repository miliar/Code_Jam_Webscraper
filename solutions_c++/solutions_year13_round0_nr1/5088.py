#include <ctime>
#include <iostream>
#include <fstream>
#include <cstring>
#include <algorithm>
#include <queue>
#include <cmath>
#include <map>
#include <set>
#include <bitset>
#include <stack>
#include <deque>
#include <assert.h>

using namespace std;
#define BUG1 puts("BUG11\n")
#define BUG2 puts("BUG22\n")
#define rep(i,a,b) for(int (i)=(a);(i)<=(b);(i)++)
#define rp(i,a) for(int i=0;i<a;i++)
#define FD(i,a,b) for(int i=a;i>=b;i--)
#define STOP  system("pause")
#define PP printf(" ")
#define mem(x,y) memset(x,y,sizeof(x))
#define LN printf("\n");
#define du freopen("in.txt","r",stdin)
#define chu freopen("out.txt","w",stdout)
#define EPS 1e-8

#define FI first
#define SE second
#define PB push_back
#define MP make_pair


typedef long long LL;
inline int dblcmp(double x) { return fabs(x)<EPS?0:x>0?1:-1; }
inline bool insize(int c,int l,int r){if (c>=l&&c<=r) return true; return false;}
template<class T> inline void checkmin(T &a,T b)	{if(a == -1 || a > b)a = b;}
template<class T> inline void checkmax(T &a,T b)	{if(a < b)	a = b;}
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef pair<int ,int> II;

int dx[] = {0,1,0,-1};//up Right down Left
int dy[] = {1,0,-1,0};
template<class T> inline void sf(T& x)
{
    char c;
    int mul = 1;
    while((c = getchar()) != EOF)
    {
        if(c == '-')mul = -1;
        if(c >= '0' && c <= '9')
        {
            x = c-'0';
            break;
        }
    }
    if(c == EOF){x = EOF;return;}
    while(c = getchar())
    {
        if(c >= '0' && c <= '9')
        {
            x = (x<<1)+(x<<3)+(c-'0');
        }
        else break;
    }
    x *= mul;
}

const int N= 50005;       // 点数
const int E=200555;   //边数
const int INF= 0x3f3f3f3f;
const long long  LINF= 0x3F3F3F3F3F3F3F3FLL;

char ch[10][10];

int cal()
{
        bool flag= 0;
        char ans;
        rep(i,1,4)
            if(ch[i][1]!='.' && ch[i][1]==ch[i][2] && ch[i][2]==ch[i][3]&& ch[i][3]==ch[i][4]&& ch[i][4]==ch[i][1])
            {
                flag= 1;
                ans= ch[i][1];
                break;
            }
        rep(i,1,4)
            if(ch[1][i]!='.' && ch[1][i]==ch[2][i] &&ch[3][i]==ch[2][i] && ch[3][i]==ch[4][i] &&ch[4][i]==ch[1][i])
            {
                flag= 1;
                ans= ch[1][i];
            }
        if(ch[1][1]!='.' && ch[1][1]==ch[2][2] && ch[2][2]==ch[3][3]&& ch[3][3]==ch[4][4] )
        {
            ans= ch[1][1];
            flag= 1;
        }
        if(ch[1][4]!='.' && ch[1][4]==ch[2][3] &&ch[2][3]==ch[3][2] && ch[4][1]==ch[3][2])
        {
            ans= ch[1][4];
            flag= 1;
        }


        if(flag)
        {
            return ans;
        }

        rep(i,1,4) rep(j,1,4)
            if(ch[i][j]=='.')
            {
                return -1;
                break;
            }
        return 0;
}

int main(){
    du;chu;
    int nca, ica(0);
    sf(nca);
    while(nca--)
    {
        rep(i,1,4)
            scanf("%s", &ch[i][1]);

        printf("Case #%d: ", ++ica);
        bool flag= 0;
        char  ans= 0;

        int t= cal();
        if(t>0)
        {
            printf("%c won\n", (char)t);
            continue;
        }

        rep(i,1,4) rep(j,1,4)
            if(ch[i][j]=='T')
            {
                ch[i][j]= 'X';
                t= cal();
                if(t>0)
                {
                    flag= 1;
                    printf("%c won\n", (char)t);
                    break;
                }
                ch[i][j]= 'O';
                t= cal();
                if(t>0)
                {
                    flag= 1;
                    printf("%c won\n", (char)t);;
                    break;
                }
            }

        if(!flag)
        {
            if(t==0)
                puts("Draw");
            else
                puts("Game has not completed");
        }


    }



}


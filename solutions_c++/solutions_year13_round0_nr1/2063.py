#include<iostream>
#include<cstdio>
#include<cstring>
#include<cmath>
#include<cstdlib>
#include<string>
#include<vector>
#include<queue>
#include<deque>
#include<map>
#include<set>
#include<algorithm>
using namespace std;
#define pb push_back
#define mp make_pair
#define fi first
#define se second
#define sz(a) ((int)(a).size())
#define all(a) (a).begin(),(a).end()
#define rep(i,n) for(int i=0;i<(n);i++)
#define repp(i,a,n) for(int i=(a);i<(n);i++)
#define dec(i,n) for(int i=(n);i>0;i--)
#define decc(i,a,n) for(int i=(a);i>(n);i--)
#define Max(a,b) ((a)>(b)?(a):(b))
#define Min(a,b) ((a)<(b)?(a):(b))
#define abs(a) ((a)<0?-(a):(a))
#define sqr(a) ((a)*(a))
#define mem(a,b) memset((a),(b),sizeof(a))
#define clr(a) mem(a,0)
const double pi=acos(-1.0);
const int inf=10000000;
typedef long long ll;
typedef pair<int,int> PII;
typedef vector<int> VI;
typedef vector< PII > VPII;
typedef vector< string > VS;
typedef vector< ll > VLL;
#define eps 1e-9
//main code starts here
#define max 5
char board[max][max];
bool win(char ch)
{
    int c;
    rep(i,4) //row
    {
        c=0;
        rep(j,4)if(board[i][j]=='T'||board[i][j]==ch)c++;
        if(c==4)return 1;
    }
    rep(i,4) //col
    {
        c=0;
        rep(j,4)if(board[j][i]=='T'||board[j][i]==ch)c++;
        if(c==4)return 1;
    }
    c=0;
    rep(i,4)if(board[i][i]=='T'||board[i][i]==ch)c++;
    if(c==4)return 1;
    c=0;
    rep(i,4)if(board[i][3-i]=='T'||board[i][3-i]==ch)c++;
    if(c==4)return 1;
    return 0;
}
bool isblank()
{
    rep(i,4)rep(j,4)if(board[i][j]=='.')return 1;
    return 0;
}
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int t,cas=1;
    cin>>t;
    while(t--)
    {
        rep(i,4)scanf("%s",board[i]);
        bool xwin=win('X');
        bool owin=win('O');
        printf("Case #%d: ",cas++);
        if(xwin)puts("X won");
        else if(owin)puts("O won");
        else if(isblank())puts("Game has not completed");
        else puts("Draw");
    }
	return 0;
}

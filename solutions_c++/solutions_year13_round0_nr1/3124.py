#define _CRT_SECURE_NO_WARNINGS
#include <algorithm>
#include <numeric>
#include <string>
#include <cstring>
#include <set>
#include <map>
#include <vector>
#include <queue>
#include <iostream>
#include <iterator>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <sstream>

using namespace std;

#define REP(i,n) for (int i=0,_n=(n); i < _n; i++)
#define REPD(i,n) for (int i=(n)-1; i >= 0; i--)
#define FOR(i,a,b) for (int _b=(b), i=(a); i <= _b; i++)
#define FORD(i,a,b) for(int i=(a),_b=(b);i>=_b;i--)
#define ALL(c) (c).begin(), (c).end()
#define SORT(c) sort(ALL(c))

#define CLEAR(x) memset(x,0,sizeof x);
#define CLEARA(x) memset(&x,0,sizeof x);
#define FILL(x,v) memset(x,v,sizeof x);
#define FILLA(x,v) memset(&x,v,sizeof x);

#define VAR(a,b) __typeof(b) a=(b)
#define FOREACH(it,c) for(VAR(it,(c).begin());it!=(c).end();++it)

#define REVERSE(c) reverse(ALL(c))
#define UNIQUE(c) SORT(c),(c).resize(unique(ALL(c))-(c).begin())
#define INF 0x7fffffff
#define X first
#define Y second
#define pb push_back
#define SZ(c) (int)(c).size()
#define MP make_pair
#define eps 1.0e-11
const double pi = acos(-1.0);

typedef pair<int, int> PII;
typedef vector<PII> VPII;
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef long long LL;

#define FN "A-Large"

#define N 111000
int nX,nO;
bool draw=true;
char board[4][4];

int main()
{
	freopen(FN ".in","r",stdin);
	freopen(FN ".out","w",stdout);

	int T,X;
	scanf("%d",&X);
	string temp;
	FOR(T,1,X)
	{
       draw=true;
       printf("Case #%d: ",T);
	   REP(i,4)
	   {
            scanf("%s",&board[i]);
       }
       REP(i,4)
       {
            nX=0;
            nO=0;
            REP(j,4)
            {
                if (board[i][j]=='.') 
                {
                    draw=false;
                    break;
                }
                if (board[i][j]=='X') nX++;
                if (board[i][j]=='O') nO++;
                if (board[i][j]=='T') 
                {
                    nX++;
                    nO++;
                }
            }
            if (nX==4 or nO==4) break;
       }
       
       if (nX!=4 && nO!=4)
       REP(i,4)
       {
            nX=0;
            nO=0;
            REP(j,4)
            {
                if (board[j][i]=='.') 
                {
                    draw=false;
                    break;
                }
                if (board[j][i]=='X') nX++;
                if (board[j][i]=='O') nO++;
                if (board[j][i]=='T') 
                {
                    nX++;
                    nO++;
                }
            }
            if (nX==4 or nO==4) break;
       }
       
       if (nX!=4 && nO!=4)
       {
            nX=0;
            nO=0;
            REP(i,4)
            {
                if (board[i][i]=='.') 
                {
                    draw=false;
                    break;
                }
                if (board[i][i]=='X') nX++;
                if (board[i][i]=='O') nO++;
                if (board[i][i]=='T') 
                {
                    nX++;
                    nO++;
                }
            }
       }
       
       
       if (nX!=4 && nO!=4)
       {
            nX=0;
            nO=0;
            for (int i=3;i>=0;i--)
            {
                if (board[3-i][i]=='.') 
                {
                    draw=false;
                    break;
                }
                if (board[3-i][i]=='X') nX++;
                if (board[3-i][i]=='O') nO++;
                if (board[3-i][i]=='T') 
                {
                    nX++;
                    nO++;
                }
            }
       }
       
       if (nX==4) 
        cout << "X won";
       else if(nO==4)
        cout << "O won";
       else if (draw)
        cout << "Draw";
       else
        cout << "Game has not completed"; 
       cout << endl;
	}
	return 0;
}

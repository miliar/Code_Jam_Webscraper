#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
 
using namespace std;

#define sz(a) (LL)a.size()
#define all(a) a.begin(), a.end()
#define pb push_back
typedef vector <int> vi;
typedef vector <string> vs;
typedef pair<int, int> pii;
#define LL long long
#define INF 1000000

const int MAX = 110;
int ans;
int r;
int board[2][110][110];

int main()
{
    //freopen("inp.txt", "r", stdin);
    //freopen("out.txt", "r", stdin);
	
    freopen("C-small-attempt0.in", "r", stdin);
    freopen("C-small-attempt0.out", "w", stdout);

    //freopen("C-small-attempt1.in", "r", stdin);
    //freopen("C-small-attempt1.out", "w", stdout);

	//freopen("C-large.in", "r", stdin);
	//freopen("C-large.out", "w", stdout);

	int numtest, test, i, j, x1, y1, x2, y2, x, y;
	cin >> numtest;

	for (test=1; test<=numtest; test++)
	{
        ans = 0;
        
        memset(board, 0, sizeof(board));
        cin >> r;
        for (i=0; i<r; i++)
        {
            cin >> x1 >> y1 >> x2 >> y2;
            for (x=x1; x<=x2; x++)
                for (y=y1; y<=y2; y++) board[0][y][x]=1;
        }

        int cur=0;
        for (;;ans++)
        {
            cur=1-cur;
            bool stop=true;
            for (i=0; i<MAX; i++) for (j=0; j<MAX; j++)
            {
                board[cur][i][j] = board[1-cur][i][j];
                if (board[1-cur][i][j]!=0) stop=false;
                if (board[1-cur][i][j]==1 && (i==0||board[1-cur][i-1][j]==0) && (j==0||board[1-cur][i][j-1]==0))
                {
                    board[cur][i][j] = 0;
                    continue;
                }
                if (board[1-cur][i][j]==0 && (i>0&&board[1-cur][i-1][j]==1) && (j>0&&board[1-cur][i][j-1]==1))
                {
                    board[cur][i][j] = 1;
                    stop=false;
                    continue;
                }
            }
            if (stop) break;
        }

        cout << "Case #" << (test) << ": " << ans << endl;
	}
	return 0;
}

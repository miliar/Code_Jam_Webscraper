#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <iostream>
#include <fstream>
#include <algorithm>
#include <string>
#define rep(i,j,k) for (int i=j;i<=k;++i)
#define rrep(i,j,k) for (int i=j;i>=k;--i)

using namespace std;

int T,row[4][2],col[4][2],diag[2][2],won;
string s[4];
bool complete;

int main()
{
    ios::sync_with_stdio(false);
    cin >> T;
    rep(test_case,1,T)
	{
	    memset(row,0,sizeof(row));
	    memset(col,0,sizeof(col));
	    memset(diag,0,sizeof(diag));
	    complete = true;
	    won = -1;

	    rep(i,0,3) cin >> s[i];

	    rep(i,0,3) rep(j,0,3)
		{
		    if (s[i][j] == '.') complete = false;
		    else if (s[i][j] == 'X')
			{
			    row[i][0]++;
			    col[j][0]++;
			    if (i == j) diag[0][0]++;
			    if (i + j == 3) diag[1][0]++;
			}
		    else if (s[i][j] == 'O')
			{
			    row[i][1]++;
			    col[j][1]++;
			    if (i == j) diag[0][1]++;
			    if (i + j == 3) diag[1][1]++;
			}
		    else if (s[i][j] == 'T')
			{
			    row[i][0]++;
			    col[j][0]++;
			    row[i][1]++;
			    col[j][1]++;
			    if (i == j) diag[0][0]++,diag[0][1]++;
			    if (i + j == 3) diag[1][0]++,diag[1][1]++;
			}
		}
	    
	    if (won == -1) 
		{
		    rep(i,0,3) if (row[i][0] >= 4 || col[i][0] >= 4) won = 0;
		    rep(i,0,1) if (diag[i][0] >= 4) won = 0;
		}
	    if (won == -1)
		{
		    rep(i,0,3) if (row[i][1] >= 4 || col[i][1] >= 4) won = 1;
		    rep(i,0,1) if (diag[i][1] >= 4) won = 1;
		}
	    cout << "Case #" << test_case << ": ";
	    if (won != -1)
		{
		    if (won == 0)
			cout << "X won" << endl;
		    else 
			cout << "O won" << endl;
		}
	    else
		{
		    if (complete)
			cout << "Draw" << endl;
		    else
			cout << "Game has not completed" << endl;
		}
	}
    return 0;
}

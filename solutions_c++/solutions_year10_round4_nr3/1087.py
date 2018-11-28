#include <string.h>       
#include <vector>       
#include <set>       
#include <map>       
#include <algorithm>       
#include <math.h>       
#include <sstream>       
#include <ctype.h>       
#include <queue>       
#include <stack>       
#include <iostream> 
#include <gmp.h>	// if GMP is not allowed, I apologize
#include <fstream>
using namespace std;


int main()
{

fstream In("c-small.in", ios::in);
fstream Out("c-small.out", ios::out);

int tests;

In >> tests;

for(int h=0; h<tests; h++)
{

int R;
int board[250][250], tempboard[250][250];
memset(board, 0, sizeof(board));

In >> R;

int x1, y1, x2, y2;

for(int i=0; i<R; i++)
{
	In >> x1 >> y1 >> x2 >> y2;
	for(int j=y1; j<=y2; j++) for(int k=x1; k<=x2; k++)
		board[j][k] = 1;
}

int ret = 0;

int flag = true;
while(flag)
{	flag = false;
	for(int i=0; i<250; i++) for(int j=0; j<250; j++)
	{	if(board[i][j]) flag = true;
		if(i==0 || j==0) tempboard[i][j] = 0;
		else if(board[i][j] && (board[i-1][j] || board[i][j-1]) ) tempboard[i][j] = 1;
		else if(board[i-1][j] && board[i][j-1]) tempboard[i][j] = 1;
		else tempboard[i][j] = 0;
	}
	for(int i=0; i<250; i++) for(int j=0; j<250; j++) board[i][j] = tempboard[i][j];
	if(flag) ret++;
}
Out << "Case #" << h+1 << ": " << ret << endl;

}

In.close();

Out.close();

return 0;

}
 

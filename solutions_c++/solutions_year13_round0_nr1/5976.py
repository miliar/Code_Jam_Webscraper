#include <iostream>
#include <vector>
#include <sstream>
#include <algorithm>
#include <numeric>
#include <set>
#include <math.h>
using namespace std;



//#define SMALL
#define LARGE
string check_status(vector<string> board)
{
	bool x,o,x1,o1,xdiag=true,odiag=true,xdiag1=true,odiag1=true,dot=false;
	for(int i=0;i<4;i++)
	{
		x=true,o=true,o1=true,x1=true;
		for(int j=0;j<4;j++)
		{
			if(board[i][j]=='.')
				dot=true;
			if(board[i][j]=='X'||board[i][j]=='.')
			{
				o=false;
			}
			if(board[i][j]=='O'||board[i][j]=='.')
			{
				x=false;
			}
			if(board[j][i]=='X'||board[j][i]=='.')
			{
				o1=false;
			}
			if(board[j][i]=='O'||board[j][i]=='.')
			{
				x1=false;
			}
			if(i==j)
			{
				if(board[i][j]=='O'||board[i][j]=='.')
					xdiag=false;
				if(board[i][j]=='X'||board[i][j]=='.')
					odiag=false;
			}
			else if(i+j==3)
			{
				if(board[i][j]=='O'||board[i][j]=='.')
					xdiag1=false;
				if(board[i][j]=='X'||board[i][j]=='.')
					odiag1=false;
			}
			
		}

		if(x||x1)
			return "X won";
		else if(o||o1)
			return "O won";
	}
	if(xdiag ||xdiag1)
		return "X won";
	else if(odiag ||odiag1)
		return "O won";
	else if(dot)
			return "Game has not completed";
		else
			return "Draw";

}
int main ()
{
	//freopen("a.txt", "rt", stdin);
#ifdef SMALL
	freopen("A-small-attempt0.in","rt",stdin);
	freopen("A-small-attempt0.out","wt",stdout);
#endif
#ifdef LARGE
	freopen("A-large.in","rt",stdin);
	freopen("A-large.out","wt",stdout);
#endif

	int T;
	cin>>T;
	for(int k=0;k<T;k++)
	{
		string temp;
		vector<string> board;
		for(int i=0;i<4;i++)
		{
			cin>>temp;
			board.push_back(temp);
		}
		printf("Case #%d: ",k+1);
		cout<<check_status(board)<<endl;
		

	}
	

	return 0;
}
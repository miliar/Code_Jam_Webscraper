#include <set>
#include <map>
#include <list>
#include <stack>
#include <queue>
#include <ctime>
#include <math.h>
#include <vector>
#include <string>
#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <string.h>
#include <algorithm>
#include <sstream>
#include <complex>
using namespace std;


#define X first
#define Y second
#define pb push_back
#define mp make_pair

const double PI = acos(-1.0);
const double INF = 1000000000;
const int MOD = 1073741824;
const int M = INF;
const double RRR = 180.0/PI;


typedef long long ll;
typedef unsigned long long ull;
typedef long double ld;
typedef vector<int> vi;



int main()
{
	//#ifndef ONLINE_JUDGE
	freopen("INPUT.TXT","r",stdin);
	freopen("OUTPUT.TXT","w",stdout);
	//#endif
	int t;
	cin>>t;
	for(int i=0; i<t; i++)
	{
		vector<string> board(4);
		for(int j=0; j<4; j++)
		{
			cin>>board[j];
		}
		
		for(int j=0; j<4; j++)
		{
			bool f=1;
			for(int k=0; k<4; k++)
			{
				if(board[j][k]=='X' || board[j][k]=='T')
				{
					continue;
				}
				else
				{
					f=0;
					break;
				}
			}
			if(f)
			{
				cout<<"Case #"<<i+1<<": X won"<<endl;
				goto end;
			}
		}
		for(int j=0; j<4; j++)
		{
			bool f=1;
			for(int k=0; k<4; k++)
			{
				if(board[k][j]=='X' || board[k][j]=='T')
				{
					continue;
				}
				else
				{
					f=0;
					break;
				}
			}
			if(f)
			{
				cout<<"Case #"<<i+1<<": X won"<<endl;
				goto end;
			}
		}
		if((board[0][0]=='X' || board[0][0]=='T') && (board[1][1]=='X' || board[1][1]=='T') && (board[2][2]=='X' || board[2][2]=='T') && (board[3][3]=='X' || board[3][3]=='T'))
		{
			cout<<"Case #"<<i+1<<": X won"<<endl;
			goto end;
		}
		if((board[0][3]=='X' || board[0][3]=='T') && (board[1][2]=='X' || board[1][2]=='T') && (board[2][1]=='X' || board[2][1]=='T') && (board[3][0]=='X' || board[3][0]=='T'))
		{
			cout<<"Case #"<<i+1<<": X won"<<endl;
			goto end;
		}





		for(int j=0; j<4; j++)
		{
			bool f=1;
			for(int k=0; k<4; k++)
			{
				if(board[j][k]=='O' || board[j][k]=='T')
				{
					continue;
				}
				else
				{
					f=0;
					break;
				}
			}
			if(f)
			{
				cout<<"Case #"<<i+1<<": O won"<<endl;
				goto end;
			}
		}
		for(int j=0; j<4; j++)
		{
			bool f=1;
			for(int k=0; k<4; k++)
			{
				if(board[k][j]=='O' || board[k][j]=='T')
				{
					continue;
				}
				else
				{
					f=0;
					break;
				}
			}
			if(f)
			{
				cout<<"Case #"<<i+1<<": O won"<<endl;
				goto end;
			}
		}
		if((board[0][0]=='O' || board[0][0]=='T') && (board[1][1]=='O' || board[1][1]=='T') && (board[2][2]=='O' || board[2][2]=='T') && (board[3][3]=='O' || board[3][3]=='T'))
		{
			cout<<"Case #"<<i+1<<": O won"<<endl;
			goto end;
		}
		if((board[0][3]=='O' || board[0][3]=='T') && (board[1][2]=='O' || board[1][2]=='T') && (board[2][1]=='O' || board[2][1]=='T') && (board[3][0]=='O' || board[3][0]=='T'))
		{
			cout<<"Case #"<<i+1<<": O won"<<endl;
			goto end;
		}

		bool f=0;
		for(int j=0; j<4; j++)
		{
			for(int k=0; k<4; k++)
			{
				if(board[j][k]=='.')
				{
					f=1;
				}
			}
		}
		if(f)
		{
			cout<<"Case #"<<i+1<<": Game has not completed"<<endl;
			goto end;
		}
		else
		{
			cout<<"Case #"<<i+1<<": Draw"<<endl;
			goto end;
		}
end:;
	}
	return 0;
}
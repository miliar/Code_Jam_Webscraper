#include <iostream>

using namespace std;

typedef long long int llint;

char board[60][60];

struct cache {
	int h;
	int v;
	int d1;
	int d2;
};

struct cache dR[60][60];
struct cache dB[60][60];

void solveCase(unsigned int caseNum)
{
	int n, i, j, k;
	cin >> n >> k;
	cin.ignore();
	string tmps;
	char tmp;
	for(i=0;i<n;i++)
	{
		for(j=0;j<n;j++)
		{
			board[i][j] = '.';
		}
	}
	for(i=0;i<n;i++)
	{
		tmps = "";
		int next = n-1;
		for(j=0;j<n;j++)
		{
			cin >> tmp;
			if(tmp != '.')
			{
				//board[i][next] = tmp;
				tmps += tmp;
				next--;
			}
		}

		for(j=0;j<tmps.length();j++)
		{
			board[i][n-1-j] = tmps[tmps.length()-j-1];
		}
	}
	for(i=0;i<n;i++)
	{
		for(j=0;j<n;j++)
		{
			// red
			if(board[i][j] == 'R')
			{
				struct cache t;
				dR[i][j].h = 1;
				dR[i][j].v = 1;
				dR[i][j].d1 = 1;
				dR[i][j].d2 = 1;
				if(i>0 && board[i-1][j] == 'R')
					dR[i][j].v += dR[i-1][j].v;
				if(j>0 && board[i][j-1] == 'R')
					dR[i][j].h += dR[i][j-1].h;
				if(i>0)
				{
					if(j>0 && board[i-1][j-1]=='R')
						dR[i][j].d1 += dR[i-1][j-1].d1;
					if(j<n-1 && board[i-1][j+1]=='R')
						dR[i][j].d2 += dR[i-1][j+1].d2;
				}
			}
			else
			{
				dR[i][j].h = 0;
				dR[i][j].v = 0;
				dR[i][j].d1 = 0;
				dR[i][j].d2 = 0;
			}
			// black
			if(board[i][j] == 'B')
			{
				struct cache t;
				dB[i][j].h = 1;
				dB[i][j].v = 1;
				dB[i][j].d1 = 1;
				dB[i][j].d2 = 1;
				if(i>0 && board[i-1][j] == 'B')
					dB[i][j].v += dB[i-1][j].v;
				if(j>0 && board[i][j-1] == 'B')
					dB[i][j].h += dB[i][j-1].h;
				if(i>0)
				{
					if(j>0 && board[i-1][j-1]=='B')
						dB[i][j].d1 += dB[i-1][j-1].d1;
					if(j<n-1 && board[i-1][j+1]=='B')
						dB[i][j].d2 += dB[i-1][j+1].d2;
				}
			}
			else
			{
				dB[i][j].h = 0;
				dB[i][j].v = 0;
				dB[i][j].d1 = 0;
				dB[i][j].d2 = 0;
			}
		}
	}
	bool winB=false, winR=false;
	for(i=0;i<n;i++)
	{
		for(j=0;j<n;j++)
		{
			if(dR[i][j].h >= k || dR[i][j].v >= k || dR[i][j].d1 >= k || dR[i][j].d2 >= k)
				winR = true;
			if(dB[i][j].h >= k || dB[i][j].v >= k || dB[i][j].d1 >= k || dB[i][j].d2 >= k)
				winB = true;
		}
	}
	
	cout << "Case #" << caseNum << ": ";
	if(winB)
	{
		if(winR)
			cout << "Both";
		else
			cout << "Blue";
	}
	else
	{
		if(winR)
			cout << "Red";
		else
			cout << "Neither";
	}
	cout << endl;
}

int main()
{
  unsigned int t, i;
  
  cin >> t;
  for(i=1; i<=t; i++)
    solveCase(i);

  return 0;
}
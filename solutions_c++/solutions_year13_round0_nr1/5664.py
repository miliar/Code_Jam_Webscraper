#include <iostream>
#include <string>

using namespace std;

int main()
{
	int n, i, j;
	string str;
	char brd[4][4], won;
	bool draw;
	cin >> n;
	for(int c=1; c<=n; c++)
	{
		for(i=0; i<4; i++)
		{
			cin >> str;
			for(j=0; j<4; j++)
				brd[i][j]=str[j];
		}
		cin;
		cout << "Case #" << c << ": ";
		draw=true;
		for(i=0; i<4; i++)
		{
			if(brd[i][0]=='.')
			{
				draw=false;
				continue;
			}
			if(brd[i][0]=='T')
				won=brd[i][1];
			else
				won=brd[i][0];
			for(j=1; j<4; j++)
			{
				if(brd[i][j]=='.')
				{
					draw=false;
					break;
				}
				if(brd[i][j]!=won&&brd[i][j]!='T')
					break;
			}
			if(j==4)
				break;
		}
		if(i!=4)
		{
			cout << won << " won" << endl;
			continue;
		}
		for(j=0; j<4; j++)
		{
			if(brd[0][j]=='.')
			{
				draw=false;
				continue;
			}
			if(brd[0][j]=='T')
				won=brd[1][j];
			else
				won=brd[0][j];
			for(i=1; i<4; i++)
			{
				if(brd[i][j]=='.')
				{
					draw=false;
					break;
				}
				if(brd[i][j]!=won&&brd[i][j]!='T')
					break;
			}
			if(i==4)
				break;
		}
		if(j!=4)
		{
			cout << won << " won" << endl;
			continue;
		}
		if(brd[0][0]!='.')
		{
			if(brd[0][0]=='T')
				won=brd[1][1];
			else
				won=brd[0][0];
			for(i=1; i<4; i++)
			{
				if(brd[i][i]=='.')
				{
					draw=false;
					break;
				}
				if(brd[i][i]!=won&&brd[i][i]!='T')
					break;
			}
			if(i==4)
			{
				cout << won << " won" << endl;
				continue;
			}
		}
		if(brd[0][3]!='.')
		{
			if(brd[0][3]=='T')
				won=brd[1][2];
			else
				won=brd[0][3];
			for(i=1; i<4; i++)
			{
				if(brd[i][3-i]=='.')
				{
					draw=false;
					break;
				}
				if(brd[i][3-i]!=won&&brd[i][3-i]!='T')
					break;
			}
			if(i==4)
			{
				cout << won << " won" << endl;
				continue;
			}
		}
		if(draw)
			cout << "Draw" << endl;
		else
			cout << "Game has not completed" << endl;
	}
	return 0;
}
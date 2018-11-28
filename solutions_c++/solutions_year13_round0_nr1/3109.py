#include <iostream>
using namespace std;
char map[5][5];

int check()
{
	char c='T';
	bool full = true;
	for (int i=0;i<4;i++)
	{
		if (map[i][0]=='.')
		{
			full = false;
			continue;
		}
		c=map[i][0];
		bool won = true;
		for (int j=1;j<4;j++)
			if (map[i][j]=='.')
			{
				full = false;
				won = false;
				break;
			}
			else if (c==map[i][j])
				continue;
			else if (map[i][j]=='T')
				continue;
			else if (c=='T')
			{
				c=map[i][j];
				continue;
			}
			else 
			{
				won = false;
				break;
			}
		if (won)
		{
			if (c=='X')
				return 1;
			else return 2;
		}
	}
	for (int i=0;i<4;i++)
	{
		if (map[0][i]=='.')
		{
			full = false;
			continue;
		}
		c=map[0][i];
		bool won = true;
		for (int j=1;j<4;j++)
			if (map[j][i]=='.')
			{
				full = false;
				won = false;
				break;
			}
			else if (c==map[j][i])
				continue;
			else if (map[j][i]=='T')
				continue;
			else if (c=='T')
			{
				c=map[j][i];
				continue;
			}
			else 
			{
				won = false;
				break;
			}
		if (won)
		{
			if (c=='X')
				return 1;
			else return 2;
		}
	}

	bool need = true;
	if (map[0][0]=='.')
	{
		full = false;
		need = false;
	}
	if (need)
	{		
		c=map[0][0];
		bool won = true;
		for (int j=1;j<4;j++)
		{
			if (map[j][j]=='.')
			{
				full = false;
				won = false;
				break;
			}
			else if (c==map[j][j])
				continue;
			else if (map[j][j]=='T')
				continue;
			else if (c=='T')
			{
				c=map[j][j];
				continue;
			}
			else 
			{
				won = false;
				break;
			}
		}
		if (won)
		{
			if (c=='X')
				return 1;
			else return 2;
		}
	}

	need = true;
	if (map[0][3]=='.')
	{
		full = false;
		need = false;
	}
	if (need)
	{		
		c=map[0][3];
		bool won = true;
		for (int j=1;j<4;j++)
			if (map[j][3-j]=='.')
			{
				full = false;
				won = false;
				break;
			}
			else if (c==map[j][3-j])
				continue;
			else if (map[j][3-j]=='T')
				continue;
			else if (c=='T')
			{
				c=map[j][3-j];
				continue;
			}
			else 
			{
				won = false;
				break;
			}
		if (won)
		{
			if (c=='X')
				return 1;
			else return 2;
		}
	}

	if (full)
		return 3;
	return 4;

}
int main()
{
	int T;
	cin>>T;
	for (int i=1;i<=T;i++)
	{
		for (int j=0;j<4;j++)
			cin>>map[j];

		int res = check();
		cout<<"Case #"<<i<<": ";
		if (res == 1)
			cout<<"X won"<<endl;
		else if (res == 2)
			cout<<"O won"<<endl;
		else if (res == 3)
			cout<<"Draw"<<endl;
		else if (res == 4)
			cout<<"Game has not completed"<<endl;

	}

	return 0;
}
#include <fstream>
#include <string>
using namespace std;
string f(char[4][4]);

int main()
{
	fstream ifs("Google.in");
	ofstream ofs("Google.out");
	int n;
	int b;
	ifs>>n;
	char board[4][4];
	for(int i=1;i<=n;i++)
	{
		for(int j=0;j<4;j++)
		{
			for(int k=0;k<4;k++)
			{
				ifs>>board[j][k];
			}
		}
		string a;
		a=f(board);
		ofs<<"Case #"<<i<<":"<<" "<<a<<endl;
	}
}

string f(char b[4][4])
{
	string a,f;
	string c="Draw";
	for(int i=0;i<4;i++)
	{
		a.clear();
		f.clear();
		for(int k=0;k<4;k++)
		{
			a.push_back(b[i][k]);
			f.push_back(b[k][i]);
		}
		if(a=="XXXX" || a=="XXXT")
		{
			c="X won";
			return c;
		}
		if(a=="OOOO" || a=="OOOT")
		{
			c="O won";
			return c;
		}
		if(f=="OOOO" || f=="OOOT")
		{
			c="O won";
			return c;
		}
		if(f=="XXXX" || f=="XXXT")
		{
			c="X won";
			return c;
		}
	}
	a.clear();
	for(int i=0;i<4;i++)
	{
		a.push_back(b[i][i]);
	}
	if(a=="XXXX" || a=="XXXT")
	{
		c="X won";
		return c;
	}
	if(a=="OOOO" || a=="OOOT")
	{
		c="O won";
		return c;
	}
	a.clear();
	int k=0;
	for(int i=3;i>=0;i--)
	{
		a.push_back(b[k][i]);
		k++;
	}
	if(a=="XXXX" || a=="XXXT")
	{
		c="X won";
		return c;
	}
	if(a=="OOOO" || a=="OOOT")
	{
		c="O won";
		return c;
	}
	for(int i=0;i<4;i++)
	{
		for(int k=0;k<4;k++)
		{
			if(b[i][k]=='.')
			{
				c="Game has not completed";
				return c;
			}
		}
	}
	return c;
}

#include <iostream>
#include <fstream>
using namespace std;

ifstream in;
ofstream out;
char arr[4][4];

bool won(int x, int o, int t)
{
	if((x==3 && t==1) || x==4)
	{
		out << "X won"<< endl;
		return true;
	}
	else if((o==3 && t==1) || o==4)
	{
		out << "O won"<< endl;
		return true;
	}
	return false;
}

bool checkRow()
{
	for(int i=0; i<4; i++)
	{
		int x=0,o=0,t=0;
		for(int j=0; j<4; j++)
		{
			if(arr[i][j]=='X')
				x++;
			else if(arr[i][j]=='O')
				o++;
			else if(arr[i][j]=='T')
				t++;
		}
		if(won(x,o,t))
			return true;
	}
	return false;
}

bool checkCol()
{
	for(int j=0; j<4; j++)
	{
		int x=0,o=0,t=0;
		for(int i=0; i<4; i++)
		{
			if(arr[i][j]=='X')
				x++;
			else if(arr[i][j]=='O')
				o++;
			else if(arr[i][j]=='T')
				t++;
		}
		if(won(x,o,t))
			return true;
	}
	return false;
}

bool checkDiag()
{
	int x=0,o=0,t=0;
	for(int i=0; i<4; i++)
	{
		if(arr[i][i]=='X')
			x++;
		else if(arr[i][i]=='O')
			o++;
		else if(arr[i][i]=='T')
			t++;
	}

	if(won(x,o,t))
		return true;

	x=0,o=0,t=0;
	for(int i=0; i<4; i++)
	{
		if(arr[i][3-i]=='X')
			x++;
		else if(arr[i][3-i]=='O')
			o++;
		else if(arr[i][3-i]=='T')
			t++;
	}

	if(won(x,o,t))
		return true;

	return false;
}
int main()
{
	int t,n;

	in.open("A-large.in");
	out.open("output.txt");
	in >> t;
	n=t;

	while(t-- > 0)
	{
		for(int i=0; i<4; i++)
			for(int j=0; j<4; j++)
				in >> arr[i][j];

		out << "Case #"<< (n-t) << ": ";
		if(checkRow())
			continue;
		else if(checkCol())
			continue;
		else if(checkDiag())
			continue;
		else
		{
			bool flag = false;
			for(int i=0; i<4; i++)
				for(int j=0; j<4; j++)
					if(arr[i][j]=='.')
						flag = true;
			if(flag)
				out << "Game has not completed" << endl;
			else
				out << "Draw" << endl;
		}
	}

	in.close();
	out.close();
}

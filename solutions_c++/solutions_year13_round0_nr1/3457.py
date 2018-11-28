#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int main()
{
	string ifilename="A-large.in",ofilename="1.out";
	ifstream infile (ifilename,ios::in);
	ofstream outfile (ofilename,ios::out);
	int t;
	int ifwon;
	bool ill,tf,isend;
	infile>>t;
	string st[4];
	for (int loop=1;loop<=t;loop++)
	{
		infile>>st[0];
		infile>>st[1];
		infile>>st[2];
		infile>>st[3];
		ifwon=0;
		ill=false;
		for (int i=0;i<4;i++)
		{
			tf=true;
			for (int j=0;j<4;j++)
			{
				if ((st[i][j]!='O')&&(st[i][j]!='T'))
				{
					tf=false;
					break;
				}
			}
			if (tf)
			{
				ill=true;
				ifwon=1;	
			}
			tf=true;
			for (int j=0;j<4;j++)
			{
				if ((st[i][j]!='X')&&(st[i][j]!='T'))
				{
					tf=false;
					break;
				}
			}
			if (tf)
			{
				ill=true;
				ifwon=2;
			}
			tf=true;
			for (int j=0;j<4;j++)
			{
				if ((st[j][i]!='O')&&(st[j][i]!='T'))
				{
					tf=false;
					break;
				}
			}
			if (tf)
			{
				ill=true;
				ifwon=1;	
			}
			tf=true;
			for (int j=0;j<4;j++)
			{
				if ((st[j][i]!='X')&&(st[j][i]!='T'))
				{
					tf=false;
					break;
				}
			}
			if (tf)
			{
				ill=true;
				ifwon=2;
			}
		}
		tf=true;
		for (int i=0;i<4;i++)
			if ((st[i][i]!='O')&&(st[i][i]!='T'))
			{
				tf=false;
				break;
			}
			if (tf)
			{
				ill=true;
				ifwon=1;
			}
		tf=true;
		for (int i=0;i<4;i++)
			if ((st[i][i]!='X')&&(st[i][i]!='T'))
			{
				tf=false;
				break;
			}
			if (tf)
			{
				ill=true;
				ifwon=2;
			}
		tf=true;
		for (int i=0;i<4;i++)
			if ((st[i][3-i]!='O')&&(st[i][3-i]!='T'))
			{
				tf=false;
				break;
			}
			if (tf)
			{
				ill=true;
				ifwon=1;
			}
		tf=true;
		for (int i=0;i<4;i++)
			if ((st[i][3-i]!='X')&&(st[i][3-i]!='T'))
			{
				tf=false;
				break;
			}
			if (tf)
			{
				ill=true;
				ifwon=2;
			}
		outfile<<"Case #"<<loop<<": ";
		if (ill)
			if (ifwon==1)
				outfile<<"O won\n";
			else
				outfile<<"X won\n";
		else
		{
			isend=true;
			for (int i=0;i<4;i++)
				for (int j=0;j<4;j++)
					if (st[i][j]=='.')
					{
						isend=false;
					}
			if (isend)
				outfile<<"Draw\n";
			else
				outfile<<"Game has not completed\n";
		}
	}
}
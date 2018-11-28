#include<fstream>
#include<iostream>

using namespace std;

int main()
{
	int t,tc,x,chk,y;
	char a[10][10],c;
	ifstream ifile("D:/in.in");
	ofstream ofile("D:/out.txt");
	ifile>>t;
	for(tc=0;tc<t;++tc)
	{
		chk=0;
		ifile>>a[0]>>a[1]>>a[2]>>a[3];
		for(x=0;x<4;++x)
		{
			if(a[x][0]!='.')
			{
				c=a[x][0];
				chk=1;
				for(y=1;y<4;++y)
				{
					if(a[x][y]!=c&&a[x][y]!='T')
					{
						chk=0;
						break;
					}
				}
				if(chk==1) break;
			}
			if(a[0][x]!='.')
			{
				c=a[0][x];
				chk=1;
				for(y=1;y<4;++y)
				{
					if(a[y][x]!=c&&a[y][x]!='T')
					{
						chk=0;
						break;
					}
				}
				if(chk==1) break;
			}
		}
		if(chk!=1)
		{
			if(a[0][0]!='.')
			{
				c=a[0][0];
				chk=1;
				for(y=1;y<4;++y)
				{
					if(a[y][y]!=c&&a[y][y]!='T')
					{
						chk=0;
						break;
					}
				}
			}
			if(chk!=1)
			{
				if(a[0][3]!='.')
				{
					c=a[0][3];
					chk=1;
					for(y=1;y<4;++y)
					{
						if(a[y][3-y]!=c&&a[y][3-y]!='T')
						{
							chk=0;
							break;
						}
					}
				}
			}
		}
		if(chk!=1)
		{
			chk=1;
			for(x=0;x<4;++x)
			{
			for(y=0;y<4;++y)
			if(a[x][y]=='.')
			{
				chk=0;
				break;
			}
			if(chk==0) break;
			}
			if(chk==0) ofile<<"Case #"<<tc+1<<": Game has not completed\n";
			else ofile<<"Case #"<<tc+1<<": Draw\n";
		}
		else
		{
			ofile<<"Case #"<<tc+1<<": "<<c<<" won\n";
		}
	}
	return 0;
}

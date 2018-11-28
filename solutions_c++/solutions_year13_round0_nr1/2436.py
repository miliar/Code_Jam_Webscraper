#include<iostream>
#include<fstream>
#include<stdlib.h>
#include<cstring>
using namespace std;

ofstream op;

void o(int flag,int c)
{
		
	op<<"Case #"<<c<<": ";
	if(flag==0)
		op<<"X won\n";
	else if(flag==1)
		op<<"O won\n";
	else if(flag==2)
		op<<"Draw\n";
	else
		op<<"Game has not completed\n";
}
int main()
{
	ifstream ip;
	int i,j,k,l;
	int T,N;
	int min;
	int flag1,flag2;
	char p[4][4];
	char c;

	op.open("output.txt");	
	ip.open("A-small-attempt1.in");
	ip>>T;
	for(k=0;k<T;k++)
	{
		flag1=flag2=0;
		for(i=0;i<4;i++)
			for(j=0;j<4;j++)
				ip>>p[i][j];
		for(i=0;i<4;i++)
		{
			c=p[i][0];
			if(c=='T') c=p[i][1];
			for(j=1;j<4;j++)
			{
				if(p[i][j]!=c && p[i][j]!='T')
					break;
				else if(p[i][j]=='.')
					flag2=1;
			}
			if(j==4 && c=='X') flag1=1;
			else if(j==4 && c=='O') flag1=2;
		}
		
		for(j=0;j<4;j++)
		{
			c=p[0][j];
			if(c=='T') c=p[1][j];
			for(i=1;i<4;i++)
			{
				if(p[i][j]!=c && p[i][j]!='T')
					break;
			}
			if(i==4 && c=='X') flag1=1;
			else if(i==4 && c=='O') flag1=2;
		}
		c=p[0][0];
		if(c=='T')
			c=p[1][1];
		for(i=1;i<4;i++)
		{
			if(p[i][i]!=c && p[i][i]!='T')
				break;
		}
		if(i==4 && c=='X')
			flag1=1;
		else if(i==4 && c=='O')
			flag1=2;
		c=p[0][3];
		if(c=='T')
			c=p[1][2];
		for(i=1;i<4;i++)
		{
			if(p[i][3-i]!=c && p[i][3-i]!='T')
				break;
		}
		if(i==4 && c=='X')
			flag1=1;
		else if(i==4 && c=='O')
			flag1=2;
		if(flag1==1)
			o(0,k+1);
		else if(flag1==2)
			o(1,k+1);
		else if(flag2==0)
			o(2,k+1);
		else
			o(3,k+1);
	}
	ip.close();
	op.close();
	return 0;
	
}

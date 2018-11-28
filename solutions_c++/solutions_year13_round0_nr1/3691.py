#include<fstream>
#include<iostream>
using namespace std;
int check(int a[4][4])
{
	int i,j,s=0,p=0,m=0,n=0;
	for(i=0;i<4;i++)
	{
		m+=a[i][i];
		n+=a[i][3-i];
		s=0;p=0;
		for(j=0;j<4;j++)
		{
			s+=a[i][j];
			p+=a[j][i];
		}
		if(s==4||p==4||s==13||p==13)
		return 1;
		else if(s==-4||p==-4||s==7||p==7)
		return -1;
	}
	if(m==4||n==4||m==13||n==13)
	return 1;
	else if(m==-4||n==-4||m==7||n==7)
	return -1;
	else return 0;
}
int main()
{
	ifstream f("1.in");
	ofstream g("1.out");
	int t,k,i,j,a[4][4],flag=1;
	char m;
	f>>t;
	for(k=1;k<=t;k++)
	{
		flag=1;
		for(i=0;i<4;i++)
		for(j=0;j<4;j++)
		{
			f>>m;
			if(m=='X')
				a[i][j]=1;
			else if(m=='O')
				a[i][j]=-1;
			else if(m=='T')
				a[i][j]=10;
			else
				{a[i][j]=0;flag=0;}
		}
		int q=check(a);
		g<<"Case #"<<k<<": ";
		if(q==1)
		g<<"X won\n";
		else if(q==-1)
		g<<"O won\n";
		else
		{if(flag)
		g<<"Draw\n";
		else
		g<<"Game has not completed\n";}
	}
}

#include<iostream>
#include<stdio.h>
#include<fstream>
#include<vector>
#include<string>
using namespace std;
char str[4][4];
int check(char a)
{
	int i,j,n=0,x=-1,y=-1,k,l,m;
	for(i=0;i<4;i++)
		for(j=0;j<4;j++)
			if(str[i][j]=='.')
			{
				n=1;
			}
			else if(str[i][j]=='T')
			{
				str[i][j]=a;
				x=i;
				y=j;
			}
	for(i=0;i<4;i++)
	{
		for(j=0;j<4;j++)
		{
			if(str[i][j]!=a)
				break;
		}
		if(j==4)
		{
			if(x!=-1&&y!=-1)
				str[x][y]='T';
			return 1;
		}
	}
	for(j=0;j<4;j++)
	{
		for(i=0;i<4;i++)
		{
			if(str[i][j]!=a)
				break;
		}
		if(i==4)
		{
			if(x!=-1&&y!=-1)
				str[x][y]='T';
			return 1;
		}
	}
	if((str[0][0]==a&&str[1][1]==a&&str[2][2]==a&&str[3][3]==a)||(str[0][3]==a&&str[1][2]==a&&str[2][1]==a&&str[3][0]==a))
	{
		if(x!=-1&&y!=-1)
			str[x][y]='T';
		return 1;
	}
	if(x!=-1&&y!=-1)
		str[x][y]='T';
	if(n==0)
		return -1;
	return 0;
}
int main()
{
	int i,j,t,k,n,a,b;
	//fstream cin;
	double p,ans,x,y;
	vector<double>arr;
	//cin.open("C:\\Users\\Sushrut\\Desktop\\Google Code Jam\\2013\\Qualify\\A\\Small Input.txt",ios::in);
	//freopen("C:\\Users\\Sushrut\\Desktop\\Google Code Jam\\2013\\Qualify\\A\\Small Output.txt","w",stdout);
	cin>>t;
	for(k=1;k<=t;k++)
	{
	//	cin.ignore();
		for(i=0;i<4;i++)
			cin>>str[i];
		j=check('X');
		if(j==-1)
			cout<<"Case #"<<k<<": Draw"<<endl;
		else if(j==1)
			cout<<"Case #"<<k<<": X won"<<endl;
		else
		{
			j=check('O');
			if(j==1)
				cout<<"Case #"<<k<<": O won"<<endl;
			else
				cout<<"Case #"<<k<<": Game has not completed"<<endl;
		}
	}
	return 0;
}
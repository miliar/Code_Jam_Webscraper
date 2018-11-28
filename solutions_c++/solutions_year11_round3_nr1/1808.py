#include<iostream>
using namespace std;

int main()
{
int tc;
cin>>tc;
int t=1;
while(t<=tc)
{

int rows,columns;
cin>>rows>>columns;
char mat[rows][columns];
char finalmat[rows][columns];
int blue=0;
for(int i=0;i<rows;i++)
{
for(int j=0;j<columns;j++)
{
cin>>mat[i][j];
if(mat[i][j]=='#')
blue++;
}
}
if(blue%4!=0)
cout<<"Case #"<<t<<":\n"<<"Impossible\n";
else
{
	for(int i=0;i<rows-1;i++)
	{
		for(int j=0;j<columns-1;j++)
		{
			if(mat[i][j]=='#'&&mat[i][j+1]=='#'&&mat[i+1][j]=='#'&&mat[i+1][j+1]=='#')
			{
				mat[i][j]='/';
				mat[i][j+1]='\\';
				mat[i+1][j]='\\';
				mat[i+1][j+1]='/';
				blue = blue-4;
			}
		}
	}
	if(blue ==0)
	{
		cout<<"Case #"<<t<<":\n";
		for(int i=0;i<rows;i++)
		{
			for(int j=0;j<columns;j++)
			{
				cout<<mat[i][j];
			}
			cout<<"\n";
		}
	}
	else
	cout<<"Case #"<<t<<":\n"<<"Impossible\n";
}

t++;
}
}

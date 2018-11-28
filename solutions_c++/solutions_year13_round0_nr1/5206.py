#if 1
#include<stdio.h>
#include<iostream>
#include<string>
#include<cstring>
#include<algorithm>

using namespace std;
int main()
{
	freopen("text.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int n;
	scanf("%d\n",&n);
	char a[100][100]={};
	for(int p=0;p<n;p++)
	{
		for(int j=0;j<4;j++)
		{
			gets(a[j]);
		}
		for(int i=0;i<4;i++)
		{
			for(int j=0;j<4;j++)
			{
				if(a[i][j]!='X'&&a[i][j]!='T')
					break;
				if(j==3)
				{
					cout<<"Case #"<<p+1<<": X won"<<endl;
					goto m;
				}
			}
			for(int j=0;j<4;j++)
			{
				if(a[j][i]!='X'&&a[j][i]!='T')
					break;
				if(j==3)
				{
					cout<<"Case #"<<p+1<<": X won"<<endl;
					goto m;
				}
			}
			for(int j=0;j<4;j++)
			{
				if(a[i][j]!='O'&&a[i][j]!='T')
					break;
				if(j==3)
				{
					cout<<"Case #"<<p+1<<": O won"<<endl;
					goto m;
				}
			}
			for(int j=0;j<4;j++)
			{
				if(a[j][i]!='O'&&a[j][i]!='T')
					break;
				if(j==3)
				{
					cout<<"Case #"<<p+1<<": O won"<<endl;
					goto m;
				}
			}
		}
			for(int j=0;j<4;j++)
			{
				if(a[j][j]!='X'&&a[j][j]!='T')
					break;
				if(j==3)
				{
					cout<<"Case #"<<p+1<<": X won"<<endl;
					goto m;
				}
			}
			for(int j=0;j<4;j++)
			{
				if(a[j][3-j]!='X'&&a[j][3-j]!='T')
					break;
				if(j==3)
				{
					cout<<"Case #"<<p+1<<": X won"<<endl;
					goto m;
				}
			}
			for(int j=0;j<4;j++)
			{
				if(a[j][j]!='O'&&a[j][j]!='T')
					break;
				if(j==3)
				{
					cout<<"Case #"<<p+1<<": O won"<<endl;
					goto m;
				}
			}
			for(int j=0;j<4;j++)
			{
				if(a[j][3-j]!='O'&&a[j][3-j]!='T')
					break;
				if(j==3)
				{
					cout<<"Case #"<<p+1<<": O won"<<endl;
					goto m;
				}
			}

			
		for(int i=0;i<4;i++)
		{
			for(int j=0;j<4;j++)
			{
				if(a[i][j]=='.')
				{
					cout<<"Case #"<<p+1<<": Game has not completed"<<endl;
					goto m;
				}
			}
		}
		
					cout<<"Case #"<<p+1<<": Draw"<<endl;
m:		if(p<n-1)
			gets(a[4]);
	}
}













#endif
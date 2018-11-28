#include <iostream>
#include <fstream>
#include <cstdio>
#include <cstring>
using namespace std;
char s[55][55];
int n,m,d[55][55];
bool fa()
{
    int i,j;
	for(i=0;i<n;i++)
		for(j=0;j<m;j++)
		{
			if(s[i][j]=='#'&&!d[i][j])
			{
				if(s[i][j+1]=='#'&&i+1<n&&s[i+1][j]=='#'&&s[i+1][j+1]=='#')
				{
					s[i][j]=s[i+1][j+1]='/';
					s[i][j+1]=s[i+1][j]='\\';
					d[i][j]=d[i+1][j]=d[i][j+1]=d[i+1][j+1]=1;
				}
			}
		}
	for(i=0;i<n;i++)
		for(j=0;j<m;j++)
			if(s[i][j]=='#')
			{
				return false;
			}
	return true;
}
int main()
{
	ofstream of("s.txt");
	int t,i,j,k=0;
	scanf("%d",&t);
	while(t--)
	{
		k++;
		scanf("%d%d",&n,&m);
		memset(d,0,sizeof(d));
		for(i=0;i<n;i++)
			scanf("%s",s[i]);
		of<<"Case #"<<k<<":"<<endl;
        if(fa())
		{
			for(i=0;i<n;i++)
			{
		for(j=0;j<m;j++)
		{
			of<<s[i][j];
			cout<<s[i][j];
		}
		cout<<endl;
		of<<endl;
			}
		}
		else
		{
			of<<"Impossible"<<endl;
			cout<<"Impossible"<<endl;
		}
	}
	return 0;
}
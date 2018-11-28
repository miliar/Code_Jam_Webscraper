#include <iostream>
#include <string>
#include <string.h>
#include <cstring>
#include <algorithm>
#include <math.h>
#include <set>
#include <map>
#include <vector>
#include <bitset>
#include <stdio.h>
#include <queue>



using namespace std;
int T,test,a[100][100],n,m;
char s[100],an[100][100];
__int64 ans;
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("output.txt","w",stdout);

	cin>>T;
	for(test=1;test<=T;test++)
	{
		ans=0;
		cin>>n>>m;
		for(int i=0;i<n;i++)
		{
			cin>>s;
			for(int j=0;j<m;j++)
				if(s[j]=='#')
					a[i][j]=1;
				else
					a[i][j]=0;
		}
		for(int i=0;i<n-1;i++)
			for(int j=0;j<m-1;j++)
				if(a[i][j]==1&&a[i+1][j]==1&&a[i][j+1]==1&&a[i+1][j+1]==1)
					a[i][j]=a[i+1][j]=a[i][j+1]=a[i+1][j+1]=-1;
		int cur=0;
		for(int i=0;i<n;i++)
			for(int j=0;j<m;j++)
				if(a[i][j]==1)
					cur++;
		
		cout<<"Case #"<<test<<": "<<endl;
		if(cur>0)
			cout<<"Impossible"<<endl;
		else
		{
			for(int i=0;i<101;i++)
				for(int j=0;j<101;j++)
					an[i][j]=0;
			for(int i=0;i<n;i++)
				for(int j=0;j<m;j++)
				{
					if(a[i][j]==0)
						an[i][j]='.';
					if(a[i][j]==-1)
					{
						a[i][j]=a[i+1][j]=a[i][j+1]=a[i+1][j+1]=3;
						an[i][j]=an[i+1][j+1]='/';
						an[i][j+1]=an[i+1][j]='\\';
					}

				}
			for(int i=0;i<n;i++)
				cout<<an[i]<<endl;
		}
	}
	return 0;
}
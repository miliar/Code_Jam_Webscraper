#include<iostream>
#include<cstdio>
#include<cstring>
#include<algorithm>
using namespace std;
#define rep(ini,n) for(int i=ini;i<n;i++)
char mat[52][52];
int main()
{
	int t,r,c;
	cin>>t;
	
	for(int test=1;test<=t;test++)
	{
		rep(0,52)
		{
			for(int j=0;j<52;j++)
			mat[i][j]=0;
		}
		cin>>r>>c;
		rep(0,r)
		{
			cin>>mat[i];
		}
		cout<<"Case #"<<test<<": "<<endl;
		for(int i=0;i<r;i++)
		{
			for(int j=0;j<c;j++)
			{
				if(mat[i][j]=='#')
				{
					if(mat[i+1][j]=='#' && mat[i][j+1]=='#'&&mat[i+1][j+1]=='#')
					{
						mat[i+1][j]='\\' ;mat[i][j+1]='\\';mat[i+1][j+1]='/';mat[i][j]='/';
						
					}
					else
					{
						cout<<"Impossible"<<endl;
						goto next;
					}
				}
			}
		}
		for(int i=0;i<r;i++)
		{
			for(int j=0;j<c;j++)
			{
				cout<<mat[i][j];
			}
			cout<<endl;
		}		
		next:int a;
	}





	return 0;
}

#include<iostream>
#include<cstdio>
#include<string>
#include<fstream>
using namespace std;
int main()
{
	freopen("1.in","r",stdin);
	freopen("1.out","w+",stdout);
	int test,t,i,j,flag;
	int r,c;
	string s[100]; 
	cin>>test;
	for (t=1;t<=test;t++)
	{
		cin>>r>>c;
		for (i=0;i<r;i++)
			cin>>s[i];
		flag=0;
		for (i=0;i<r;i++)
		{
			if (flag) break;
			for (j=0;j<c;j++)
				if (s[i][j]=='#')
				{
					if (i==r-1 || j==c-1) 
					{
						flag=1;
						break;
					}
					if (s[i+1][j]=='#'&&s[i][j+1]=='#'&&s[i+1][j+1]=='#')
					{
						s[i+1][j]='\\';
						s[i+1][j+1]='/';
						s[i][j]='/';
						s[i][j+1]='\\';
					}
					else flag=1;
				}
		}
		if (flag) 
		{
									printf("Case #%d:\n",t);
						printf("Impossible\n");
		}
		else 
		{
			printf("Case #%d:\n",t);
			for (i=0;i<r;i++)
				cout<<s[i]<<endl;
		}
	}
	return 0;
}
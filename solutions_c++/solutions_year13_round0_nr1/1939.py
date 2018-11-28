#include <vector>
#include <iostream>
#include <string>
#include <algorithm>
#define mod 1000000007
using namespace std;

char a[10][10];
int i,j,w,t,q;

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	cin>>w;
	t=w;
	while(w--)
	{
		for(i=1;i<=4;i++)
		{
			for(j=1;j<=4;j++)
			{
				cin>>a[i][j];
			}
		}
//		X won
		for(i=1;i<=4;i++)
		{
			q=0;
			for(j=1;j<=4;j++)
			{
				if(a[i][j]=='X' || a[i][j]=='T')
				{
					q++;
				}
			}
			if(q==4)
			{
				cout<<"Case #"<<t-w<<": X won"<<endl;
				goto cycle;
			}
		}
		for(i=1;i<=4;i++)
		{
			q=0;
			for(j=1;j<=4;j++)
			{
				if(a[j][i]=='X' || a[j][i]=='T')
				{
					q++;
				}
			}
			if(q==4)
			{
				cout<<"Case #"<<t-w<<": X won"<<endl;
				goto cycle;
			}
		}
		q=0;
		for(i=1;i<=4;i++)
		{
			if(a[i][i]=='T' || a[i][i]=='X')
			{
				q++;
			}
		}
		if(q==4)
		{
			cout<<"Case #"<<t-w<<": X won"<<endl;
			goto cycle;
		}
		q=0;
		for(i=4;i>=1;i--)
		{
			if(a[4-i+1][i]=='T' || a[4-i+1][i]=='X')
			{
				q++;
			}
		}
		if(q==4)
		{
			cout<<"Case #"<<t-w<<": X won"<<endl;
			goto cycle;
		}
//		Y won
		for(i=1;i<=4;i++)
		{
			q=0;
			for(j=1;j<=4;j++)
			{
				if(a[i][j]=='O' || a[i][j]=='T')
				{
					q++;
				}
			}
			if(q==4)
			{
				cout<<"Case #"<<t-w<<": O won"<<endl;
				goto cycle;
			}
		}
		for(i=1;i<=4;i++)
		{
			q=0;
			for(j=1;j<=4;j++)
			{
				if(a[j][i]=='O' || a[j][i]=='T')
				{
					q++;
				}
			}
			if(q==4)
			{
				cout<<"Case #"<<t-w<<": O won"<<endl;
				goto cycle;
			}
		}
		q=0;
		for(i=1;i<=4;i++)
		{
			if(a[i][i]=='T' || a[i][i]=='O')
			{
				q++;
			}
		}
		if(q==4)
		{
			cout<<"Case #"<<t-w<<": O won"<<endl;
			goto cycle;
		}
		q=0;
		for(i=4;i>=1;i--)
		{
			if(a[4-i+1][i]=='T' || a[4-i+1][i]=='O')
			{
				q++;
			}
		}
		if(q==4)
		{
			cout<<"Case #"<<t-w<<": O won"<<endl;
			goto cycle;
		}
		q=0;
		for(i=1;i<=4;i++)
		{
			for(j=1;j<=4;j++)
			{
				if(a[i][j]=='.')
				{
					cout<<"Case #"<<t-w<<": Game has not completed"<<endl;
					goto cycle;
				}
			}
		}
		cout<<"Case #"<<t-w<<": Draw"<<endl;
cycle:;
	}
	return 0;
	}



#include<iostream>
#include<math.h>
#include<algorithm>
#include<string>
using namespace std;


int n,k;
char g[60][60];

char temp[60];


struct pp{
	int left;
	int up;
	int leftup;
};

pp dp[60][60];


int main()
{


	int t;
	cin>>t;
	int cases=0;
	while(t--)
	{
		cout<<"Case #"<<++cases<<": ";
		cin>>n>>k;

		// cout<<endl;

		int i,j;
		for(i=0;i<n;i++)
		{
			cin>>g[i];
			int len=0;
			for(j=0;j<n;j++)
				if(g[i][j]!='.')
				{
					temp[len++]=g[i][j];
				}
				int p=n-1;
				--len;
				while(len>=0)
					g[i][p--]=temp[len--];
				while(p>=0) g[i][p--]='.';
		}


		bool flagred=false;
		bool flagblue= false;
		//检验红色
		for(i=0;i<n;i++)
		{
			if(g[0][i]!='R')
				dp[0][i].left=dp[0][i].leftup=dp[0][i].up=0;
			else
				dp[0][i].left=dp[0][i].leftup=dp[0][i].up=1;

			if(g[i][0]!='R')
				dp[i][0].left=dp[i][0].leftup=dp[i][0].up=0;
			else
				dp[i][0].left=dp[i][0].leftup=dp[i][0].up=1;
		}

		for(i=1;i<n;i++)
		{
			if(flagred)
				break;
			for(j=1;j<n;j++)
			{
				if(g[i][j]!='R')
				{
					dp[i][j].left=dp[i][j].leftup=dp[i][j].up=0;
				}
				else
				{
					dp[i][j].left=dp[i][j-1].left+1;
					if(dp[i][j].left>=k)
					{
						flagred=true;
						break;
					}
					dp[i][j].leftup=dp[i-1][j-1].leftup+1;
					if(dp[i][j].leftup>=k)
					{
						flagred=true;
						break;
					}
					dp[i][j].up=dp[i-1][j].up+1;
					if(dp[i][j].up>=k)
					{
						flagred=true;
						break;
					}
				}
			}
		}

		for(i=0;i<n;i++)
		{
			if(flagred)
				break;
			if(g[n-1][i]!='R')
			{
				dp[n-1][i].left=0;
			}
			else
			{
                dp[n-1][i].left=1;
			}
			if(g[i][0]!='R')
			{
				dp[i][0].left=0;
			}
			else
			{
				dp[i][0].left=1;
 			}
		}

		for(i=n-2;i>=0;i--)
		{
			if(flagred)
				break;
			for(j=1;j<n;j++)
			{
				if(g[i][j]=='R')
					dp[i][j].left=dp[i+1][j-1].left+1;
				else
					dp[i][j].left=0;
				if(dp[i][j].left>=k)
				{
					flagred=true;
					break;
				}
			}
		}



		//校验蓝色
		for(i=0;i<n;i++)
		{
			if(g[0][i]!='B')
				dp[0][i].left=dp[0][i].leftup=dp[0][i].up=0;
			else
				dp[0][i].left=dp[0][i].leftup=dp[0][i].up=1;

			if(g[i][0]!='B')
				dp[i][0].left=dp[i][0].leftup=dp[i][0].up=0;
			else
				dp[i][0].left=dp[i][0].leftup=dp[i][0].up=1;
		}

		for(i=1;i<n;i++)
		{
			if(flagblue)
				break;
			for(j=1;j<n;j++)
			{
				if(g[i][j]!='B')
				{
					dp[i][j].left=dp[i][j].leftup=dp[i][j].up=0;
				}
				else
				{
					dp[i][j].left=dp[i][j-1].left+1;
					if(dp[i][j].left>=k)
					{
						flagblue=true;
						break;
					}
					dp[i][j].leftup=dp[i-1][j-1].leftup+1;
					if(dp[i][j].leftup>=k)
					{
						flagblue=true;
						break;
					}
					dp[i][j].up=dp[i-1][j].up+1;
					if(dp[i][j].up>=k)
					{
						flagblue=true;
						break;
					}
				}
			}
		}

		for(i=0;i<n;i++)
		{
			if(flagblue)
				break;
			if(g[n-1][i]!='B')
			{
				dp[n-1][i].left=0;
			}
			else
			{
                dp[n-1][i].left=1;
			}
			if(g[i][0]!='B')
			{
				dp[i][0].left=0;
			}
			else
			{
				dp[i][0].left=1;
 			}
		}

		for(i=n-2;i>=0;i--)
		{
			if(flagblue)
				break;
			for(j=1;j<n;j++)
			{
				if(g[i][j]=='B')
					dp[i][j].left=dp[i+1][j-1].left+1;
				else
					dp[i][j].left=0;
				if(dp[i][j].left>=k)
				{
					flagblue=true;
					break;
				}
			}
		}


		if(flagblue&&flagred)
			cout<<"Both"<<endl;
		else if(flagblue)
			cout<<"Blue"<<endl;
		else if(flagred)
			cout<<"Red"<<endl;
		else
			cout<<"Neither"<<endl;
	}
}
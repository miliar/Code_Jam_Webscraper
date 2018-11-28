#include<iostream>
#include<map>
#include<string>
using namespace std;

int DP[105][1005];

char data[105][105];

int n,s,q;


char temp[105];

int a[1005];


int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	scanf("%d",&n);
	int line=0;
	while(n--)
	{
		scanf("%d\n",&s);
		map<string,int> mp;
		for(int i=0;i<s;i++)
		{
			gets(data[i]);
			string s=data[i];
			mp[s]=i+1;
			
		}
		scanf("%d\n",&q);
		if(q==0) {printf("Case #%d: %d\n",++line,0);continue;}

		for(int j=0;j<s;j++)
			DP[j][0]=0;
		for(int i=1;i<=q;i++)
			for(int j=0;j<s;j++)
				DP[j][i]=q;


		for(int i=1;i<=q;i++)
		{
			gets(temp);
			string tt=temp;
			a[i]=mp[tt];
			for(int j=0;j<s;j++)
			{
				if(a[i]==j+1)
				{
					DP[j][i]=q;
				}
				else
				{
					for(int k=0; k<s;k++)
					{
						if(k==j) DP[j][i]=min(DP[j][i-1],DP[j][i]);
						else DP[j][i]=min(DP[k][i-1]+1,DP[j][i]);
					}
				}
			}
		}
		int mi=q;
		for(int i=0;i<s;i++)
		{
			if(DP[i][q]<mi) mi=DP[i][q];
		}
		printf("Case #%d: %d\n",++line,mi);
	}
}
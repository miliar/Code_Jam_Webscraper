#pragma warning (disable :4786)
#include<iostream>
#include<algorithm>
#include<string>
#include<map>
using namespace std;
int dp[1000][100];
string q[1001];
#define min(a,b) (a<b ? a: b)
int main()
{

	int N , S , Q ;
	int i  , j , k;
	string str;
	char temp[1111];
	map<string,int> my_map;
	int Case ;
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	while( cin>>N)
	{
		for(Case=1;Case<=N;Case++)
		{
			my_map.clear();
			scanf("%d",&S);
			getchar();
			for(i=0;i<S;i++)
			{	
				gets(temp);
				str = temp ;
				my_map[str]=i;
			}
			scanf("%d",&Q);
			getchar();
			for(i=0;i<Q;i++)
			{
				gets(temp);
				q[i]=temp;
			}
			for(i=0;i<Q;i++)
				for(j=0;j<S;j++)
					dp[i][j]=214748367;
			for(i=0;i<S;i++)
			{
				if(my_map[q[0]]==i)
					dp[0][i]=214748367;
				else
					dp[0][i]=1;
			}
			for(i=1;i<Q;i++)
			{
				for(j=0;j<S;j++)
				{
					if(j!=my_map[q[i]])
						dp[i][j]=min(dp[i][j],dp[i-1][j]);
					else
					{	
						for(k=0;k<S;k++)
							if(k!=j)
								dp[i][k]=min(dp[i][k],dp[i-1][j]+1);
							else
								dp[i][k]=214748364;
					}		
				}
			}
			int Min =2147483647;
			for(i=0;i<S;i++)
				Min = min(Min , dp[Q-1][i]-1);
			if(Q==0)	Min= 0;
			cout<<"Case #"<<Case<<": "<<Min<<endl;
		}
	}
	return 0 ; 
}
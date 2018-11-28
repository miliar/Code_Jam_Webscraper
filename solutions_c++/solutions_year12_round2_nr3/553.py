#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<ctype.h>
#include<math.h>
#include<algorithm>
#include<string>
#include<vector>
#include<map>
#include<set>
#include<queue>
#include<deque>
#include<sstream>
#include<iostream>
#include<stack>
#include<list>
using namespace std;

typedef vector<vector<int> > vii;
typedef vector<int> vi;
typedef vector<string> vs;
typedef long long LL;

#define sz size()
#define all(n) n.begin(),n.end()
#define clr(a,n) memset(a,n,sizeof(a))
#define pb push_back
#define fo(i,j) for(int i=0;i<j;i++)

int arr[22];
int vis[2000002];

int main()
{
	freopen("in.in","r",stdin);
	freopen("out.out","w",stdout);
	
	int T,k=0;
	
	scanf("%d",&T);
	
	while(T--)
	{
		bool OMG=0;
		clr(vis,-1);
		
		k++;
		int N;
		scanf("%d",&N);
		
		for(int i=0;i<N;i++)
		{
			scanf("%d",&arr[i]);
		}
		printf("Case #%d:\n",k);
		for(int i=1;i<(1<<N);i++)
		{
			int x=0;
			for(int j=0;j<N;j++)
			{
				if(i&(1<<j))
				{
					x+=arr[j];
				}
			}
			if(vis[x]!=-1)
			{
				bool flag=0;
				for(int j=0;j<=N;j++)
				{
					if(vis[x]&(1<<j))
					{
						if(flag)printf(" ");
						printf("%d",arr[j]);
						if(!flag)flag=1;
					}
				}
				printf("\n");
				flag=0;
				for(int j=0;j<N;j++)
				{
					if(i&(1<<j))
					{
						if(flag)printf(" ");
						printf("%d",arr[j]);
						if(!flag)flag=1;
					}
				}
				printf("\n");
				OMG=1;
				break;
			}
			vis[x]=i;
		}
		if(!OMG)printf("Impossible\n");
	}
	
}




































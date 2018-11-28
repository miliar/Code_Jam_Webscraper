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

int arr[1005];
bool vis[100];

int add(int x,int y)
{
	int i=0,ret=0,c=1;
	while(x || y)
	{
		if((x%2==1 && y%2==1) || (x%2==0 && y%2==0))vis[i]=0;
		if((x%2==1 && y%2==0) || (x%2==0 && y%2==1))vis[i]=1;
		
		if(vis[i])ret+=c;
		
		c*=2;
		x/=2;
		y/=2;
		i++;
	}
	return ret;
}

int main()
{
    freopen ("C.in","r",stdin);
    freopen ("C.out","w",stdout);
    
    int i,j,k=0,T;
    
    scanf("%d",&T);
    while(T--)
    {
		k++;
		int N,ret=0,F=0;
		scanf("%d",&N);
		
		fo(i,N)scanf("%d",&arr[i]);
		
		for(i=0;i<(1<<N);i++)
		{
			int sum=0;
			int a=0,b=0,f1=0,f2=0;
			for(j=0;j<N;j++)
			{
				if((bool)(i&(1<<j))==1)
					a=add(a,arr[j]),f1=1;
			}
			for(j=0;j<N;j++)
			{
				if((bool)(i&(1<<j))==0)
					b=add(b,arr[j]),f2=1,sum+=arr[j];
			}
			if(a==b && f1 && f2)
			{
				ret=max(ret,sum);
				F=1;
			}
		}
		if(F)
		{
			printf("Case #%d: %d\n",k,ret);
		}
		if(!F)
		{
			printf("Case #%d: NO\n",k);
		}
	}
	
}



































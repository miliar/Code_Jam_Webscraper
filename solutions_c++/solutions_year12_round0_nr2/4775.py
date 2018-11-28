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

int N,P,S;
bool vis[105][105];
int best[105][105],score[105];

int solve(int ind,int s)
{
	if(s>S)return -1<<28;
	if(ind==N)
	{
		if(s==S)return 0;
		return -1<<28;
	}
	
	if(vis[ind][s])return best[ind][s];
	
	int ret=-1<<28;
	
	for(int i=0;i<=10;i++)
	{
		for(int j=0;j<=10;j++)
		{
			for(int k=0;k<=10;k++)
			{
				bool f=0,a=0;
				if(abs(i-j)==2)f=1;
				if(abs(i-j)>2)continue;
				if(abs(i-k)==2)f=1;
				if(abs(i-k)>2)continue;
				if(abs(k-j)==2)f=1;
				if(abs(k-j)>2)continue;
				
				if(i>=P || j>=P || k>=P)a=1;
				
				if(i+j+k==score[ind])ret=max(ret,a+solve(ind+1,s+f));
			}
		}
	}
	vis[ind][s]=1;
	return best[ind][s]=ret;
}

int main()
{
	freopen("in.in","r",stdin);
	freopen("out.out","w",stdout);
	
	int k=0,T;
	
	scanf("%d",&T);
	
	while(T--)
	{
		clr(vis,0);
		
		scanf("%d %d %d",&N,&S,&P);
		for(int i=0;i<N;i++)
		{
			scanf("%d",&score[i]);
		}
		k++;
		printf("Case #%d: %d\n",k,solve(0,0));
	}
}




































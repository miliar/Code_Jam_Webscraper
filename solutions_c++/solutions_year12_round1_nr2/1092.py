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

int best[41][(1<<20)+1];
int s1[1005],s2[1005],N;

int solve(int stars,int mask)
{
	if(mask>=(((1<<(N*2))-1)^((1<<N)-1)))return 0;
	
	if(best[stars][mask]!=-1)return best[stars][mask];
	
	int ret=1<<30;
	
	for(int i=N*2-1;i>=0;i--)
	{
		if(i>=N && s2[i-N]<=stars && !(bool)(mask&(1<<i)))
		{
			ret=min(ret,1+solve(stars+2-(bool)(mask&(1<<(i-N))),mask|(1<<i)));
		}
		else if(i<N && s1[i]<=stars && !(bool)(mask&(1<<i))  && !(bool)(mask&(1<<(i+N))))
		{
			ret=min(ret,1+solve(stars+1,mask|(1<<i)));
		}
	}
	
	return best[stars][mask]=ret;
}

int main()
{
	freopen("in.in","r",stdin);
	freopen("out.out","w",stdout);
	
	int T,k=0;
	
	scanf("%d",&T);
	
	while(T--)
	{
		clr(best,-1);
		k++;
		
		scanf("%d",&N);
		for(int i=0;i<N;i++)
		{
			scanf("%d %d",&s1[i],&s2[i]);
		}
		
		int ret=solve(0,0);
		
		if(ret==1<<30)printf("Case #%d: Too Bad\n",k);
		else printf("Case #%d: %d\n",k,ret);
	}
	
}




































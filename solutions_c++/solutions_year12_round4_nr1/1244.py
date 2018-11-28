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

int L[10005],D[10005];
int CD[10005];

int main()
{
	freopen("in.in","r",stdin);
	freopen("out.out","w",stdout);
	
	int T,k=0;
	int N,DD;
	
	scanf("%d",&T);
	
	while(T--)
	{
		clr(CD,0);
		k++;
		scanf("%d",&N);
		
		for(int i=0;i<N;i++)
		{
			scanf("%d %d",&D[i],&L[i]);
		}
		
		scanf("%d",&DD);
		D[N]=DD;
		L[N]=1;
		N++;
		
		//printf("%d\n",N);
		/*for(int i=0;i<N;i++)printf("%d %d\n",D[i],L[i]);
		printf("%d\n",DD);
		getchar();
		getchar();*/
		
		int cur=0,next=1;
		int cd=CD[0]=D[0];
		
		printf("Case #%d: ",k);
		
		while(next<N)
		{//printf("*%d*\n",CD[cur]);
			int ocd=CD[cur];
				
				while(next<N)
				{
					if(ocd>=D[next]-D[cur])
					cd=min(D[next]-D[cur],L[next]);
					else break;
					
					CD[next]=max(CD[next],cd);
					
					next++;
				}
				cur++;
				next=cur+1;
		}
		if(CD[N-1])printf("YES\n");
		else printf("NO\n");
	}
	
}




































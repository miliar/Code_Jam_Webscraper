#pragma warning(disable:4786)
#include<iostream>
#include<cstdio>
#include<algorithm>
#include<vector>
#include<set>
#include<map>
#include<functional>
#include<string>
#include<cstring>
#include<cstdlib>
#include<queue>
#include<utility>
#include<fstream>
#include<sstream>
#include<cmath>
#include<stack>
#include<cstdio>
#include <ctime>


using namespace std;

#define MEM(a,b) memset(a,(b),sizeof(a))
#define MAX(a,b) ((a) > (b) ? (a) : (b))
#define MIN(a,b)  ((a) < (b) ? (a) : (b))
#define istr(S) istringstream sin(S)
#define MP make_pair
#define pb push_back
#define inf 1000000000
#define maxn 1000000

//typedef long long  LL;
//typedef __int64 LL;

typedef pair<int,int> pi;
typedef vector<int> vi;
typedef vector<string> vs;
typedef vector<double> vd;
typedef vector<pi> vpi;

int type[105],button[105];
int seen[105][105][105];
int dist[105][105][105],now,n;

/*
int solve()
{
	queue<int> Q;

	MEM(seen,-1);
	Q.push(1);Q.push(1);Q.push(0);
	seen[1][1]][0]=0;
	
	while(!Q.empty())
	{
		int o=Q.front();Q.pop();
		int b=Q.front();Q.pop();
		int x=Q.front();Q.pop();

		for(i=-1;i<=+1;i++)
			for(j=-1;j<=+1;j++)
			{
				if(o+i<1 || o+i>100 || b+j<1 || b+j>100) continue;

				if(seen[o+i][b+j][x]!=-1)
				{
					Q.push(o+i);Q.push(b+j);Q.push(o+i);
				}
			}
	}
	
	
	return -1;
	
}
*/

int main()
{
	int i,j,k,tests,cs=0,n;


	//freopen("E:\\GCJ\\Asmall.in","r",stdin);
	freopen("E:\\GCJ\\Alarge.out","w",stdout);

	scanf("%d",&tests);

	while(tests--)
	{

		vi A,B;
		int pa,pb,ans=0;
		int a,b;
		pa=pb=1;
		a=b=0;

		scanf("%d",&n);
		for(i=0;i<n;i++)
		{
			char tmp[5];
			scanf("%s%d",tmp,&k);
			if(tmp[0]=='O')
				A.pb(k),type[i]=0;
			else
				B.pb(k),type[i]=1;
			button[i]=k;
		}

		for(i=0;i<n;i++)
		{
			//printf("%d %d %d %d\n",i,pa,pb,ans);
			if(type[i]==0)
			{
				int t= abs(pa-button[i])+1;
				ans+=t;
				pa=button[i];
				a++;

				if(b<B.size())
				{
					int q=abs(pb-B[b]);

					if(q<=t) 
						pb=B[b];
					else
					{
						if(B[b]<pb)
							pb-=t;
						else
							pb+=t;
					}
				}
			}

			else
			{
				int t= abs(pb-button[i])+1;
				ans+=t;
				pb=button[i];
				b++;

				if(a<A.size())
				{
					int q=abs(pa-A[a]);

					if(q<=t) 
						pa=A[a];
					else
					{
						if(A[a]<pa)
							pa-=t;
						else
							pa+=t;
					}
				}
			}

		}
		printf("Case #%d: %d\n",++cs,ans);
	}

	return 0;
} 



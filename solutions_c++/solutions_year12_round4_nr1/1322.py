#include<iostream>
#include<map>
#include<math.h>
#include<vector>
#include<string>
#include<string.h>
#include<queue>
#include<algorithm>
#include<sstream>
#define all(X) (X).begin(),(X).end()
#define mem(X) memset(X,0,sizeof(X))
#define debug_v(v) for(int db=0;db<(v).size();db++)cout<<v[db]<<','<<;cout<<endl;
#define pqpush(pq,x,cmp) (pq).push_back(x);push_heap((pq).begin(),(pq).end(),cmp);
#define pqpop(pq,cmp) pop_heap((pq).begin(),(pq).end(),cmp);(pq).pop_back();
#define PB(x) push_back(x)
using namespace std;
typedef long long ll;
typedef vector<int>::iterator iv;
typedef map<string,int>::iterator msii;
typedef map<int,int>::iterator miii;
typedef map<int,bool>::iterator mibi;
typedef map<string,bool>::iterator msbi;
typedef map<string,int> msi;
typedef map<int,int> mii;
typedef map<int,bool> mib;
typedef map<string,bool> msb;
typedef vector<int> vi;
typedef vector<string> vs;



bool done[10001];
int dm[10002],lm[10002],dp[10002],D;
int t,n,h1,h2,cc,h3,h4,qa,qb,q[10000];
bool ans;


int main(){
	freopen("A-small-attempt2.in","r",stdin);
	freopen("A-small-attempt2.txt","w",stdout);
	scanf("%d",&t);
	while(t--)
	{
		scanf("%d",&n);
		dm[0]=0;
		ans=0;
		for(h1=1;h1<=n;h1++)
		{
			scanf("%d%d",&dm[h1],&lm[h1]);
		}
		scanf("%d",&dm[n+1]);
		
		mem(done);
		done[1]=1;
		dp[1]=0;
		
		
		
		for(h1=1;h1<=n;h1++)
		{
			if(done[h1])
			{
				for(h2=h1+1;h2<=n+1;h2++)
				{
					if(min(lm[h1],dm[h1]-dm[dp[h1]])+dm[h1]>=dm[h2])
						if(!done[h2]||dp[h2]>h1)
						{
							done[h2]=1;
							dp[h2]=h1;
							if(h2==n+1)ans=1;
						}
				}
			}
		}
		
		
		
		
		printf("Case #%d: %s\n",++cc,ans?"YES":"NO");
	}
}

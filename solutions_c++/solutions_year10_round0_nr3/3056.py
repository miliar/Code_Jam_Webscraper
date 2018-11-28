#include<math.h> 

#include<ctype.h>
#include<stdlib.h> 
#include<stack>
#include<queue> 
#include<list>
#include<map>

#include<string.h> 
#include<algorithm> 
#include<iostream>
#include<sstream> 
#include<vector> 
#include<string> 

using namespace std; 

#define vi vector<int>
#define vd vector<double>
#define vs vector<string>
#define fo(i,j,n) for(i=j;i<n;++i)
#define foo(i,j,v) for(i=j;i<v.size();++i)
#define li(v) v.begin(),v.end()
#define co continue;
#define re return 
#define max(a,b) ((a>b) ? a : b)

#define min(a,b) ((a<b) ? a : b)
#define max(a,b) ((a>b) ? a : b)

#define inf (1e8+1)
#define pi (2*acos(0))
#define eps 1e-9
typedef __int64 Long;
struct xx
{
	Long val,pos,Round;
};

int main()
{
	freopen("c://Codejam//C.in","r",stdin);
	freopen("c://Codejam//C.out","w",stdout);
	Long i,j,T,N,R,K,n,res=0,su; xx x; 
	queue<xx> Q; vector<Long> L,cost;
	scanf("%I64d",&T);
	fo(i,1,T+1)
	{
		while(!Q.empty())Q.pop();
		L.clear(); cost.clear(); cost.push_back(0);
		scanf("%I64d%I64d%I64d",&R,&K,&N); 
		L.resize(N,-1); res = 0;
		fo(j,0,N)
		{
			scanf("%I64d",&n); x.pos = j; x.val = n; x.Round = 0; Q.push(x); 
		}
		fo(j,1,R+1)
		{
			su = 0; x = Q.front(); n = x.pos;
			if(L[n]!=-1)
			{
				res = cost[j-1];
				res += ((R-j+1)/(j-L[x.pos]))*(cost[j-1]-cost[L[x.pos]-1]);
				n = (R-j+1)%(j-L[x.pos]); 
				n+=L[x.pos];
				n--;
				res += (cost[n]-cost[L[x.pos]-1]);
				break;
			}
			while(x.Round < j)
			{
				if(su+x.val > K)break; su += x.val; Q.pop(); x.Round = j; Q.push(x); x = Q.front();
			}
			L[n] = j; cost.push_back(su); cost[j] += cost[j-1];
		}
		if(res == 0)res = cost[R];
		printf("Case #%I64d: %I64d\n",i,res);
	}
} 


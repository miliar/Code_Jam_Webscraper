#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#define LL long long
#define MP make_pair
#define PB push_back
#define PII pair< int, int >
#define REP(i,n) for(int i=0;i<n;i++)
#define FOR(i,L,R) for(int i=L;i<=R;i++)
#define FORD(i,R,L) for(int i=R;i>=L;i--)
#define ALL(i) (i).begin(),(i).end()
#define sz(i) (int)(i).size()
#define INF 10000000
using namespace std;
int cas;
int v[3000];
LL sum[3000];
int R,N,K,g[3000];
int main()
{
	freopen("C-small-Attempt0.in","r",stdin);
	freopen("C-small.out","w",stdout);
	scanf("%d",&cas);
	int ca=0;
	while(cas--)
	{
		ca++;
		memset(v,0,sizeof(v));
		memset(sum,0,sizeof(sum));
		scanf("%d%d%d",&R,&K,&N);
		REP(i,N)
			scanf("%d",&g[i]);
		printf("Case #%d: ",ca);
		int cnt=0;
		int idx=0;
		int ad=0;
		int st,ed,xunhuan;
		while(1)
		{
			if(v[idx])
			{
				st=v[idx];
				ed=cnt;
				xunhuan=ed-st+1;
				break;
			}
			if(v[idx]==0)
			{
				v[idx]=++cnt;
				int t=(idx+1)%N;
				ad=g[idx];
				while(t!=idx&&ad+g[t]<=K)
				{
					ad+=g[t];
					t=(t+1)%N;
				}
				sum[cnt]=ad;
				ad=0;
				idx=t;
			}
		}
		LL fin=0;
		int left,chu;
		if(R<=ed)
			for(int i=1;i<=R;i++)
				fin+=sum[i];
		else
		{
			for(int i=1;i<st;i++)
				fin+=sum[i];
			 left=(R-st+1)%(xunhuan);
			 chu=(R-st+1)/xunhuan;
			LL tmp=0;
			for(int i=st;i<=ed;i++)
				tmp+=sum[i];
			fin+=chu*tmp;
			if(left)
				for(int i=st;left>0;i++,left--)
					fin+=sum[i];
			
		}
		printf("%lld\n",fin);
			
	}
//	system("pause");
	return 0;
}

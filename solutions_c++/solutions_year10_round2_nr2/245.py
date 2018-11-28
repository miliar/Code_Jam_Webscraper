#include <vector>
#include <list>
#include <map>
#include <set>
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
using namespace std;
string str;

int main()
{
	freopen("B-small-attempt0.in","r",stdin);
	freopen("B-small-attempt0.out","w",stdout);
	int cases;
	int N,K,B,T;
	bool can[100];
	int X[100],V[100];
	scanf("%d",&cases);
	for(int cas=1;cas<=cases;cas++)
	{
		int ans;
		memset(can,false,sizeof(can));
		scanf("%d%d%d%d",&N,&K,&B,&T);
		for(int i=0;i<N;i++)
			scanf("%d",&X[i]);
		for(int i=0;i<N;i++)
			scanf("%d",&V[i]);
		for(int i=0;i<N;i++)
			if(X[i]+V[i]*T>=B)
				can[i]=true;
		int cnt=0,index;
		for(int i=N-1;i>=0;i--)if(can[i])
		{
			cnt++;
			if(cnt==K){index=i;break;}
		}
		if(cnt<K)printf("Case #%d: IMPOSSIBLE\n",cas);
		else
		{
			int ans=0;
			for(int i=N-1;i>=index;i--)if(can[i])
				for(int j=N-1;j>i;j--)
					if(!can[j])ans++;
			printf("Case #%d: %d\n",cas,ans);
		}

		
	}
}
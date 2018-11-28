#include<iostream>
#include<cstring>
#include<cstdio>
#include<algorithm>

using namespace std;

int main()
{
	freopen("C-large.in","r",stdin);
	freopen("C-large.out","w",stdout);
	int t,cas = 1;
	scanf("%d",&t);
	while( t-- )
	{
		int R,k,n;
		int g[1100];
		int flag[1100] = {0};
		__int64 eur[1100] = {0};
		__int64 ans = 0;
		bool suc = false;
		scanf("%d%d%d",&R,&k,&n);
		for(int i = 0; i < n; i++)
			scanf("%d",&g[i]);
		
		int i = 1, cur = 0, cap = k, times = 0;
		flag[0] = 1;
		while( i <= R )
		{
			cap = k;
			times = 0;
			while( cap - g[cur] >= 0 && times < n)
			{
				eur[i] = eur[i] + g[cur];
				cap -= g[cur];
				times++;
				cur++;
				cur %= n;
			}
			if( flag[cur]== 0 )
			{
				flag[cur] = i+1;
			}
			else
			{
				int p = i+1 - flag[cur]; //cout << i+1 <<" "<<flag[cur]<<" " << cur <<endl;
				long long pe = 0;
				for( int j = flag[cur]; j < i+1; j++)
					pe += eur[j];
				ans = ans + (R-flag[cur]+1)/p*pe;
				for( int j = 0; j < flag[cur]; j++)
					ans += eur[j];
				for( int j = 0; j < (R-flag[cur]+1)%p; j++)
					ans += eur[flag[cur]+j];
				printf("Case #%d: %I64d\n",cas++,ans);
				suc = true;
				break;
			}
			i++;
		}
		if( suc )	continue;
		for(int j = 0; j < i; j++)
			ans += eur[j];
		printf("Case #%d: %I64d\n",cas++,ans);
	}
	return 0;
}

			
				

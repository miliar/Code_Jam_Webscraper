#include <cstdio>
#include <vector>
#include <algorithm>
#include <iostream>

int T, t;
int ans;
int M, V;
bool leaf[50];
bool type[50];
bool old[50];
bool ch  [50];
std :: vector<int> change;

int dfs(int st)
{
	if( leaf[st] == 1 )	return type[st];
	if( type[st] == 0 )	return dfs( st * 2 ) | dfs(st * 2 + 1);
						return dfs( st * 2 ) & dfs(st * 2 + 1);
}


int main()
{
	scanf("%d", &T);
	for(t = 1; t <= T; t ++)
	{
		change.clear();
		scanf("%d %d", &M, &V);
		memset(leaf, 1, sizeof(leaf));
		int i;
		for(i = 1; i <= (M - 1)/2; i ++)
		{
			leaf[i] = 0;
			scanf("%d %d", &type[i], &ch[i]);
			old[i] = type[i];
			if( ch[i] == 1 )	change.push_back(i);
		}
		for(; i <= M; i ++)
			scanf("%d", &type[i]);
		int res = 1000;
		for(int cur = 0; cur < (1 << change.size()); cur ++)
		{
			int temp = 0;
			for(int i = 0; i < change.size(); i ++)
			{
				if( cur & (1 << i) )
					type[ change[i] ] = 1;
				else
					type[ change[i] ] = 0;
				if( type[ change[i] ] != old[ change[i] ] )
					temp ++;
			}
			if( temp > res )	continue;
			if( dfs(1) == V )
				if( temp < res )
					res = temp;
		}
		if( res != 1000 )
			printf("Case #%d: %d\n", t, res);
		else
			printf("Case #%d: IMPOSSIBLE\n", t);
	}
    return 0;
}

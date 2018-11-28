#define _CRT_SECURE_NO_DEPRECATE
#include <cstdio>
#include <cstdlib>
#include <algorithm>
using namespace std;
#define MAXS 100
#define MAXQ 1000


int main()
{
	freopen("A-large.in", "rt", stdin);
	freopen("A-large.out", "wt", stdout);
	int N, k;
	scanf("%d", &N);
	for(k = 0 ; k < N ; ++k)
	{
		int i, j;
		int S, Q;
		char tursa4ki[MAXS + 1][101] = {0};
		int vuprosi[MAXQ + 1] = {0};
		scanf("%d\n", &S);
		for(i = 0 ; i < S ; ++i)
			gets(tursa4ki[i]);
		scanf("%d\n", &Q);
		for(i = 0 ; i < Q ; ++i)
		{
			char buff[101];
			gets(buff);
			for(j = 0 ; j < S ; ++j)
				if(strcmp(buff, tursa4ki[j]) == 0)
				{
					vuprosi[i] = j;
					break;
				}
		}
		int c = 0, last = 0;
		bool active[MAXS] = {0};
		int ans = 0;
		while(true){
		for(i = last ; i < Q && c < S; ++i)
		{
			if(!active[vuprosi[i]])
			{
				active[vuprosi[i]] = true;
				c++;
			}
			if(c == S)break;
		}
		if(i >= Q)break;
		for(j = 0 ; j < MAXS ; ++j)active[j] = false;
		ans++;
		c = 0;
		last = i;
		}
		printf("Case #%d: %d\n", k + 1, ans);
	}
	return 0;
}



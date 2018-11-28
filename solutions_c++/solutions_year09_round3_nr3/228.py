#include <cstdio>
#include <climits>
#include <algorithm>

const int MAX_Q = 5 + 2;
const int MAX_P = 100 + 5;

int T;
int P, Q;
int a[MAX_Q];
bool used[MAX_P];
int main()
{
	scanf("%d", &T);
	for(int t = 0; t < T; t ++)
	{
		scanf("%d %d", &P, &Q);
		for(int i = 0; i < Q; i ++)	scanf("%d", &a[i]);
		std :: sort(a, a + Q);
		int res = INT_MAX;
		do
		{
			int cur = 0;
			memset(used, 1, sizeof(used));
			for(int i = 0; i < Q; i ++)
			{
				used[ a[i] ] = 0;
				int pos = a[i] - 1;
				while( 1 )
				{
					if( pos == 0 || used[pos] == 0 )
						break;
					cur ++;
					pos --;
				}
				pos = a[i] + 1;
				while(1)
				{
					if(pos == P + 1 || used[pos] == 0)
						break;
					cur ++;
					pos ++;
				}
			}
			if(cur < res)	res = cur;
		}
		while(std :: next_permutation(a, a + Q));
		printf("Case #%d: %d\n", t + 1, res);
	}
    return 0;
}

#include <cstdio>
#include <mem.h>
#include <cstdlib>
#include <vector>

#define f(i, n)                         for(int i = 0; i < int(n); i ++)
#define ff(i, st, end)                  for(int i = int(st); i < int(end); i ++)
#define fx(it, v)                       for( typeof( (v).begin() ) it = (v).begin(); it != (v).end; it ++ )
#define fv(i, v)                        for(int i = 0; i < (int)(v).size(); i ++)
#define all(v)                          (v).begin(), (v).end()

int T, t;
int ans;
int n;
int K;
int d[105];
int num[5005];
std :: vector<int> av;

int main()
{
	scanf("%d", &T);
	for(t = 1; t <= T; t ++)
	{
		av.clear();
		scanf("%d", &K);
		scanf("%d", &n);
		for(int i = 0; i < n; i ++)	{ scanf("%d", &d[i]); d[i] --;}
		
		for(int i = 0; i < K; i ++)	av.push_back( i );
		
		int cur = 0;
		int pos = 0;
		
//		memset(used, 0, sizeof(used));
		
		while( cur < K )
		{
			
			
			
			int left = cur;
//			printf("cur: %d\n", cur);
//			for( ; left > 0; )	if( !used[pos % K] )pos ++, left --;
/*			while( left > 0 )
			{
				left --;
				pos ++; pos %= av.size();
//				printf("left: %d pos: %d, %d\n", left, pos, av[pos]);
//				system("pause");
//				if( used[pos] == 0 )
//				{
//					printf("in\n");
//					left --;
//					if(left == 0)	break;
//				}
//				pos ++; pos %=K;
			} */
//			while( used[pos] == 1 ){ pos ++; if(pos == K) pos = 0; }
			
			pos += left; pos %= av.size();
			num[ av[pos] ] = cur;
//			printf("cur %d is on pos %d\n", cur, av[pos]);
			av.erase( av.begin() + pos );
//			used[pos] = 1;
//			pos ++;

			if(av.size())pos %= av.size();
			cur ++;
		}
		
		printf("Case #%d: ", t);
		for(int i = 0; i + 1 < n; i ++)
			printf("%d ", num[ d[i] ] + 1);
		printf("%d\n", num[d[n - 1]] + 1);
	}
    return 0;
}

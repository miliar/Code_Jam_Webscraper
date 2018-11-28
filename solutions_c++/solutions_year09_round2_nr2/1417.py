#include <cstdio>
#include <cstring>

const int MAX_LEN = 20 + 5;

int T;
int N;
char s[MAX_LEN];
int cnt[10], cur[10];
int main()
{
    scanf("%d", &T);
    for(int t = 0; t < T; t ++)
    {
		scanf("%d", &N);
		sprintf(s, "%d", N);
		memset(cnt, 0, sizeof(cnt));
		for(int i = 0; s[i]; i ++)	cnt[s[i] - '0'] ++;
		int n;
		for(n = N + 1; ; n ++)
		{
			sprintf(s, "%d", n);
			memset(cur, 0, sizeof(cur));
			for(int i = 0; s[i]; i ++)
				cur[s[i] - '0'] ++;
			bool ok = 1;
			for(int i = 1; i < 10; i ++)
				if( cur[i] != cnt[i] )
				{
					ok = 0;
					break;
				}
			if(ok)	break;
		}
		printf("Case #%d: %d\n", t + 1, n);
    }
    return 0;
}

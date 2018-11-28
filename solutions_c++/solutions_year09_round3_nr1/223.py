#include <cstdio>
#include <cstring>
#include <iostream>

const int MAX_N = 64;

int T;
char s[MAX_N];
bool used[256];
int sub[256];
int main()
{
	scanf("%d\n", &T);
	for(int t = 0; t < T; t ++)
	{
		gets(s);
		memset(used, 0, sizeof(used));
		long long base = 0;
		for(int i = 0; s[i]; i ++)
			if( !used[s[i]] )
				base ++, used[s[i]] = 1;
		if(base == 1)	base ++;
		memset(used, 0, sizeof(used));
		memset(sub, -1, sizeof(sub));
		sub[s[0]] = 1;
		used[1] = 1;
		int next = 2;
		for(int i = 1; s[i]; i ++)
		{
			if( sub[s[i]] == -1 )
				if(!used[0])
				{
					sub[s[i]] = 0;
					used[ 0 ] = 1;
				}
				else
				{
					sub[s[i]] = next;
					used[ next ++ ] = 1;
				}
		}
		long long mply = 1;
		long long res = 0;
		for(int i = strlen(s) - 1; i >= 0; i --)
		{
			res += sub[s[i]] * mply;
			mply *= base;
		}
//		printf("Case #%d: %I64d\n", t + 1, res);
		std :: cout << "Case #" << t + 1 << ": " << res << "\n";
	}
    return 0;
}

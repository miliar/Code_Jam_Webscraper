#include <cstdio>
#include <iostream>

#define f(i, n)                         for(int i = 0; i < int(n); i ++)

int T, t;
int m[6];
int ans;
int main()
{
	scanf("%d", &T);
	for(t = 1; t <= T; t ++)
	{
		int k;
		std :: string s, cur;
		std :: cin >> k >> s;
		int res = s.size();
		f(i, k)	m[i] = i;
		int times = s.size() / k;
		do
		{
			cur = "";
			f(i, times)
				f(j, k)
					cur += s[ i*k + m[j] ];
//			std :: cout << cur << "\n";
			int sz = 1;
			for(int i = 1; i < cur.size(); i ++)
				if( cur[i] != cur[i - 1] )
					sz ++;
			if( sz < res )	res = sz;
		}
		while( std :: next_permutation(m, m + k) );
		printf("Case #%d: %d\n", t, res);
	}
    return 0;
}

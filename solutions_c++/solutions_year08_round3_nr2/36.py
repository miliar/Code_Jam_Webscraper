#include <cstdio>
#include <cstring>
#include <math.h>
#include <vector>
#include <algorithm>
#include <list>
#include <string>
#include <map>
#include <cassert>

using namespace std;

const int M(210);
const int NMAX(50);

__int64 cc[NMAX][M];
char str[NMAX];

int strmod(int s, int t)
{
	int ret = 0;
	while( s<=t )
	{
		ret *= 10;
		ret += str[s]-'0';
		ret %= M;
		s ++;
	}
	return ret;
}

int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int N;
	scanf("%d", &N);
	for( int nCase=1; nCase<=N; nCase++ )
	{
		scanf("%s", str);
		memset(cc, 0, sizeof(cc));
		cc[0][0] = 1;
		int len = strlen(str);
        for( int i=1; i<=len; i++ )
		{
			for( int j=0; j<i; j++ )
			{
				int rem = strmod(j, i-1);
				for( int k=0; k<M; k++ )
				{
					cc[i][(k+rem)%M] += cc[j][k];
					if( j!=0 )
					{
						cc[i][(k+M-rem)%M] += cc[j][k];
					}
				}
			}
		}
		__int64 rsl = 0;
		for( int i=0; i<M; i++ )
		{
			if( i%2==0 || i%3==0 || i%5==0 || i%7==0 )
			{
				rsl += cc[len][i];
			}
		}
		printf("Case #%d: %I64d\n", nCase, rsl);
	}
	return 0;
}

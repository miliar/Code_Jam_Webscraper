#include <cstdio>
#include <cstring>
#include <string>
#include <vector>
#include <cassert>
#include <map>
#include <set>
#include <list>
#include <bitset>
#include <algorithm>
#include <math.h>

using namespace std;

typedef __int64 int64;

#define SUBMIT

int main()
{
	freopen("in.txt", "r", stdin);

#ifdef SUBMIT
	freopen("ans.txt", "w", stdout);
#endif

	int totCase;
	scanf("%d", &totCase);
	for( int nCase=1; nCase<=totCase; nCase++ )
	{
		printf("Case #%d: ", nCase);
		int k;
		char str[1024];
		scanf("%d%s", &k, str);
		int perm[5];
		for( int i=0; i<k; i++ )
		{
			perm[i] = i;
		}
		int best = -1;
		do
		{
			char temp[1024];
			int len = strlen(str);
			for( int i=0; i<len; i+=k )
			{
				for( int j=0; j<k; j++ )
				{
					temp[i+j] = str[i+perm[j]];
				}
			}
			int cc = 0;
			for( int i=0; i<len; i++ )
			{
				if( i==0 || temp[i]!=temp[i-1] )
				{
					cc ++;
				}
			}
			if( best==-1 || cc<best )
			{
				best = cc;
			}
		}
		while( next_permutation(perm, perm+k) );
		printf("%d\n", best);
	}
	return 0;
}

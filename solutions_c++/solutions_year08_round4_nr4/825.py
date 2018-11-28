#include <cstdio>
#include <algorithm>
#include <cstring>
using namespace std;

char s[65536];
char q[65536];
int main()
{
	int t;
	scanf("%d",&t);

	for(int z=1;z<=t;z++)
	{
		int k;
		scanf("%d\n%s",&k,	s);
		int l = strlen(s);
		int perm[16] = {0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15};
		int best = l;
		do
		{
			for(int i=0;i<l;i+=k)
				for(int j=0;j<k;j++)
					q[i+perm[j]] = s[i+j];
				
			int cnt = 1;
			for(int i=1;i<l;i++)
				if(q[i]!=q[i-1])
					cnt++;

			if( cnt < best)
				best = cnt;
		} while( next_permutation(perm, perm + k) );

		printf("Case #%d: %d\n", z, best);
	}
	return 0;
}

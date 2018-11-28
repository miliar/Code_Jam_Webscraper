#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cstring>
using namespace std;

char	s[10000];
int	len;

int	perm[10];
char	p[10000];
int	k;

void  apply()
{
	int	i,j;

	for(i = 0; i < len; i += k)
	{
		for(j = 0; j < k; j++)
			p[i + j] = s[i + perm[j]];
	}
}

int main()
{
	int	N,cs;
	int	i;

	scanf("%d",&N);
	
	for(cs = 1; cs <= N; cs++)
	{
		scanf("%d",&k);
		scanf("%s",s);

		len = strlen(s);

		for(i = 0; i < k; i++) perm[i] = i;

		int cm = len;

		do
		{
			apply();
			int	c = 0;

			for(i = 0; i < len; i++)
			{
				if(i == 0 || p[i] != p[i - 1])
					c++;
			}

			cm = min(cm,c);
		} while(next_permutation(perm,perm + k));
	
		printf("Case #%d: %d\n",cs,cm);
	}

	return 0;
}

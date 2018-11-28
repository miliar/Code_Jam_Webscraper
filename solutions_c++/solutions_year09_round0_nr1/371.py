#include "iostream"
#include "string"
#include "algorithm"
#include "vector"
using namespace std;

#define MAX 5010

char dict[MAX][20];
int L, D, N;

char pattern[1024];

bool re[MAX];

int deal()
{
	int i, j, k;

	memset(re, 1, sizeof(re));

	int digit=-1;
	for(i=0; pattern[i];)
	{
		if(pattern[i]=='(')
		{
			++i;
			for(j=i+1; islower(pattern[j]); ++j);
		}
		else if(islower(pattern[i]))
		{
			j=i+1;
		}
		else
		{
			++i;
			continue;
		}
		++digit;
		for(k=1; k<=D; ++k)
			if(re[k])
			{
				int t;
				for(t=i; t<j; ++t)
					if(dict[k][digit]==pattern[t]) break;
				if(t>=j)
					re[k]=false;					
			}
		i=j;
	}

	k=0;
	for(j=1; j<=D; ++j)
		if(re[j])
			++k;
	return k;
}

void wuming()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
}

int main()
{
	wuming();

	int i, j, k;

	scanf("%d%d%d", &L, &D, &N);
	for(i=1; i<=D; ++i)
		scanf("%s", dict[i]);

	int test=0;
	while(N--)
	{
		scanf("%s", pattern);

		printf("Case #%d: %d\n", ++test, deal());
		
	}


	return 0;
}
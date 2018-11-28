#include <stdio.h>
#include <string.h>


int s;
int q;
int arr[1024];
int opt[1024][1024];

void Read()
{
	int i;
	int j;

	char sstmp[1024];
	char **ss = new char* [1024];
	for(i=0; i<1024; i++)
		ss[i] = new char[102];
    
    scanf("%d", &s);
    gets(sstmp);
	for (i=0; i<s; i++)
		gets(ss[i]);
	scanf("%d", &q);
    gets(sstmp);
	for (i=0; i<q; i++)
	{
		gets(sstmp);
		for(j=0; j<s; j++)
			if(strcmp(sstmp, ss[j]) == 0)
			{
				arr[i] = j;
				break;
			}
	}
}

int Solve()
{
	int i;
	int j;
	int k;

	for (j=0; j<s; j++)
		opt[0][j] = 0;
	opt[0][arr[0]] = 999999;

	for (i=1; i<q; i++)
	{
		for (j=0; j<s; j++)
		{
			if (j == arr[i])
			{
				opt[i][j] = 999999;
			}
			else
			{
				opt[i][j] = opt[i-1][j];
				for (k=0; k<s; k++)
					if (opt[i][j] > opt[i-1][k]+1)
						opt[i][j] = opt[i-1][k]+1;
			}
		}
	}

	int ans = 999999;
	for (j=0; j<s; j++)
		if (ans > opt[q-1][j])
			ans = opt[q-1][j];
	
	/*for (i=0; i<q; i++)
	{
		for (j=0; j<s; j++)
			printf("%d ", opt[i][j]);
		puts("");
	}*/
	
	return ans;
}

int main()
{
	freopen("uni.in", "rt", stdin);
	freopen("uni.out", "wt", stdout);

	int n;

	scanf("%d", &n);
	for (int i=0; i<n; i++)
	{
		Read();
		printf("Case #%d: %d\n", i+1, Solve());
	}

	return 0;
}

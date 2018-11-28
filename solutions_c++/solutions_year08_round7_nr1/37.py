#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#define max(a,b) ((a)>(b)?(a):(b))

int n;
char m[2000][21];

int find(char *str)
{
	int i;

	for (i=0; i<n; i++)
		if (strcmp(str,m[i]) == 0) break;

	if (i==n)
		strcpy(m[n++], str);

	return i;
}

int e[2000][2000];

int chk(const void *a, const void *b)
{
	int aa = *(int *)a;
	int bb = *(int *)b;

	return bb-aa;
}

int findcnt(int node)
{
	int t[20]; int s=0;
	int bst=0;
	int cnt=1; // if recipe? which it will be if not leaf
	for (int i=0; i<n; i++)
	{
		if (e[node][i])
		{
			if (m[i][0] >= 'A' && m[i][0] <= 'Z')
			{
				t[s++] = findcnt(i);
				cnt++;
			}
			//printf("node %s -> %s", m[node], m[i]);
		}
	}

	qsort(t,s, sizeof(int), chk);

	for (int i=0; i<s; i++)
	{
		//printf("t[%d] %d\n", i, t[i]);
		bst=max(bst, i+t[i]);
	}

	//printf("%d %d %d\n", node, bst, cnt);
	return max(bst, cnt);
}
int main()
{
	int i,bst,j,N,nodes,k;
	char str[40];

	scanf("%d", &N);

	for (int cs=1; cs<=N; cs++)
	{
		n=0;
		
		memset(e, 0, sizeof(e));
		scanf("%d", &nodes);
		//printf("num nodes %d\n", nodes);
		for (i=0;i<nodes;i++)
		{
			scanf("%s %d", str, &k);
			//printf("read %s %d\n", str, k);
			int item =  find(str);
			for (j=0;j<k;j++)
			{
				scanf("%s", str);
				int item2 = find(str);

				//printf("connecting %d %d\n", item, item2);
				e[item][item2] = 1;
			}
		}

		bst = findcnt(0);
		printf("Case #%d: %d\n", cs, bst);
	}
	return 0;
}

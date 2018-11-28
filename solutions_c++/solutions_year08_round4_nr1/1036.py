#include<stdio.h>
#include<math.h>
#include<stdlib.h>
#include<string.h>
#include<ctype.h>

#define SZ 10001

typedef struct  
{
	int g;
	int c;
}node;

long minCng, cnt;
int op[SZ];
int res[SZ];
node nodes[SZ];
long intern, leaf, m, v;

void recur(int ind);
int toogle(int a);
int getResult(void);
int AND(int a, int b);
int OR(int a, int b);

int main()
{
	//freopen("input.in","rt",stdin);
	freopen("A-small.in","rt",stdin);
	freopen("A-small.txt","wt",stdout);
	//freopen("A-large.in","rt",stdin);
	//freopen("A-large.txt","wt",stdout);
	long kase, i, j, t;
	
	scanf("%d", &t);
	for(kase = 1; kase <= t; kase++)
	{
		printf("Case #%d: ",kase);
		scanf("%ld %ld", &m, &v);
		minCng = m + 1;
		intern = (m - 1) / 2;
		leaf = (m + 1) / 2;
		for(i = 0; i < intern; i++)
			scanf("%ld %ld" , &nodes[i].g, &nodes[i].c);
		for(i = intern, j = 0; j < leaf; i++, j++)
			scanf("%ld" , &res[i]);
		cnt = 0;
		recur(0);
		if(minCng == m + 1)
			printf("IMPOSSIBLE\n");
		else
			printf("%ld\n", minCng);
	}
	return 0;
}

void recur(int ind)
{
	if(ind == intern)
	{
		if(getResult() == v)
		{
			if(minCng > cnt)
				minCng = cnt;
		}
	}
	else
	{
		op[ind] = nodes[ind].g;
		recur(ind + 1);
		if(nodes[ind].c)
		{			
			op[ind] = toogle(nodes[ind].g);
			cnt++;
			recur(ind + 1);
			cnt--;
		}
	}
	
}

int toogle(int a)
{
	if(a == 0)
		return 1;
	return 0;
}

int getResult(void)
{
	for(int i = intern - 1; i >= 0; i--)
	{
		if(op[i] == 1)
			res[i] = AND(res[(i + 1) * 2 - 1], res[(i + 1) * 2]);
		else
			res[i] = OR(res[(i + 1) * 2 - 1], res[(i + 1) * 2]);
	}
	return res[0];
}

int AND(int a, int b)
{
	if(a == 1 && b == 1)
		return 1;
	else
		return 0;
}
int OR(int a, int b)
{
	if(a == 0 && b == 0)
		return 0;
	else
		return 1;
}
#include <iostream>
#include <cmath>
#include <string>
#include <vector>
#include <list>
#include <algorithm>
#include <cstdio>
#include <cstring>
#include <map>

using namespace std;

#ifndef ONLINE_JUDGE
int poj();
int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	poj();
	return 0;
}
#define main poj
#endif

#define clr(x) memset(x, 0, sizeof(x))
#define MAXINT 200000000
#define EPS 0.00000001
#define MAXN 300

struct node
{
	char fea[81];
	double p;
	node *next[2];
};

bool dfs(node *&p, double myp, bool start = 1)
{
	char buf[100];
	int now = 0, time;
	bool kuo;
	//printf("################\n");
	p = new node;
	p->next[0] = 0;
	p->next[1] = 0;
	p->fea[0] = '\0';
	p->p = myp;
	
	time = 20;
	kuo = 0;
	while (start)
	{
		scanf("%s", buf);
		//printf("%s\n", buf);
		if (buf[0] == '(')
		{
			if (strlen(buf) == 1) scanf("%lf", &myp);
			else sscanf(buf, "(%lf", &myp);
			//printf("now:%d\n", now);
			
			if (buf[strlen(buf) - 1] == ')')
			{
				dfs(p->next[now++], myp, 0);
				continue;
			}
			
			if (dfs(p->next[now++], myp)) return 0;
		}
		else if (buf[0] == ')')
		{
			if (strlen(buf) > 1 && buf[strlen(buf) - 2] == ')') return 1;
			else return 0;
		}
		else
		{
			sscanf(buf, "%s", p->fea);
		}
	}
	
	return 0;
}

char data[200][200];
double result;
int n;

void make(node *now)
{
	int i;
	if (now == NULL) return;
	
	result *= now->p;
	
	for (i = 0; i < n; i++)
		if (strcmp(data[i], now->fea) == 0)
		{
			make(now->next[0]);
			break;
		}
	
	if (i == n)
		make(now->next[1]);
}

int main()
{
	double a;
	node *root;
	int tcase, tno, i, j, l, ani;
	char buf[100];
	
	scanf("%d", &tcase);
	for (tno = 1; tno <= tcase; tno++)
	{
		scanf("%d\n", &l);
		
		scanf("(%lf", &a);
		dfs(root, a);
		//return 0;
		scanf("%d", &ani);
		printf("Case #%d:\n", tno);
		for (i = 0; i < ani; i++)
		{
			scanf("%s%d", buf, &n);
			for (j = 0; j < n; j++)
				scanf("%s", data[j]);
			result = 1;
			make(root);
			printf("%.7lf\n", result);	
		}
	}
	
	return 0;
}

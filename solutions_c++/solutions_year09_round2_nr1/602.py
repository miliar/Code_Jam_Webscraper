#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <ctype.h>

char s[100001] , str[101], *pos;

struct tree
{
	double p;
	char s[21];
	bool leaf;
}p[100001];

void create(int id)
{
	while (!isdigit(*pos)) pos ++;
	double pi = *pos - '0' , ten = 1;
	if (*(pos + 1) == '.')
	{
		pos += 2;
		while (isdigit(*pos))
		{
			ten /= 10;
			pi += (*pos - '0') * ten;
			pos ++;
		}
	}
	p[id].p = pi;
	while (!isalpha(*pos) && *pos != ')')
	{
		pos ++;
	}
	if (*pos == ')')
	{
		p[id].leaf = 1;
	}
	else
	{
		p[id].leaf = 0;
		char *ps = p[id].s;
		while (isalpha(*pos))
		{
			*ps = *pos;
			ps ++;
			pos ++;
		}
		*ps = 0;
		create(id << 1);
		create(1 + (id << 1));
		while (*pos != ')') pos ++;
		pos ++;
	}
	
}

char save[101][21];
int num;
double ans;


void search(int id)
{
	ans *= p[id].p;
	if (p[id].leaf == 1)
		return;
	int i;
	bool flag = 0;
	for (i = 0;i < num;i ++)
	{
		if (strcmp(p[id].s , save[i]) == 0)
		{
			flag = 1;
			break;
		}
	}
	if (flag)
	{
		search(id << 1);
	}
	else
	{
		search(1 + (id << 1));
	}
}
int main()
{
	int i , j , t , cas , l , m;
	freopen("F:\\A-small-attempt0.in" , "r" , stdin);
	freopen("F:\\A-small-attempt0.out" , "w" , stdout);
	scanf("%d" , &t);
	for (cas = 1;cas <= t;cas ++)
	{
		scanf("%d" , &l);
		getchar();
		s[0] = 0;
		for (i = 0;i < l;i ++)
		{
			gets(str);
			strcat(s , str);
		}
		pos = s;
		create(1);
		scanf("%d" , &m);
		printf("Case #%d:\n" , cas);
		while (m --)
		{
			scanf("%s%d" , str , &num);
			for (i = 0;i < num;i ++)
			{
				scanf("%s" , save[i]);
			}
			ans = 1;
			search(1);
			
			printf("%.7lf\n", ans);
		}
	}

	return 0;
}
#include <stdio.h>
#include <string.h>
#include <math.h>
#include <algorithm>
using  namespace std;

const  int MAXN = 1000;
int  L, A, n;
char  ts[MAXN*100];

struct  Node
{
	char  s[100];
	double  v;
	int  son[2];
}dt[MAXN];
int  dlen; 
double get_num(int  &p)
{
	double ret = 0;
	while(!(ts[p] >= '0' && ts[p] <= '9')) p++;
	while(ts[p] >= '0' && ts[p] <= '9')
	{
		ret = ts[p]-'0';
		p++;
	}
	if(ts[p] == '.')
	{
		double  power = 10;
		p++;
		while(ts[p] >= '0' && ts[p] <= '9')
		{
			ret += (ts[p]-'0')/power;
			power *= 10;
			p++;
		}
	}
	return  ret;
}

void  get_string(char *s, int &p)
{
	int i = 0;
	while(ts[p] == ' ') p++;
	while(ts[p] >= 'a' && ts[p] <= 'z')
	{
		s[i++] = ts[p];
		p++;
	}
	s[i] = '\0';
}

int  DFS(int  p, int father, int tag)
{

	int  tp;
	while(ts[p] == ' ') p++;
	if(ts[p] == '\0') return p;
	if(ts[p] == '(')
	{
		p++;
		dt[dlen].v = get_num(p);
		if(father >= 0)
		{
			dt[father].son[tag] = dlen;
		}
		int  tmp = dlen;
		dlen++;
		while(ts[p] == ' ') p++;
		if(ts[p] == ')' || ts[p] == '\0') return  p+1;
		get_string(dt[tmp].s, p);
		while(ts[p] != '(') p++;
		tp = DFS(p, tmp, 0);	
		tp = DFS(tp, tmp, 1);
		while(ts[tp] != ')') tp++;
	}
	return  tp+1;
}

void  Init()
{
	int  i;
	ts[0] = '\0';
	int len = strlen(ts);
	scanf("%d", &L);
	gets(ts);
	for(i = 0; i < L; i++)
	{
		gets(ts+len);
		len = strlen(ts);
	}
	memset(dt, 0, sizeof(dt));
	dlen = 1;
}
int  main()
{
	int  T, CAS = 1;
	int  i;
	char  ani[150][150];
	//freopen("A2.in", "r", stdin);
	//freopen("A2.out", "w", stdout);
	scanf("%d", &T);
	while(T--)
	{
		Init();
		
		DFS(0, -1, 0);
		scanf("%d", &A);
		printf("Case #%d:\n", CAS++);
		while(A--)
		{
			scanf("%s %d", ani, &n);
			int  cur = 1;
			double  ans = dt[cur].v;
			for(i = 0; i < n; i++)
				scanf("%s", ani[i]);
			while(dt[cur].son[0] != 0)
			{
				for(i = 0; i < n; i++)
				{
					if(strcmp(ani[i], dt[cur].s) == 0)
						break;
				}
				if(i != n)
					cur = dt[cur].son[0];
				else  cur = dt[cur].son[1];
					ans *= dt[cur].v;
				if(dt[cur].son[0] == 0) break;
			}
			printf("%.7lf\n", ans);
		}
	}
	return  0;
}

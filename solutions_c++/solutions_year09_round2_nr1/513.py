#include <iostream>
using namespace std;

struct Tree
{
	double t;
	char s[20];
	int l, r;
}a[1000];
int la;
bool isSmall(const char &c)
{
	return c >= 'a' && c <= 'z';
}

void read(int Temp)
{
	a[Temp].s[0] = 0;
	char c;
	while( scanf("%c", &c)!=EOF )
		if( c == '(' )break;

	scanf("%lf", &a[Temp].t);
	
	while( scanf("%c", &c)!=EOF )
	{
		if( isSmall(c) )
		{
			int i = 1;
			a[Temp].s[0] = c;
			for( ; ;i++)
			{
				scanf("%c", &a[Temp].s[i]);
				if( !isSmall(a[Temp].s[i]) )
				{
					a[Temp].s[i] = 0;
					la++;
					a[Temp].l = la;
					read(a[Temp].l);
					la++;
					a[Temp].r = la;
					read(a[Temp].r);
					break;
				}
			}
		}
		else if( c == ')' )
		{
			if(a[Temp].s[0] == 0) a[Temp].r = a[Temp].l = -1;
			break;
		}
	}
}

char str[200][100];
int n;
double out;

void dfs(int Temp)
{
	if(Temp == -1) return;
	out *= a[Temp].t;
	if( a[Temp].s[0] == 0 ) return ;
	for(int i=0; i<n; i++)
		if(strcmp(str[i], a[Temp].s) == 0)
		{
			dfs(a[Temp].l);
			return ;
		}
	dfs(a[Temp].r);
}



int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int T, C;
	int line;
	scanf("%d", &T);
	int i, CA;
	char s[20];
	for(C=1; C<=T; C++)
	{
		scanf("%d", &line);
		la = 0;
		read(0);

		scanf("%d", &CA);
		printf("Case #%d:\n", C);
		while(CA--)
		{
			scanf("%s", s);
			scanf("%d", &n);
			for(i=0; i<n; i++)
				scanf("%s", str[i]);

			out = 1;
			dfs(0);
			printf("%.7lf\n", out);
		}
	}
	return 0;
}
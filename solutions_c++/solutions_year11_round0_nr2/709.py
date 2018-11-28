#include <cstdio>
#include <cstring>

using namespace std;

char c[255][255];
int o[255][255];
int v[255];

char s[5];

char stk[102];
char inv[102];

int p;

char top()
{
	return stk[p-1];
}

void pop()
{
	v[top()]--;
	p--;
}

void push(char t1)
{
	if (p == 0) {
		v[t1]++;
		stk[p++] = t1;
		return;
	}
	char t2 = top();
	v[t1]++;
	stk[p++] = t1;
	if (c[t1][t2] != 0)
	{
		pop(); pop();
		push(c[t1][t2]);
	} else {
		for (char i='A'; i<='Z'; i++)
		{
			if (o[t1][i] == 1 && v[i] != 0)
			{
				p = 0;
				memset(v, 0, sizeof(v));
				return;
			}
		}
	}
}
	

int main ()
{
	int n;
	scanf("%d", &n);
	for (int i=1; i<=n; i++)
	{
		p = 0;
		memset(c, 0, sizeof(c));
		memset(o, 0, sizeof(o));
		memset(v, 0, sizeof(v));
		
		int t;
		
		scanf("%d", &t);
		for (int j=0; j<t; j++)
		{
			scanf("%s", s);
			c[s[0]][s[1]] = s[2];
			c[s[1]][s[0]] = s[2];
		}
		
		scanf("%d", &t);
		for (int j=0; j<t; j++)
		{
			scanf("%s", s);
			o[s[0]][s[1]] = 1;
			o[s[1]][s[0]] = 1;
		}
		
		scanf("%d", &t);
		scanf("%s", inv);
		
		for (int j=0; j<t; j++)
		{
			push(inv[j]);
		}
		
		printf("Case #%d: [", i);
		for (int j=0; j<p; j++)
		{
			if (j != 0) printf(", ");
			printf("%c", stk[j]);
		}
		printf("]\n");
	}
	return 0;
}
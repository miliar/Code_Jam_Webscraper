#include <cstdio>
#include <algorithm>
using namespace std;

int C,D,n,top;
char c[33][33];
bool d[33][33];
char s[111];
int st[111];

void test()
{
	for(int i = 0; i < 26; i++) for(int j = 0; j < 26; j++)
		c[i][j] = d[i][j] = 0;
	scanf("%d", &C);
	for(int i = 0; i < C; i++)
	{
		scanf("%s", s);
		c[s[0]-'A'][s[1]-'A'] = s[2]-'A';
		c[s[1]-'A'][s[0]-'A'] = s[2]-'A';
	}
	scanf("%d", &D);
	for(int i = 0; i < D; i++)
	{
		scanf("%s", s);
		d[s[0]-'A'][s[1]-'A'] = 1;
		d[s[1]-'A'][s[0]-'A'] = 1;
	}
	scanf("%d%s", &n, s);
	top = -1;
	for(int i = 0; i < n; i++)
	{
		char q = s[i]-'A';
		while(top >= 0 && c[q][st[top]])
		{
			top--;
			q = c[q][st[top+1]];
		}
		bool fnd = 0;
		for(int j = 0; j <= top; j++) if(d[q][st[j]]) top = -1, fnd = 1;
		if(!fnd) st[++top] = q;
	}
	printf("[");
	for(int i = 0; i <= top; i++)
		if(i == top) printf("%c", 'A'+st[i]);
		else printf("%c, ", 'A'+st[i]);
	printf("]\n");
}

int main()
{
	int tt;
	scanf("%d", &tt);
	for(int i = 1; i <= tt; i++)
	{
		printf("Case #%d: ", i);
		test();
	}
}

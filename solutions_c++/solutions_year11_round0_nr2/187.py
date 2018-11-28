#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include<algorithm>
#include<map>
using namespace std;

int c, d;
char co[100][10];
char op[100][10]; 
char s[1000], list[1000];
map<int, char> m;
int ct[300];
int cnt;

bool combine()
{
	if (cnt < 2)return false;
	char a = list[cnt - 2], b = list[cnt - 1];
	if (a > b)swap(a, b);
	if (m.find(a * 128 + b) != m.end())
	{
		char rep = m[a * 128 + b];
		list[cnt - 2] = rep;
		list[cnt - 1] = 0;
		--cnt;
		ct[a]--;
		ct[b]--;
		ct[rep]++;
		return true;
	}
	return false;
}

void oppose()
{
	for (int i = 0; i < d; i++)
	{
		if (ct[op[i][0]] && ct[op[i][1]])
		{
			cnt = 0;
			memset(ct, 0, sizeof(ct));
			return;
		}
	}
}

int solve()
{
	m.clear();
	memset(ct, 0, sizeof(ct));
	cnt = 0;
	
	scanf("%d", &c);
	for (int i = 0; i < c; i++)
	{
		scanf("%s", co[i]);
		if (co[i][0] > co[i][1])swap(co[i][0], co[i][1]);
		m[co[i][0] * 128 + co[i][1]] = co[i][2];
	}

	scanf("%d", &d);
	for (int i = 0; i < d; i++)
	{
		scanf("%s", op[i]);
	}
		
	scanf("%*d%s", s);
	
	for (int i = 0; s[i]; i++)
	{
		list[cnt++] = s[i];
		ct[s[i]]++;
		while (combine());
		oppose();
//		printf("        %s\n", list);
	}
	list[cnt] = 0;
	printf("[");
	for (int i = 0; list[i]; i++)
	{
		printf("%c", list[i]);
		if (list[i + 1])printf(", ");
	}
	printf("]\n");
}


int main()
{
	int tc;
	scanf("%d", &tc);
	for (int i = 1; i <= tc; i++)
	{
		printf("Case #%d: ", i);
		solve();
	}
	return 0;
}

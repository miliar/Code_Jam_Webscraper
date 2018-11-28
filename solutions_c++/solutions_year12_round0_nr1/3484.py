#include <cstdio>
using namespace std;

char table[1000],buff[20000];

int main ()
{
	freopen("table.txt", "r", stdin);
	char s[20], s2[20];
	int n=26;
	while (n--)
	{
		scanf("%s", s);
		scanf("%s", s2);
		table[s[0]]=s2[0];
	}
	FILE *f2 = fopen("in.txt","r");
	int cnt; fscanf(f2, "%d\n", &cnt);
	for (int i =1; i<=cnt;++i)
	{
		fgets(buff,1000000,f2);
		for (char *i = buff; *i; ++i)
			if (*i >= 'a' && *i <= 'z')
				*i = table[*i];
		printf("Case #%d: %s", i,buff);
	}
}

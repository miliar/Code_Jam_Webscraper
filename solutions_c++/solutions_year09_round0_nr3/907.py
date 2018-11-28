#include <cstdio>
#include <cstring>

int Test;

const char sim[] = "welcome to code jam";
void work()
{
	char s[600] = {};
	gets(s);
	int v[20] = {};
	for (int i = 0; s[i]; ++i)
	{
		for (int j = 17; j + 1; --j)
		{
			if (s[i] == sim[j + 1])
			{
				v[j + 1] += v[j];
				v[j + 1] %= 10000;
			}
		}
		if (s[i] == 'w')
			++v[0];
	}
	printf("Case #%d: %04d\n", ++Test, v[18]);
}

int main()
{
	int n;
	scanf("%d", &n);
	char s[50];
	gets(s);
	for (int i = 0; i < n; ++i)
		work();
}

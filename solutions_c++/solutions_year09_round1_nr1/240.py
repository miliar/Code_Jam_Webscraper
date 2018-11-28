#include <cstdio>
#include <cstring>
#include <cstdlib>

using namespace std;

char buf[1024];
int b[10], bLen;
bool v[1000000];



bool Test(int n, int base)
{
	//printf("%d %d\n", n, base);
	if(n == 1)
		return true;
	if(v[n])
		return false;
	v[n] = true;
	int ret = 0;
	while(n)
	{
		int cur = n % base;
		n /= base;
		ret += cur * cur;
	}
	return Test(ret, base);
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t;
	int i, j, k;
	scanf("%d", &t);
	getchar();
	for(int tt = 1; tt <= t; tt++)
	{
		memset(v, 0, sizeof(v));
		gets(buf);
		bLen = 0;
		for(char *tmp = strtok(buf, " "); tmp != NULL; tmp = strtok(NULL, " "))
		{
			b[bLen++] = atoi(tmp);
		}

		for(i = 2; ;i++)
		{
			for(j = 0; j < bLen; j++)
			{
				memset(v, 0, sizeof(v));
				if(!Test(i, b[j]))
					break;
			}
			if(j >= bLen)
				break;
		}
		printf("Case #%d: %d\n", tt, i);
	}

	return 0;
}
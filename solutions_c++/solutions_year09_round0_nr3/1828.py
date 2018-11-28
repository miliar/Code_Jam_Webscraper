#include <iostream>
#include <string>
using namespace std;

int n;
int len;
int sum;
char p[510];
char w[20] = "welcome to code jam";

void work(int ppos, int wpos)
{
	if (ppos > len)
		return;

	if (wpos > 18)
	{
		++sum;
		if (sum >= 10000)
			sum %= 10000;
		return;
	}

	while ((p[ppos] != w[wpos]) && (ppos < len)) ++ppos;
	for (int i=ppos; i<len; ++i)
	{
		while ((p[i] != w[wpos]) && (i < len)) ++i;
		work(i+1, wpos+1);
	}
}

int main()
{
	cin >> n;
	getchar();
	for (int x=1; x<=n; ++x)
	{
		gets(p);
		len = strlen(p);
		sum = 0;
		work(0, 0);
		printf("Case #%d: %04d\n", x, sum);
	}

	return 0;
}
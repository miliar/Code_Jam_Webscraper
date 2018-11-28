#include <cstdio>
#include <string>
using namespace std;
const int MAXD = 5000;
const int MAXL = 15;
string word[MAXD];
int d, l, n;
int calc (char* buf) 
{
	static bool tmp[MAXD];
	static bool tmp1[MAXD];
	memset (tmp, 1, sizeof(tmp));
	
	int now = l;
	int i;
	while (now)
	{
		memset (tmp1, 0, sizeof(tmp));
		if (buf[0] == '(')
		{
			i = 1;
			while (buf[i] != ')')
			{
				for (int j = 0;j < d; j ++)
				{
					if (word[j][l - now] == buf[i])
						tmp1[j] = true;
				}
				i ++;
			}
			for (int j = 0; j < d; j ++)
			{
				tmp[j] &= tmp1[j];
			}
			buf += i + 1;
		} else
		{
			for (int j = 0;j < d; j ++)
			{
				if (word[j][l - now] == buf[0])
					tmp1[j] = true;
			}
			for (int j = 0; j < d; j ++)
			{
				tmp[j] &= tmp1[j];
			}
			buf ++;
		}
		now --;
	}
	int ans = 0;
	for (int j = 0; j < d; j ++)
	{
		if (tmp[j])
		{
			ans ++;
		}
	}
	return ans;
}
int main()
{
	scanf ("%d%d%d", &l, &d, &n);
	char buf[28 * MAXL + 1];
	for (int i = 0; i < d; i ++)
	{
		scanf ("%s", buf);
		word[i] = buf;
	}
	for (int i = 0; i < n; i ++)
	{
		scanf ("%s", buf);
		printf ("Case #%d: %d\n", i + 1, calc(buf));
	}
	
	return 0;
}

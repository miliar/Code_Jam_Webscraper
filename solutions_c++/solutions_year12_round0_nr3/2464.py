#include <cstdio>
#include <cstring>
int db[] = {0, 1, 3, 6, 10, 15, 21};
const int LIM = 2000001;
char used[LIM];
//bool nondec(char* s)
//{
//	for (int i = 1; s[i]; i++)
//		if (s[i] < s[i - 1])
//			return false;
//	return true;
//}
bool mono(char* s)
{
	for (int i = 1; s[i]; i++)
		if (s[i] != s[i - 1])
			return false;
	return true;
}
void doublestr(char* str)
{
	int len = strlen(str);
	for (int i = 0; i < len; i++)
		str[len + i] = str[i];
	str[len * 2] = 0;
}
int count(int a, int b)
{
	char str[16];
	int cnt = 0;
	memset(used, 0, LIM);
	for (int x = a; x <= b; x++)
	{
		if (!used[x])
		{
			sprintf(str, "%d", x);
			if (!mono(str))
			{
				int val, good = 0, len = strlen(str);
				doublestr(str);
				for (int i = 0; i < len; i++)
				{
					if (str[i] != '0')
					{
						str[i + len] = 0;
						sscanf(str + i, "%d", &val);
						if (val >= a && val <= b && !used[val])
						{
							used[val]++;
							good++;
						}
						str[i + len] = str[i];
					}
				}
				if (good)
					cnt += db[good - 1];
			}
		}
	}
	return cnt;
}
int main()
{
	int t, a, b;
	freopen("C-large.in", "r", stdin);
	freopen("C-large.out", "w", stdout);
	scanf("%d", &t);
	for (int i = 1; i <= t; i++)
	{
		scanf("%d%d", &a, &b);
		printf("Case #%d: %d\n", i, count(a, b));
	}
	return 0;
}
//Magicka

#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <fstream>

using namespace std;

int C, D, N;
char c[137][14];
char d[129][13];
char s[1001];
char ans[10001];

void deal (fstream &ouf)
{
	int len = strlen(s), i, j = 0, k, t, f, l;
	bool flag, remove;
	for (i = 0; i < len; i++)
	{
		ans[j++] = s[i];
		remove = false;
		if (j > 1)
		{
			flag = false;
			for (k = 0; k < C; k++)
			{
				if (c[k][0] == ans[j - 2] && c[k][1] == ans[j - 1] || c[k][0] == ans[j - 1] && c[k][1] == ans[j - 2])
				{
					ans[j - 2] = c[k][2];
					j--;
//					break;
					remove = flag = true;
					break;
				}
			}
/*			if (!flag)
			{
				break;
			}*/
		}
		if (remove == false && j > 1)
		{
			for (k = 0; k < D; k++)
			{
				l = f = 0;
				if (ans[j - 1] == d[k][0])
				{
					f = 1;
				}
				else if (ans[j - 1] == d[k][1])
				{
					l = 1;
				}
				if (f == 0 && l == 0)
				{
					continue;
				}
				for (t = 0; t < j - 1; t++)
				{
					if (f == 0 && ans[t] == d[k][0])
					{
						f = 1;
					}
					else if (l == 0 && ans[t] == d[k][1])
					{
						l = 1;
					}
					if (f == 1 && l == 1)
					{
						break;
					}
				}
				if (t < j - 1)
				{
					j = 0;
					break;
				}
			}
		}
	}
	ans[j] = '\0';
	if (j == 0)
	{
//		printf("[]\n");
		ouf << "[]" << endl;
		return;
	}
//	printf("[");
	ouf << "[";
	for (i = 0; i < j - 1; i++)
	{
//		printf("%c, ", ans[i]);
		ouf << ans[i] << ", ";
	}
//	printf("%c]\n", ans[i]);
	ouf << ans[i] << "]" << endl;
}

int main()
{
	int T, num = 1, i;
	fstream inf, ouf;
	inf.open("B-large.txt", ios::in);
	if (!inf)
	{
		exit(0);
	}
	ouf.open("result1.txt", ios::out);
	if (!ouf)
	{
		exit(0);
	}
	inf >> T;
//	scanf("%d", &T);
	while (T > 0)
	{
//		scanf("%d", &C);
		inf >> C;
		for (i = 0; i < C; i++)
		{
			inf >> c[i];
//			scanf("%s", c[i]);
		}
//		scanf("%d", &D);
		inf >> D;
		for (i = 0; i < D; i++)
		{
//			scanf("%s", d[i]);
			inf >> d[i];
		}
//		scanf("%d%s", &N, s);
		inf >> N >> s;
//		printf("Case #%d: ", num);
		ouf << "Case #" << num << ": ";
		num++;
		deal(ouf);
		T--;
	}
	inf.close();
	ouf.close();
	return 0;
}
#include <stdio.h>
#include <algorithm>

using namespace std;

struct Long
{
	int data[21];
	int data2[21];
	int len;

	void Read()
	{
		char c = '0';
		len = 0;
		while(('0' <= c && c <= '9'))
		{
			if (scanf("%c", &c) != 1)
				break;
			if ('0' <= c && c <= '9')
				data[len++] = c - '0';
		}
	}
};

int t;
Long l;
bool is_rez = false;

int main()
{
	freopen("B-small.in", "r", stdin);
	freopen("B-small.out", "w", stdout);
	scanf("%d\n", &t);
	for (int i = 0; i < t; i++)
	{
		l.len = 0;
		l.Read();
		for (int j = 0; j < l.len; j++)
			l.data2[j] = l.data[j];

		is_rez = false;

		next_permutation(l.data, l.data + l.len);
		for (int j = 0; j < l.len; j++)
		{
			if (l.data2[j] < l.data[j])
				is_rez = true;
			if (l.data2[j] != l.data[j])
				break;
		}

		int cnt = 0;

		for (int j = 0; j < l.len; j++)
			if (l.data[j] == 0)
				cnt++;
			else
				break;

		printf("Case #%d: ", i + 1);
		for (int j = cnt; j < l.len; j++)
		{
			printf("%d", l.data[j]);
			if (j == cnt && !is_rez)
				printf("0");
			if (j == cnt)
			{
				for (int u = 0; u < cnt; u++)
					printf("0");
			}
		}
		printf("\n");
	}
	return 0;
}
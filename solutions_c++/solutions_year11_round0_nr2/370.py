#include <stdio.h>
#include <stdlib.h>

#define FOR(i, N)	for (int i=0; i<N; ++i)

namespace
{
	const int cMaxC = 36;
	const int cMaxD	= 28;
	const int cMaxN = 100;
}

char is_combine(int len, char *list, char new_char, int C, char list_c[cMaxC][3])
{
	if (len > 0 && C > 0)
	{
		char last_char = list[len - 1];

		FOR(c, C)
		{
			char c1 = list_c[c][0];
			char c2 = list_c[c][1];

			if (c1 == new_char && c2 == last_char) return list_c[c][2];
			if (c2 == new_char && c1 == last_char) return list_c[c][2];
		}
	}

	return 0;
}

bool is_oppose(int len, char *list, char new_char, int D, char list_d[cMaxD][2])
{
	if (len > 0 && D > 0)
	{
		char list_oppose[cMaxD];
		int num_oppose = 0;

		FOR(d, D)
		{
			if (list_d[d][0] == new_char) {list_oppose[num_oppose] = list_d[d][1]; ++num_oppose;}
			if (list_d[d][1] == new_char) {list_oppose[num_oppose] = list_d[d][0]; ++num_oppose;}
		}

		if (num_oppose > 0)
		{
			FOR(l, len) FOR(o, num_oppose) if (list[l] == list_oppose[o]){ return true; }
		}
	}
	return false;
}

int main()
{
	int T=0; scanf("%d", &T);

	FOR(t, T)
	{
		char list_c[cMaxC][3];
		char list_d[cMaxD][2];
		char list_n[cMaxN];

		int C = 0;
		int D = 0;
		int N = 0;

		printf("Case #%d: [", t+1);

		// read

		scanf("%d ", &C);
		FOR(c, C) scanf("%c%c%c ", &list_c[c][0], &list_c[c][1], &list_c[c][2]);

		scanf("%d ", &D);
		FOR(d, D) scanf("%c%c ", &list_d[d][0], &list_d[d][1]);

		scanf("%d ", &N);
		FOR(n, N) scanf("%c", &list_n[n]);

		// solve

		char list_a[cMaxN];
		int  pos = 0;

		FOR(n, N)
		{
			char new_char = list_n[n];

		restart:
			char combine = is_combine(pos, list_a, new_char, C, list_c);
			if (combine != 0)
			{
				pos -= 1;
				new_char = combine;
				goto restart;
			}

			if (is_oppose(pos, list_a, new_char, D, list_d))
			{
				pos = 0;
				continue;
			}

			// add

			list_a[pos] = new_char;
			++pos;
		}

		FOR(i, pos)
		{
			printf("%c", list_a[i]);
			if (i < pos - 1) printf(", ");
		}

		printf("]\n");
	}
}

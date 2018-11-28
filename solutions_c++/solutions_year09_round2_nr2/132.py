#include <iostream>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <queue>
#include <set>
using namespace std;

char	s[30];
int		p[50], L;
int		T;

void Init ()
{
	scanf ("%s", s);
	L = strlen (s);

	for (int i = L - 1; i >= 0; --i)
	{
		int min = -1;
		for (int j = i + 1; j < L; ++j)
			if (s[j] > s[i])
				if (min == -1 || s[j] < s[min])
					min = j;

		if (min == -1) continue;

		swap (s[i], s[min]);

		for (int j = i + 1; j < L; ++j)
			for (int k = j + 1; k < L; ++k)
				if (s[j] > s[k]) swap (s[j], s[k]);

		printf ("%s\n", s);
		return;
	}

	int d[10];
	memset (d, 0, sizeof (d));
	for (int i = 0; i < L; ++i)
		d[s[i] - '0'] ++;
	d[0] ++;

	for (int i = 0; i < L + 1; ++i)
	{
		int st = 0;
		if (i == 0) st = 1;
		while (d[st] == 0) ++st;
		printf ("%d", st);
		d[st] --;
	}
	printf ("\n");
}

int main()
{
	freopen ("in.txt", "r", stdin);
	freopen ("ou.txt", "w", stdout);

	scanf ("%d", &T);
	for (int i = 1; i <= T; ++i)
	{
		printf ("Case #%d: ", i);
		Init ();
	}

	return 0;
}

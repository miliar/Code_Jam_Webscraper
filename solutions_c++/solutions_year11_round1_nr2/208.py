#include <iostream>
#include <cstring>
#include <cstdio>
using namespace std;

const int MAXN = 10000 + 10;
const int MAXM = 100 + 10;
const int MAXL = 20;

char w[MAXN][MAXL];
char s[MAXM][30];
int bset[MAXN];
int list[MAXN];
int N, M, tot;


void Init ()
{
	scanf ("%d%d", &N, &M);
	for (int i = 0; i < N; i++) {
		scanf ("%s", w[i]);
		bset[i] = 0;

		for (int j = 0; j < strlen (w[i]); j++) {
			bset[i] |= 1 << (w[i][j] - 'a');
		}
	}

	for (int i = 0; i < M; i++)
		scanf ("%s", s[i]);
}

int check (char w1[], char w2[], char c)
{
	int l = strlen (w2);
	for (int i = strlen (w1); i >= 0; --i) {
		if (w1[i] != c) {
			if (i < l && w2[i] == c) return 0;
		} else {
			if (i >= l || w2[i] != c) return 0;
		}
	} 

	return 1;
}

int calc (char s[], char word[], int wset)
{
	int tot = 0;
	int curset = 0;
	for (int i = 0; i < N; i++)
	{
		if (strlen (w[i]) != strlen (word)) continue;
		list[tot ++] = i;
		curset |= bset[i];
	}

	int right = 0;

	int d, ret = 0;
	for (int i = 0; i < 26; i++) {

		d = (1 << (s[i] - 'a'));

		if (!(curset & d)) continue;

		if (!(wset & d))
			ret ++;
		else {
			wset ^= d;
			right |= d;
		}

		if (wset == 0) return ret;

		int j = 0;
		curset = 0;

		while (j < tot) {
			if (check (w[list[j]], word, s[i])) {
				curset |= bset[list[j]];
				j ++;
			}
			else
				list[j] = list[-- tot];
		}
	}

	return ret;
}

void Solve ()
{
	for (int i = 0; i < M; i++) {
		int max = -1, ans, tmp;

		for (int j = 0; j < N; j++) {
			tmp = calc (s[i], w[j], bset[j]);

			//printf ("%s %s   %d\n", s[i], w[j], tmp);
			if (tmp > max) {
				max = tmp;
				ans = j;
			}
		}

		printf (" %s", w[ans]);
	}
	printf ("\n");
}

int main ()
{
	//freopen ("in.txt", "rt", stdin);

	int T;

	scanf ("%d", &T);

	for (int i = 1; i <= T; i++) {
		printf ("Case #%d:", i);
		Init ();
		Solve ();
	}

	return 0;
}


#include <cstdio>
#include <algorithm>
using namespace std;
int cases, k, len;
char s[50001], t[50001];
int p[20], cnt, ans;
int main ()
{
//	freopen ("D-small-attempt0.in", "r", stdin);
//	freopen ("output.txt", "w", stdout);
	int i, j;
	scanf ("%d", &cases);
	for (int tt = 1; tt <= cases; tt++){
		scanf ("%d", &k);
		scanf ("%s", s);
		for (i = 0; i < k; ++ i) p[i] = i;
		len = strlen (s);
		ans = 0x7fffffff;
		do {
			for (i = 0; i < len / k; i++)
				for (j = 0; j < k; j++)
					t[i*k+j] = s[i*k+p[j]];
			cnt = 0;
			for (i = 0; i < len; i++)
				if (i == 0 || t[i] != t[i-1]) cnt++;
			ans <?= cnt;
		}while (next_permutation (p, p + k));
		printf ("Case #%d: %d\n", tt, ans);
	}
}

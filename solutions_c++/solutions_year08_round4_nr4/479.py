#include	<cstdio>
#include	<algorithm>
using namespace std;
int t, k, len;
char s[1001], s2[1001];
int perm[5], cnt, best;
int main ()
{
	freopen ("D-small-attempt0.in", "r", stdin);
	freopen ("output.txt", "w", stdout);
	scanf ("%d", &t);
	for (int l = 1; l <=t; ++l)
	{
		scanf ("%d", &k);
		scanf ("%s", s);
		for (int i = 0; i < k; ++ i)
			perm[i] = i;
		len = strlen (s);
		best = 0x7fffffff;
		do {
			for (int i = 0; i < len / k; ++ i)
			{
				for (int j = 0; j < k; ++ j)
					s2[i*k+j] = s[i*k+perm[j]]; 
			}
			cnt = 0;
			for (int i = 0; i < len; ++ i)
				if (i == 0 || s2[i] != s2[i-1])
					++ cnt;
			best <?= cnt;
		} while (next_permutation (perm, perm + k));
		printf ("Case #%d: %d\n",l ,best);
	}
	//system ("pause");
}

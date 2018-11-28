#include<cstdio>
#include<algorithm>
#define INF 0x7fffffff
using namespace std;
int t, k, len;
char s[1001], str[1001];
int p[5], cnt, ans;
void cal()
{
	do {
		for (int i = 0; i < len / k; ++ i)
		{
			for (int j = 0; j < k; ++ j)
				str[i*k+j] = s[i*k+p[j]]; 
		}
		int temp = 0;
		for (int i = 0; i < len; ++ i)
			if (i == 0 || str[i] != str[i-1])
				++ temp;
		ans <?= temp;
	} while (next_permutation (p, p + k));

}
int main ()
{
	freopen ("D-small-attempt0.in", "r", stdin);
	freopen ("output.txt", "w", stdout);
	int cases;
	scanf ("%d", &cases);
	for (int ca = 1; ca <= cases; ++ca)
	{
		scanf ("%d", &k);
		scanf ("%s", s);
		for (int i = 0; i < k; ++ i)
			p[i] = i;
		len = strlen (s);
		ans = INF;
		cal();
		printf ("Case #%d: %d\n",ca ,ans);
	}
}

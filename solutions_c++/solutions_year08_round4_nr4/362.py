#include <stdio.h>
#include <string.h>
#include <algorithm>
#include <vector>

#define inf 0x3f3f3f3f
#define bmax 50005
#define pb push_back

using namespace std;

int rez;
int T, k;
char s[bmax], nou[bmax];
vector <int> v;

void verif()
{
	for(int i = 0; i < (int)strlen(s) - 1; i++)
	{
		int p1 = i % k;
		int p2 = ((int)i / k) * k;
		nou[p2 + v[p1]] = s[i];
	}

	int tot = 1;
	for(int i = 1; i < (int)strlen(s) - 1; i++)
		if(nou[i] != nou[i - 1]) tot++;

	rez = min(rez, tot);
}

int main()
{
	freopen("d.in", "r", stdin);

	scanf("%d\n", &T);
	for(int t = 1; t <= T; t++)
	{
		printf("Case #%d: ", t);
		scanf("%d\n", &k);
		fgets(s, bmax, stdin);

		v.clear();
		for(int i = 1; i <= k; i++) v.pb(i - 1);
		rez = inf;
		verif(); 
		while(next_permutation(v.begin(), v.end())) verif();

		printf("%d\n", rez);
	}
}

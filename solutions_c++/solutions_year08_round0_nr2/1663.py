#include <stdio.h>
#include <string.h>
#include <algorithm>
#include <vector>

#define pb push_back
#define bmax 1024
#define nmax 1024

using namespace std;
typedef pair<int, int> ii;

char s[bmax];
int v[nmax], start[nmax], finish[nmax];
int T, D, NA, NB, na, nb;
int h1, m1, h2, m2;
vector <ii> pt[2], V;

void clean(int x)
{
	v[x] = 1;
	int celdevreme = finish[x] + D;
	int unde = 1;
	if(x > NA) unde = 0;
	for(int i = 0; i < (int)pt[unde].size(); i++)
		if(!v[pt[unde][i].second] && pt[unde][i].first >= celdevreme)
		{
			clean(pt[unde][i].second);
			break;
		}
}

int main()
{
	freopen("b.in", "r", stdin);
	// freopen("b.out", "w", stdout);

	scanf("%d\n", &T);
	for(int t = 1; t <= T; t++)
	{
		scanf("%d\n", &D);
		scanf("%d %d\n", &NA, &NB);
		memset(v, 0, sizeof(v)); na = nb = 0;
		V.clear(); pt[0].clear(); pt[1].clear();
		for(int i = 1; i <= NA; i++)
		{
			fgets(s, bmax, stdin);
			sscanf(s, "%d:%d %d:%d", &h1, &m1, &h2, &m2);
			start[i] = h1 * 60 + m1;
			finish[i] = h2 * 60 + m2;
			V.pb(ii(start[i], i));
			pt[0].pb(ii(start[i], i));
		}
		for(int i = 1; i <= NB; i++)
		{
			fgets(s, bmax, stdin);
			sscanf(s, "%d:%d %d:%d", &h1, &m1, &h2, &m2);
			start[NA + i] = h1 * 60 + m1;
			finish[NA + i] = h2 * 60 + m2;
			V.pb(ii(start[NA + i], NA + i));
			pt[1].pb(ii(start[NA + i], NA + i));
		}
		sort(V.begin(), V.end());
		sort(pt[0].begin(), pt[0].end());
		sort(pt[1].begin(), pt[1].end());

		for(int i = 0; i < (int)V.size(); i++)
			if(!v[V[i].second])
			{
				if(V[i].second <= NA) na++;
				else nb++;
				clean(V[i].second);
			}

		printf("Case #%d: %d %d\n", t, na, nb);
	}
	
	return 0;
}

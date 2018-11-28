#include <cstdio>
#include <vector>
#include <algorithm>
#include <utility>

using namespace std;

int N, T, NA, NB, sol_a, sol_b;
vector < pair <int, int > > ta, tb;
vector < bool > fa, fb;

int main()
{
	int loop, i, j, h1, m1, h2, m2;
	FILE *fi = fopen("b.in", "r");
	FILE *fo = fopen("b.out", "w");
	fscanf(fi, "%d", &N);
	for (loop = 1; loop <= N; loop ++)
	{
		ta.clear(); tb.clear(); fa.clear(); fb.clear();
		fscanf(fi, "%d %d %d", &T, &NA, &NB);
		for (i=1; i<=NA; i++)
		{
			fscanf(fi, "%d:%d %d:%d", &h1, &m1, &h2, &m2);
			ta.push_back(make_pair(h1*60+m1, h2*60+m2));
			fa.push_back(true);			
		}
		for (i=1; i<=NB; i++)
		{
			fscanf(fi, "%d:%d %d:%d", &h1, &m1, &h2, &m2);
			tb.push_back(make_pair(h1*60+m1, h2*60+m2));
			fb.push_back(true);
		}
		sort(ta.begin(), ta.end());
		sort(tb.begin(), tb.end());
		sol_a = NA; sol_b = NB;
		for (i=0; i<NA; i++)
			for (j=0; j<NB; j++)
				if (ta[i].second + T <= tb[j].first && fb[j])
				{
					fb[j] = false;
					sol_b--;
					break;
				}
		for (i=0; i<NB; i++)
			for (j=0; j<NA; j++)
				if (tb[i].second + T <= ta[j].first && fa[j])
				{
					fa[j] = false;
					sol_a--;
					break;
				}
		fprintf(fo, "Case #%d: %d %d\n", loop, sol_a, sol_b);
	}
	fclose(fi);
	fclose(fo);
	return 0;
}
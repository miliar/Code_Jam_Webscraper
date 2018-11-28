#include <stdio.h>
#include <string.h>
#include <vector>
using namespace std;

int tc, ntc;
int n, m;
int va[10], vb[10];

typedef vector <int> vi;

int ncomp;
vector <int> comp[100];

bool match(const vi& v, int a, int b)
{
	int i;
	int nfound = 0;
	for (i=0; i<v.size(); i++)
	{
		if (v[i] == a) nfound++;
		if (v[i] == b) nfound++;
		if (nfound == 2) return true;
	}
	return false;
}

void fix(int id, int a, int b)
{
	int i;
	int ia, ib;
	for (i=0; i<comp[id].size(); i++)
	{
		if (comp[id][i] == a) ia = i;
		else if (comp[id][i] == b) ib = i;
	}

	if (ia > ib) swap(ia, ib);

	vi v1, v2;
	for (i=ia; i<=ib; i++) v1.push_back( comp[id][i] );

	for (i=ib; i<comp[id].size(); i++) v2.push_back( comp[id][i] );
	for (i=0; i<=ia; i++) v2.push_back( comp[id][i] );

	comp[id] = v1;
	comp[ncomp++] = v2;
}

int best;

int col[10];
int ans[10];

bool tmp[10];

bool valid(int nfix, int target)
{
	int i, j;
	for (i=0; i<ncomp; i++)
	{
		if (target > comp[i].size()) return false;

		for (j=0; j<target; j++) tmp[j] = false;
		for (j=0; j<comp[i].size(); j++)
		{
			if (comp[i][j] >= nfix) break;
			tmp[ col[ comp[i][j] ] ] = true;
		}
		if (j < comp[i].size()) continue;
		for (j=0; j<target; j++) if (!tmp[j]) return false;
	}
	return true;
}

void dfs(int id, int cnum)
{
	int rem = n - id;
	if (cnum + rem <= best) return;
	if (!valid(id, cnum)) return;

	int i;
	if (id == n)
	{
		best = cnum;
		for (i=0; i<n; i++) ans[i] = col[i];
		return;
	}

	for (i=0; i<=cnum; i++)
	{
		col[id] = i;
		if (i == cnum) dfs(id+1, cnum+1);
		else dfs(id+1, cnum);
	}
}

int main()
{
	FILE* fi = fopen("C0.in", "r");
	FILE* fo = fopen("C0.out", "w");

	fscanf(fi, "%d", &ntc);
	int i, j;
	for (tc = 1; tc <= ntc; tc++)
	{
		fscanf(fi, "%d %d", &n, &m);
		for (i=0; i<m; i++) fscanf(fi, "%d", &va[i]);
		for (i=0; i<m; i++) fscanf(fi, "%d", &vb[i]);

		for (i=0; i<100; i++) comp[i].clear();
		ncomp = 0;

		ncomp = 1;
		for (i=0; i<n; i++) comp[0].push_back( i );

		for (i=0; i<m; i++)
		{
			va[i]--;
			vb[i]--;
	
			for (j=0; j<ncomp; j++) if (match(comp[j], va[i], vb[i]))
			{
				fix(j, va[i], vb[i]);
				break;
			}
		}

		//printf("%d\n", ncomp);
		//for (i=0; i<ncomp; i++)
		//{
			//for (j=0; j<comp[i].size(); j++) printf("%d ", comp[i][j] + 1);
			//printf("\n");
		//}

		best = 0;
		dfs(0, 0);

		printf("Case #%d: %d\n", tc, best);
		fprintf(fo, "Case #%d: %d\n", tc, best);
		for (i=0; i<n; i++)
		{
			if (i) printf(" ");
			if (i) fprintf(fo, " ");
			printf("%d", ans[i]+1);
			fprintf(fo, "%d", ans[i]+1);
		}
		printf("\n");
		fprintf(fo, "\n");
	}

	fclose(fi); fclose(fo);
	return 0;
}
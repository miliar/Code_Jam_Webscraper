#include <cstdio>
#include <algorithm>

using namespace std;

int n, s, p;
int maxx;
int a[128];
int b[128][3];

void visit(int x, int t, int total, int prev, int ss)
{
	if(maxx == n) return;
	if(ss > s || ss+n-x<s) return;
	if(t == 2)
	{
		b[x][t] = a[x] - total;
		if(b[x][t] - b[x][0] > 2 || b[x][t] < b[x][0]) return;
		int t1 = min(min(b[x][0], b[x][1]), b[x][2]);
		int t2 = max(max(b[x][0], b[x][1]), b[x][2]);
		if(t2-t1 == 2) ++ss;
		if(ss > s) return;
		if(x == n-1)
		{
			if(ss != s) return;
			int w = 0;
			for(int i = 0; i < n; ++i)
			{
				int t2 = max(max(b[i][0], b[i][1]), b[i][2]);
				if(t2 >= p) w++;
			}
			maxx = max(maxx, w);
		}
		else visit(x+1, 0, 0, 0, ss);
		return;
	}
	int st, ed;
	if(t == 0) st = (a[x]-2)/3, ed = a[x]/3 + 1;
	else st = prev, ed = b[x][0] + 3;
	for(int i = max(0, st); i <= a[x]-total && i < ed; ++i)
	{
		b[x][t] = i;
		visit(x, t+1, total+i, i, ss);
	}
}

int main()
{
	FILE *in = fopen("B-small-attempt0.in", "r");
	FILE *out = fopen("output.txt", "w");

	//in = stdin;
	//out = stdout;

	int tn, ti = 0;
	fscanf(in, "%d", &tn);
	while(tn--)
	{
		fscanf(in, "%d %d %d", &n, &s, &p);
		for(int i = 0; i < n; ++i)
			fscanf(in, "%d", &a[i]);
		maxx = 0;
		visit(0, 0, 0, 0, 0);
		fprintf(out, "Case #%d: %d\n", ++ti, maxx);
	}
}

/*
4
3 1 5 15 13 11
3 0 8 23 22 21
2 1 1 8 0
6 2 8 29 20 8 18 18 21
*/

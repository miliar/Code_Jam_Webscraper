#include <stdio.h>
#include <string.h>

int tc, ntc;
int n;

char buf[5];
char col[200];
int pos[200];

struct tt
{
	int id;
	int po, pb;
};

int val[200][200][200];
tt q[8000000];
int nq;

bool valid(int x)
{
	return x >= 1 && x <= 100;
}

void add(const tt& x, int v)
{
	if (val[x.id][x.po][x.pb] == -1)
	{
		val[x.id][x.po][x.pb] = v;
		q[nq++] = x;
	}
}

int bfs()
{
	memset(val, -1, sizeof(val));
	nq = 0;
	
	tt cur, nex;
	cur.id = 0;
	cur.po = cur.pb = 1;
	add(cur, 0);
	
	int it;
	for (it=0; it<nq; it++)
	{
		cur = q[it];
		int cval = val[cur.id][cur.po][cur.pb];
		if (cur.id == n) return cval;
		// move
		
		int a, b;
		for (a=-1; a<=2; a++) for (b=-1; b<=2; b++)
		{
			if (a == 2 && b == 2) continue;
			if (a == 2)
			{
				if (col[cur.id] != 'O') continue;
				if (pos[cur.id] != cur.po) continue;
			}
			if (b == 2)
			{
				if (col[cur.id] != 'B') continue;
				if (pos[cur.id] != cur.pb) continue;
			}
						
			nex = cur;			
			if (a != 2) nex.po += a;
			if (b != 2) nex.pb += b;
			if (a == 2 || b == 2) nex.id++;
			if (!valid(nex.po) || !valid(nex.pb)) continue;
			add(nex, cval+1);
		}
	}
	
	return -1;
}

int main()
{
	//FILE* fi = fopen("A.in", "r");
	//FILE* fo = fopen("A.out", "w");
	//FILE* fi = fopen("A-small0.in", "r");
	//FILE* fo = fopen("A-small0.out", "w");

	FILE* fi = fopen("A-large.in", "r");
	FILE* fo = fopen("A-large.out", "w");
	
		
	fscanf(fi, "%d", &ntc);
	
	int i;
	for (tc=1; tc<=ntc; tc++)
	{
		fscanf(fi, "%d", &n);
		for (i=0; i<n; i++)
		{
			fscanf(fi, "%s %d", buf, &pos[i]);
			col[i] = buf[0];
		}

		int res = bfs();
		printf("Case #%d: %d\n", tc, res);		
		fprintf(fo, "Case #%d: %d\n", tc, res);		
	}	
	
	fclose(fi); fclose(fo);
}
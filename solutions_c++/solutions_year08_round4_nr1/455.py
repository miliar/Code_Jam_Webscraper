#include <iostream>
using namespace std;
const int INF = 1000000000;
struct ND
{
	int V, G;
	bool C;
};
ND Tr[100010];
void DFS(int p)
{
	if (Tr[p].V + 1) return;
	int ls = (p << 1) + 1;
	int rs = ls + 1;
	if (Tr[ls].V == -1)
		DFS(ls);
	if (Tr[rs].V == -1)
		DFS(rs);

	if (Tr[p].G == 1)
		Tr[p].V = Tr[ls].V & Tr[rs].V;
	else
		Tr[p].V = Tr[ls].V | Tr[rs].V;
}


int Solve(int x, int v)
{
	if(Tr[x].G == -1)
	{
		if (Tr[x].V == v) return 0;
		else
			return INF;
	}
	if (Tr[x].V == v) return 0;
	int ls = (x << 1) + 1;
	int rs = ls + 1, tmp;
	if (Tr[x].C == 1)
	{
		if (Tr[x].G == 1)
		{
			if (v == 0)
				return min(Solve(ls, 0), Solve(rs, 0));
			if (v == 1)
				if (Tr[ls].V == 0 && Tr[rs].V == 0)
					return min(Solve(ls, 1), Solve(rs, 1)) + 1;
				else
					return 1;
		}
		else
		{
			if (v == 1)
				return  min(Solve(ls, 1), Solve(rs, 1));
			if (v == 0)
				if (Tr[ls].V == 1 && Tr[rs].V == 1)
					return min(Solve(ls, 0), Solve(rs, 0)) + 1;
				else
					return 1;
		}
	}
	else
	{
		if (Tr[x].G == 1)
		{
			if (v == 0)
				return min(Solve(ls, 0), Solve(rs, 0));
			if (v == 1)
			{
				tmp =  Solve(rs, 1) + Solve(ls, 1);
				if (tmp > INF) tmp = INF;
				return tmp;
			}
		}
		else
		{
			if (v == 1)
				return min(Solve(rs,1), Solve(ls, 1));
			if (v == 0)
			{
				tmp = Solve(rs, 0) + Solve(ls, 0);
				if (tmp > INF) tmp = INF;
				return tmp;
			}
		}
	}
}

int M, V;
int main()
{
	int t, ii, r, i;
	freopen("A_L.in", "r", stdin);
  
	freopen("A_L.out", "w", stdout);

	scanf("%d", &t);
	for (ii = 1; ii <= t; ++ii)
	{
		scanf("%d%d", &M, &V);
		for (i = 0; i < (M - 1) / 2; ++i)
		{
			scanf("%d%d", &Tr[i].G, &Tr[i].C);
			Tr[i].V = -1;
		}
		for(i = (M-1)/2; i < M; i++)
		{
			scanf("%d", &Tr[i].V);
			Tr[i].G = -1;
			Tr[i].C = 0;
		}
		DFS(0);
		r = Solve(0, V);
		if (r < INF)
			printf("Case #%d: %d\n", ii, r);
		else
			printf("Case #%d: IMPOSSIBLE\n", ii);
	}
}


#include <iostream>

using namespace std;

const int INF = 10000000;

struct node
{
	int C, G, V;
};

node tree[100000];


void Calc(int x)
{
	if (tree[x].V != -1) return ;
	int p1 = 2 * x + 1;
	int p2 = 2 * x + 2;
	if (tree[p1].V == -1)
		Calc(p1);
	if (tree[p2].V == -1)
		Calc(p2);

	if (tree[x].G == 1)
		tree[x].V = tree[p1].V & tree[p2].V;
	else
		tree[x].V = tree[p1].V | tree[p2].V;
}


int Solve(int x, int v)
{
	if (tree[x].G == -1)
	{
		if (tree[x].V == v) return 0;
		else
			return INF;
	}
	if (tree[x].V == v) return 0;
	int p1 = 2 * x + 1;
	int p2 = 2 * x + 2;

	if (tree[x].C == 1)
	{
		if (tree[x].G == 1)
		{
			if (v == 0)
				return min(Solve(p1, 0), Solve(p2, 0));
			if (v == 1)
				if (tree[p1].V == 0 && tree[p2].V == 0)
					return min(Solve(p1, 1), Solve(p2, 1)) + 1;
				else
					return 1;

		}
		else
		{
			if (v == 1)
				return  min(Solve(p1, 1), Solve(p2, 1));
			if (v == 0)
				if (tree[p1].V == 1 && tree[p2].V == 1)
					return min(Solve(p1, 0), Solve(p2, 0)) + 1;
				else
					return 1;
		}
	}
	else
	{
		if (tree[x].G == 1)
		{
			if (v == 0)
				return min(Solve(p1, 0), Solve(p2, 0));
			if (v == 1)
			{
				int temp =  Solve(p1, 1) + Solve(p2, 1);
				if (temp > INF) temp = INF;
				return temp;
			}
		}
		else
		{
			if (v == 1)
				return min(Solve(p1,1), Solve(p2, 1));
			if (v == 0)
			{
				int temp = Solve(p1, 0) + Solve(p2, 0);
				if (temp > INF) temp = INF;
				return temp;
			}
		}
	}
}

int M, V;
int main()
{
	int T;
	freopen("in.txt","r", stdin);
  
	freopen("out.txt", "w", stdout);

	scanf("%d", &T);
	for (int ctr = 1; ctr <= T; ctr++)
	{
		scanf("%d%d", &M, &V);
		
		for (int i = 0; i < (M-1)/ 2; i++)
		{
			scanf("%d%d", &tree[i].G, &tree[i].C);
			tree[i].V = -1;
		}

		for (int i = (M-1)/2; i < M; i++)
		{
			scanf("%d", &tree[i].V);
			tree[i].G = -1;
			tree[i].C = 0;
		}

		Calc(0);


		int ret = Solve(0, V);
		if (ret < INF)
			printf("Case #%d: %d\n", ctr, ret);
		else
			printf("Case #%d: IMPOSSIBLE\n", ctr);
	}
	return 0;
}


#include <cstdio>
#include <iostream>
#include <vector>

using namespace std;

int M,V;

struct Node
{
	int type; //0 - chyslo, 1 - op
	int op; //0 - Or, 1 - And;
	int ch;
	int val; //0,1 0 - Or, 1 - And;
	Node()
	{
	}
	Node(int itype, int v1, int v2)
	{
		type = itype;
		if (itype == 1)
		{
			op = v1;
			ch = v2;
		}
		else
		{
			val = v1;
		}
	}
};

Node vec[11000];

int calc(int elem, int need)
{
	Node x = vec[elem];
	if (x.type == 0)
	{
		if (x.val == need)
		{
			return 0;
		}
		return -1;
	}
	if (x.ch == 0)
	{
		if (x.op == 1) //AND
		{
			if (need == 1)
			{
				int res1 = calc((elem+1)*2-1,need);
				int res2 = calc((elem+1)*2,need);
				if (res1 == -1 || res2 == -1)
					return -1;
				return res1+res2;
			}
			else
			{
				int res1 = calc((elem+1)*2-1,need);
				int res2 = calc((elem+1)*2,need);
				if (res1 == -1 && res2 == -1)
					return -1;
				if (res1 == -1)
					return res2;
				if (res2 == -1)
					return res1;
				return min(res1,res2);

			}
		}
		else //OR
		{
			if (need == 0)
			{
				int res1 = calc((elem+1)*2-1,need);
				int res2 = calc((elem+1)*2,need);
				if (res1 == -1 || res2 == -1)
					return -1;
				return res1+res2;
			}
			else
			{
				int res1 = calc((elem+1)*2-1,need);
				int res2 = calc((elem+1)*2,need);
				if (res1 == -1 && res2 == -1)
					return -1;
				if (res1 == -1)
					return res2;
				if (res2 == -1)
					return res1;
				return min(res1,res2);
			}
		}
	}
	else
	{
		int res = -1;
		if (x.op == 1) //AND
		{
			if (need == 1)
			{
				int res1 = calc((elem+1)*2-1,need);
				int res2 = calc((elem+1)*2,need);
				if (res1 == -1 || res2 == -1)
					res = -1;
				if (res1 != -1 && res2 != -1)
					res = res1+res2;
			}
			else
			{
				int res1 = calc((elem+1)*2-1,need);
				int res2 = calc((elem+1)*2,need);
				if (res1 == -1 && res2 == -1)
					res = -1;
				if (res1 == -1)
					res = res2;
				if (res2 == -1)
					res = res1;
				if (res1 != -1 && res2 != -1)
					res = min(res1,res2);

			}
		}
		else //OR
		{
			if (need == 0)
			{
				int res1 = calc((elem+1)*2-1,need);
				int res2 = calc((elem+1)*2,need);
				if (res1 == -1 || res2 == -1)
					res = -1;
				if (res1 != -1 && res2 != -1)
					res = res1+res2;
			}
			else
			{
				int res1 = calc((elem+1)*2-1,need);
				int res2 = calc((elem+1)*2,need);
				if (res1 == -1 && res2 == -1)
					res = -1;
				if (res1 == -1)
					res = res2;
				if (res2 == -1)
					res = res1;
				if (res1 != -1 && res2 != -1)
					res = min(res1,res2);
			}
		}
		int ress = -1;
		x.op = 1-x.op;
		if (x.op == 1) //AND
		{
			if (need == 1)
			{
				int res1 = calc((elem+1)*2-1,need);
				int res2 = calc((elem+1)*2,need);
				if (res1 == -1 || res2 == -1)
					ress = -1;
				if (res1 != -1 && res2 != -1)
					ress = res1+res2;
			}
			else
			{
				int res1 = calc((elem+1)*2-1,need);
				int res2 = calc((elem+1)*2,need);
				if (res1 == -1 && res2 == -1)
					ress = -1;
				if (res1 == -1)
					ress = res2;
				if (res2 == -1)
					ress = res1;
				if (res1 != -1 && res2 != -1)
					ress = min(res1,res2);

			}
		}
		else //OR
		{
			if (need == 0)
			{
				int res1 = calc((elem+1)*2-1,need);
				int res2 = calc((elem+1)*2,need);
				if (res1 == -1 || res2 == -1)
					ress = -1;
				if (res1 != -1 && res2 != -1)
					ress = res1+res2;
			}
			else
			{
				int res1 = calc((elem+1)*2-1,need);
				int res2 = calc((elem+1)*2,need);
				if (res1 == -1 && res2 == -1)
					ress = -1;
				if (res1 == -1)
					ress = res2;
				if (res2 == -1)
					ress = res1;
				if (res1 != -1 && res2 != -1)
					ress = min(res1,res2);
			}
		}
		if (ress != -1)
			ress++;

		if (res == -1 && ress == -1)
			return -1;
		if (res == -1)
			return ress;
		if (ress == -1)
			return res;
		return min(res,ress);

	}
	return -1;
}

int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int T;
	scanf("%d", &T);
	for (int tt=1; tt<=T; tt++)
	{
		cerr<<tt<<endl;
		scanf("%d%d", &M, &V);
		for (int i=0; i<(M-1)/2; i++)
		{
			int a, b;
			scanf("%d%d", &a, &b);
			vec[i] = Node(1,a,b);
		}
		for (int i=(M-1)/2; i<M; i++)
		{
			int a;
			scanf("%d", &a);
			int p = i;
			vec[p] = Node(0,a,0);
		}
		int res = calc(0, V);
		if (res == -1)
			printf("Case #%d: IMPOSSIBLE\n", tt);
		else
			printf("Case #%d: %d\n", tt, res);
	}
	return 0;
}
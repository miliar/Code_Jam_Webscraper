#include <iostream>
#include <algorithm>
#include <numeric>
#include <vector>
#include <queue>
#include <list>
#include <stack>
#include <string>
#include <fstream>
#include <math.h>
#include <limits>
#include <set>
#include <map>
#include <string>
#include <sstream>
#include <stdio.h>
using namespace std;

#define ALL(ar)       (ar).begin(),(ar).end()
#define SZ(a)         int((a).size())
#define REP(i,n)      for(int i=0,len123=(n);i<len123;i++)
#define FOR(i,n,m)    for(int i=(n),len123=(m);i<len123;i++)
#define INF           (1<<28)
typedef long long          LL;
typedef long double        LD;
typedef unsigned long long ULL;
typedef vector<int>        VI;
typedef pair<int,int>      II;

int sol[2][10002];
int com[10002];

struct Node
{
	bool op, val, changeble, inter;
	int num;
	bool cache;

	Node *left, *right;

	bool compute()
	{
		if (com[num] != -1)	return com[num];
		if (inter)
		{
			if (op == 1)
				com[num] = left->compute() && right->compute();
			else
				com[num] = left->compute() || right->compute();
			return com[num];
		}
		else {
			com[num] = val;
			return com[num];
		}
	}

	int solve(bool _v)
	{
		if (sol[_v][num] != -1) return sol[_v][num];
		
		if (compute() == _v)  {
			sol[_v][num] = 0;
			return 0;
		}

		if (inter)
		{
			int res = 0;
			if (op == 1) {
				if (_v)
					res = left->solve(1) + right->solve(1);
				else
					res = min(left->solve(0), right->solve(0));
			}
			else
			{
				if (_v)
					res = min(left->solve(1), right->solve(1));
				else
					res = left->solve(0) + right->solve(0);
			}
			
			if (changeble)
			{
				int res2 = 1;
				op = !op;

				if (op == 1) {
					if (_v)
						res2 += left->solve(1) + right->solve(1);
					else
						res2 += min(left->solve(0), right->solve(0));
				}
				else
				{
					if (_v)
						res2 += min(left->solve(1), right->solve(1));
					else
						res2 += left->solve(0) + right->solve(0);
				}

				op = !op;
				if (res2 < res)
					res = res2;
			}

			if (res > INF) res = INF;
			sol[_v][num] = res;
			return res;
		}
		else
		{
			if (_v == val) {
				sol[_v][num] = 0;
				return 0;
			}
			else {
				sol[_v][num] = INF;
				return INF;
			}
		}
	}
};

int TC, M, V;
int m[10002];


int main()
{
#ifndef ONLINE_JUDGE
    freopen("in.in", "rt", stdin);
  freopen("out.out", "wt+", stdout);
#endif

	scanf("%d", &TC);
	REP(tc, TC)
	{
		scanf("%d %d", &M, &V);
		REP(i,M+1) { m[i] = INF, sol[0][i] = sol[1][i] = com[i] = -1; }

		vector<Node*> v;

		int a, b, len = (M-1)/2;
		REP(i,len) {
			Node* cur = new Node;
			cur->inter = true;
			scanf("%d %d", &a, &b);
			cur->op = a, cur->changeble = b;
			cur->num = i+1;

			v.push_back(cur);
		}

		REP(i,len+1) {
			Node* cur = new Node;
			cur->inter = false;
			scanf("%d", &a);
			cur->changeble = false;
			cur->val = a;
			cur->num = i+1+len;
			v.push_back(cur);
		}

		Node* root = v[0];
		queue<Node*> q; q.push(root);
		FOR(i,1,M) {
			Node* cur = q.front(); q.pop();
			cur->left = v[i];
			cur->right = v[i+1];
			q.push(cur->left);
			q.push(cur->right);
			i++;
		}

		m[0] = root->solve(V);

		printf("Case #%d: ", tc+1);
		if (m[0] == INF)
			printf("IMPOSSIBLE");
		else
			printf("%d", m[0]);
		printf("\n");
	}

    return 0;
}



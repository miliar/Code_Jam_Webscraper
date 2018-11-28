#define _CRT_SECURE_NO_DEPRECATE
#include <cstdlib>
#include <algorithm>
#include <vector>
#include <string>
#include <cstring>
#include <cstdio>
#include <set>
#include <map>
#include <cmath>
#include <queue>
#include <sstream>
#include <iostream>
using namespace std;

//////////////////// Defines ////////////////////

#pragma comment(linker, "/STACK:67108864")

#define inf      2147483647
#define inf64    9223372036854775807
#define eps      1e-6
#define pi      3.14159265358
#define sqr(a) (a)*(a)
#define rall(a) a.rbegin(),a.rend()
#define all(a) a.begin(),a.end()
#define sz(a) (a).size()
#define mset(a,v) memset(a, v, sizeof(a))
#define pb push_back 
typedef long long ll;
typedef vector<int> VI;
typedef vector<double> VD;
typedef vector<string> VS;

#define ContinueIf(x) if ((x)) continue
#define ContinueUnless(x) if(!(x)) continue

#define BreakIf(x) if ((x)) break
#define BreakUnless(x) if(!(x)) break

#define ReturnUnless(x) if (!(x)) return
#define ReturnIf(x) if ((x)) return

#define ReturnUnless2(x, ret) if (!(x)) return ret
#define ReturnIf2(x, ret) if ((x)) return ret

//////////////////// Problem Code ////////////////////

#define MAX 2048
int needed[MAX], P;

int tree[MAX * 4];

void setRange(int from, int to)
{
	for (int i = from ; i <= to ; ++i)
	{
		--needed[i];
		needed[i] = max(0, needed[i]);
	}
}

void updateTree(int pos, int a, int b, int ind)
{
	ReturnUnless(needed[pos]);
	if (a == b && a == pos)
	{
		// leaf
		tree[ind] = 1;
		--needed[pos];
		return;
	}
	int m = (a + b) / 2;
	if (!tree[ind])
	{
		tree[ind] = 1;
		setRange(a, b);
	}
	if (pos > m)
	{
		updateTree(pos, m + 1, b, ind * 2 + 1);
	}
	else
	{
		updateTree(pos, a, m, ind * 2);
	}
}

int main()
{
	int k, T;
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	scanf("%d", &T);
	for(k = 1 ; k <= T ; ++k)
	{
		int ans = 0;
		scanf("%d", &P);
		mset(tree, 0);
		for (int i = 1 ; i <= (1 << P) ; ++i)
		{
			int n;
			scanf("%d", &n);
			needed[i] = P - n;
		}
		for (int i = 1 ; i <= (1 << P) ; ++i)
		{
			ans += needed[i];
			updateTree(i, 1, (1 << P), 1);
			if (i > 1)
			{
				int t;
				scanf("%d", &t);
			}
		}
		printf("Case #%d: %d\n", k, ans);
	}
	return 0;
}


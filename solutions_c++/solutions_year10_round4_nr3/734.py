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

int mat[128][128][2];

int main()
{
	int k, T;
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	scanf("%d", &T);
	for(k = 1 ; k <= T ; ++k)
	{
		int ans = 0;
		mset(mat, 0);
		int R;
		scanf("%d", &R);
		int mX = 0, mY = 0;
		for (int i = 0 ; i < R ; ++i)
		{
			int x, y, X, Y;
			scanf("%d%d%d%d", &x, &y, &X, &Y);
			for (int j = x ; j <= X ; ++j)
			{
				for (int t = y ; t <= Y ; ++t)
				{
					mat[j][t][0] = 1;
				}
			}
			mX = max(mX, X);
			mY = max(mY, Y);
		}
		int cur = 0, sec = 1;
		while(1) {
		bool flag = true;
		swap(cur, sec);
		for (int i = 1 ; i <= mX ; ++i)
		{
			for (int j = 1 ; j <= mY ; ++j)
			{
				if (mat[i][j][sec] && (!mat[i-1][j][sec] && !mat[i][j-1][sec]))
				{
					flag = false;
					mat[i][j][cur] = 0;
				}
				else if (!mat[i][j][sec] && (mat[i-1][j][sec] && mat[i][j-1][sec]))
				{
					flag = false;
					mat[i][j][cur] = 1;
				}
				else
				{
					mat[i][j][cur] = mat[i][j][sec];
				}
			}
		}
		++ans;
		BreakIf(flag);
		}
		printf("Case #%d: %d\n", k, ans - 1);
	}
	return 0;
}


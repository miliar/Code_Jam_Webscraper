#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

#define sz size()
#define PB push_back
#define clr(x) memset(x, 0, sizeof(x))
#define forn(i,n) for(__typeof(n) i = 0; i < (n); i++)
#define ford(i,n) for(int i = (n) - 1; i >= 0; i--)
#define forv(i,v) forn(i, v.sz)
#define For(i, st, en) for(__typeof(en) i = (st); i < (en); i++)

using namespace std;
typedef long long ll;

int main()
{
	int cases = 0;
	cin >> cases;
	forn(i, cases)
	{
		ll A;
		int N, M;
		cin >> N >> M >> A;
		int j, k, l, m;
		bool found = false;
		for(j=0; j<=N; j++)
			for(k=0; k<=M; k++)
				for(l=0; l<=N; l++)
					for(m=0; m<=M; m++)
						if(abs(j*m-k*l) == A)
						{
							found = true;
							goto b;
						}
		b:
		if(found)
			printf("Case #%d: 0 0 %d %d %d %d\n", i+1, j, k, l, m);
		else
			printf("Case #%d: IMPOSSIBLE\n", i+1);
	}
	return 0;
}

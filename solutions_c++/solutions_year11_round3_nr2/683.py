/**
 * Author        : mahbub
 * Problem Name  : GCJ.R1C.Problem_B._Space_Emergency
 * Algorithm     : 
 * Date          : Sunday, May 22, 2011
 */
#pragma warning ( disable : 4786)
#include <vector>
#include <list>
#include <map>
#include <set>
#include <string>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <numeric>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <sstream>
#include <ctime>
#include <cstring>
#include <climits>
using namespace std;

#define All(X) X.begin(),X.end()
#define For(i, s, n) for(int i=(s); i<=(n); i++)
#define Rep(i, n) for(int i=0; i<(n); i++)
#define Clr(arr) memset(arr, 0, sizeof(arr))
#define Slr(arr) memset(arr, -1, sizeof(arr))
#define Co continue
#define Re return
#define Sf scanf
#define Pf printf
#define Ss stringstream
#define Ox 2147483647
#define Pi (2.0*acos(0.0))
#define Eps (1e-9)

int cs[1001], tcs[1001];
vector<int> used;

bool isUsed(int x) {
	Rep(i, used.size()) {
		if (used[i]==x) {
			Re true;
		}
	}

	Re false;
}
int main() {
	freopen("GCJ.R1C.B.in.txt", "r", stdin);
	freopen("GCJ.R1C.B.out.txt", "w", stdout);
	int tcases, L, t, N, C, mrk;
	long long tim, onmrk;

	Sf("%d",&tcases);

	For(tcase, 1, tcases) {
		Sf("%d %d %d %d",&L, &t, &N, &C);
		Rep(i, C) {
			Sf("%d",&cs[i]);
			tcs[i] = cs[i];
		}
		//sort(tcs, tcs+C);
		tim = 0; mrk = -1;
		For(i, 1, N) {
			tim += 2*cs[(i-1)%C];
			if (tim>t && mrk==-1) {
				mrk = i;
				onmrk = tim;
			}
		}
		//tim *= 2;

		if (mrk > -1) {
			int maxv = -1, ind = -1;
			used.clear();
			while(L-->0) {
				maxv = -1, ind = -1;
				For(i, mrk, N) {
					int dis = 2*cs[(i-1)%C];
					if (i==mrk) {
						dis = onmrk - t;
					}
					if(dis>maxv && !isUsed(i)) {
						ind = i;
						maxv = dis;
					}
				}
				if (maxv > -1) {
					used.push_back(ind);
					tim -= (maxv /2); 
				}
			}
		}

		Pf("Case #%d: %lld\n",tcase, tim);

	}
	Re 0;
}
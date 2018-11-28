#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
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
using namespace std; 
//______________________________________________________________________________________________________________________
#define MPI 3.14159265358979323846264338327950288419716939937510
//______________________________________________________________________________________________________________________
#define ALL(C)              (C).begin(),(C).end() 
#define FOR(i, N)           for (int i = 0; i < (N); ++i)
#define FORC(i, C)          for (int i = 0; i < (C).size(); ++i)
#define FORN(i, x, n)       for (int i = x; i <= (n); ++i)
#define DEBUG(x)            cerr << #x << " = " << (x) << endl;
//______________________________________________________________________________________________________________________

int main()
{
	//freopen("input.txt", "rt", stdin);
	//freopen("output.txt", "wt", stdout);

	int T, R, k, N;

	scanf("%d", &T);
	
	FOR (t, T) {
		scanf("%d%d%d", &R, &k, &N);
		vector<int> vi(N, 0);
		FOR (n, N) scanf("%d", &vi[n]);

		int ind = 0;
		int ret = 0;
		FOR (r, R) {
			int sum = 0;
			FOR (i, N) {
				int x = (ind + i) % N;
				if (sum + vi[x] <= k)	{ sum += vi[x]; }
				else					{ ind = x; break; }
			}
			ret += sum;
		}
		printf("Case #%d: %d\n", t + 1, ret);
	}

	return 0;
}
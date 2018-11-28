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

	int T, N, K;

	scanf("%d", &T);

	FOR (t, T) {
		scanf("%d%d", &N, &K);
		int X = 1 << N;
		K = K % X;
		printf("Case #%d: %s\n", t + 1, (K == X - 1 ? "ON" : "OFF"));
	}

	return 0;
}
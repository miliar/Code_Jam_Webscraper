#include <algorithm> 
#include <bitset> 
#include <cassert>
#include <cmath> 
#include <complex>
#include <cstdio> 
#include <cstdlib> 
#include <cstring>
#include <ctime> 
#include <deque> 
#include <functional> 
#include <iomanip> 
#include <iostream> 
#include <list> 
#include <map> 
#include <numeric> 
#include <queue> 
#include <set> 
#include <sstream> 
#include <stack> 
#include <utility> 
#include <valarray>
#include <vector> 
using namespace std; 

#define ALL(x) (x).begin(), (x).end()
#define MP make_pair
#define SZ(x) ((int) (x).size())
#define max2(x,y) ((x) = max((x),(y)))
#define min2(x,y) ((x) = min((x),(y)))
typedef long long LL;

#define MAXN 1010

int N, K, R;

int groupSize[MAXN];
int nextFirst[MAXN];
int peopleCnt[MAXN];

void calcTables()
{
	int j = 0;
	int sz = 0;
	for (int i = 0; i < N; ++i) {
		if (groupSize[i] > K) {
			nextFirst[i] = -1;
			peopleCnt[i] = 0;
			sz -= groupSize[j];
			j += 1;
			continue;
		}
		if (i == j) {
			sz += groupSize[i];
			j = (j+1) % N;
		}
		while (i != j && sz+groupSize[j] <= K) {
			sz += groupSize[j];
			j = (j+1) % N;
		}
		nextFirst[i] = j;
		peopleCnt[i] = sz;
		sz -= groupSize[i];
	}
}

bool vis[MAXN];

LL solve()
{
	calcTables();
	memset(vis, 0, sizeof vis);

	int currentFirst = 0;
	LL people = 0;
	int rounds = 0;

	while (vis[currentFirst] == false) {
		vis[currentFirst] = true;
		rounds += 1;
		people += peopleCnt[currentFirst];
		currentFirst = nextFirst[currentFirst];
		if (rounds == R || currentFirst == -1)
			return people;
	}

	int roundsLeft = R - rounds;
	LL peopleInCircle = 0;
	rounds = 0;

	memset(vis, 0, sizeof vis);
	while (vis[currentFirst] == false) {
		vis[currentFirst] = true;
		rounds += 1;
		peopleInCircle += peopleCnt[currentFirst];
		currentFirst = nextFirst[currentFirst];
		if (rounds == roundsLeft || currentFirst == -1)
			return people + peopleInCircle;
	}

	int circleCnt = roundsLeft / rounds;
	people += circleCnt * peopleInCircle;
	rounds = circleCnt * rounds;

	if (rounds == roundsLeft)
		return people;

	while (true) {
		rounds += 1;
		people += peopleCnt[currentFirst];
		currentFirst = nextFirst[currentFirst];
		if (rounds == roundsLeft || currentFirst == -1)
			return people;
	}
}

LL solve_slow()
{
	int currentFirst = 0;
	LL people = 0;
	for (int r = 0; r < R; ++r) {
		int oldFirst = currentFirst;
		int sz = groupSize[currentFirst];
		currentFirst = (currentFirst+1) % N;
		assert(sz <= K);

		while (oldFirst != currentFirst && sz+groupSize[currentFirst] <= K) {
			sz += groupSize[currentFirst];
			currentFirst = (currentFirst+1) % N;
		}
		people += sz;
	}
	return people;
}

int main()
{
	int T;
	scanf("%d", &T);
	for (int TC = 1; TC <= T; ++TC) {
		scanf("%d %d %d", &R, &K, &N);
		for (int i = 0; i < N; ++i)
			scanf("%d", &groupSize[i]);
		printf("Case #%d: %lld\n", TC, solve());
		//printf("%lld == %lld\n", solve(), solve_slow());
		//assert(solve() == solve_slow());
	}
	return 0;
}

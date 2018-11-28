#define _CRT_SECURE_NO_WARNINGS
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <climits>
#include <cassert>
#include <ctime>
#include <string>
#include <vector>
#include <algorithm>
#include <map>
#include <set>
#include <queue>
#include <sstream>
#include <numeric>
using namespace std;

#include <iostream>

#define FOR(i, a, b) for (int i(a), _b(b); i <= _b; ++i)
#define FORD(i, a, b) for (int i(a), _b(b); i >= _b; --i)
#define REP(i, n) for (int i(0), _n(n); i < _n; ++i)
#define REPD(i, n) for (int i((n)-1); i >= 0; --i)
#define ALL(c) (c).begin(), (c).end()

typedef long long int64;
typedef unsigned long long uint64;

template<typename T> int size(const T& c) { return (int)c.size(); }
template<typename T> void remin(T& a, const T& b) { if (b < a) a = b; }
template<typename T> void remax(T& a, const T& b) { if (b > a) a = b; }
template<typename T> T abs(T x) { return x < 0 ? -x : x; }
template<typename T> T sqr(T x) { return x*x; }


void Solve(int caseNo)
{
	int L,N,C;
	long long t;
	cin >> L >> t >> N >> C;

	vector<int>AA(C);
	REP(i,C){
		cin >> AA[i];
	}

	vector<int>DistArr(N);
	int a = 0;
	REP(i,N){
		DistArr[i] = AA[a];
		a++;
		if (a>=C){
			a=0;
		}
	}

	vector<int> LPosArr(L);
	long long minTime = 10000000000000000;

	REP(i,L){
		LPosArr[i] = N;
	}

	bool isOK;
	do 
	{
		////////
		// Simulation
		long long curTime = 0;
		REP(n,N){
			int n1 = n;
			int n2 = n+1;
			int dist = DistArr[n]; // From n1 to n2
			bool hasBoost = false;
			REP(l,L){
				if (LPosArr[l] == n)
				{
					hasBoost = true;
					break;
				}
			};
			
			long long endTime = curTime + 2 * dist;
			if (!hasBoost || (endTime < t)){
				curTime += 2 * dist;
			}
			else {
				// Booster is effective
				if (curTime >= t){
					curTime += dist;
				}
				else {
					long long nonBoostedTime = t - curTime;
					assert (nonBoostedTime >= 0);
					assert (nonBoostedTime % 2 == 0);
					int nonBoostedDist = nonBoostedTime / 2;
					int boostedDist = dist - nonBoostedDist;
					curTime += 2 * nonBoostedDist + boostedDist;
				}
			}
		}

		////////

		if (minTime > curTime) {
			minTime = curTime;
		}

		isOK = false;
		for (int pos = L-1; pos >=0; pos--)
		{
			LPosArr[pos]--;
			if (LPosArr[pos] >= 0){
				isOK = true;
				break;
			}
			else
			{
				LPosArr[pos] = N;
			}
		}

	} while (isOK);




	//int lstate = 0; // State of boosters
	//REP(i,1<<L){
	//	REP(j,L){
	//		LPosArr[i] = ((lstate & 1<<i) != 0) ? 1 : 0;

	//		////////
	//		// Simulation
	//		long long curTime = 0;
	//		REP(n,N){
	//			int n1 = n;
	//			int n2 = n+1;
	//			int dist = DistArr[n]; // From n1 to n2
	//			if(LPosArr[])
	//			


	//		}


	//		////////
	//		if (minTime < curTime) {
	//			minTime = curTime;
	//		}
	//	}
	//	lstate++;
	//}

	printf("Case #%d: %d\n", caseNo, minTime);
    //printf( "%2.1f\n", ans );
}


int main()
{
	//if (freopen("c:\\_temp\\B.in", "rt", stdin) == NULL) throw 1;
	//if (freopen("c:\\_temp\\B.out", "wt", stdout) == NULL) throw 2;

	if (freopen("c:\\_temp\\B-small-attempt0.in", "rt", stdin) == NULL) throw 1;
	if (freopen("c:\\_temp\\B-small-attempt0.out", "wt", stdout) == NULL) throw 2;

	//if (freopen("c:\\_temp\\B_test.in", "rt", stdin) == NULL) throw 1;
	//if (freopen("c:\\_temp\\B_test.out", "wt", stdout) == NULL) throw 2;

	//if (freopen("c:\\_temp\\B-large.in", "rt", stdin) == NULL) throw 1;
	//if (freopen("c:\\_temp\\B-large.out", "wt", stdout) == NULL) throw 2;

	int caseCount;
	scanf("%d%", &caseCount);
	clock_t totalNow = clock();

	FOR(i, 1, caseCount) {
		clock_t now = clock();
		cerr << "case " << i << "...";
		
		Solve(i);
		fflush(stdout);

		cerr << "Done!; Elapsed ms:" << (double)(clock() - now) * 1000 / CLOCKS_PER_SEC << "\n";
	}
	cerr << "Total elapsed seconds:" << (double)(clock() - totalNow) / CLOCKS_PER_SEC << "\n";

	exit(0);
}
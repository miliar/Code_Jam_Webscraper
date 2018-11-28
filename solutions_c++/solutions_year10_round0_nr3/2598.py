#include <cstdio>
#include <cmath>
#include <iostream>
#include <sstream>
#include <iomanip>
#include <vector>
#include <list>
#include <stack>
#include <queue>
#include <string>
#include <algorithm>
#include <set>
#include <map>

using namespace std;


typedef vector<int> VI;
typedef vector<double> VD;
typedef vector<string> VS;
typedef long long LL;

#define FOR(i, L, U)		for(int i=L; i<=U; i++)
#define EPS 1e-9


queue<int> g, gNext;

int main()
{

//	freopen("E:\\C-small-attempt1.in", "r", stdin);
//	freopen("E:\\output.txt", "w", stdout);

	int TC, tcase;
	int R, k, N;
	int i, j;
	int temp, totalEuro, eachRide, groupTaken;

	cin >> TC;

	FOR(tcase, 1, TC) {
		totalEuro = 0;

		cin >> R >> k >> N;

		g = queue<int>();		

		FOR(i, 1, N) {
			cin >> temp;
			g.push(temp);
		}
		
		FOR(i, 1, R) {
			eachRide = 0;
			for(groupTaken = 1;  eachRide + g.front() <= k && groupTaken <= N; groupTaken++) {
				eachRide += g.front();
				g.push(g.front());
				g.pop();
			}
			totalEuro += eachRide;
		}
		cout << "Case #" << tcase << ": " << totalEuro << "\n";

	}

	return 0;
}
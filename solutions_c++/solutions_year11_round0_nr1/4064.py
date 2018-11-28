#define _CRT_SECURE_NO_WARNINGS

#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <cctype>

#include <iostream>
#include <sstream>
#include <string>

#include <vector>
#include <list>
#include <queue>
#include <set>
#include <map>
#include <stack>
#include <algorithm>
using namespace std;

#define FOR(i,a,b) for (int i = (a); i < (b); ++i)
#define FORN(i,a,n) for (int i = (a); i < (a)+(n); ++i)

//#define DEBUG(x) cout << '>' << #x << ':' << x << endl;
//#define SIZE(x) int(x.size())

typedef pair<int,int> PII;
typedef long long ll;

/////////////////////////////////////////////////////////////////////////

#define MAXD 150

vector<int> robots[2];
vector<int> probots[2];
vector<int> who;

void Solve(int testcase)
{
	printf("Case #%d: ", testcase+1);

	int N;
	scanf(" %d", &N);

	robots[0].clear();
	robots[1].clear();
	probots[0].clear();
	probots[1].clear();
	who.clear();

	// nacitaj
	FOR (i, 0, N) {
		int pos;
		char robot;
		scanf(" %c %d", &robot, &pos);

		who.push_back(robot == 'O' ? 0 : 1);
		robots[who[i]].push_back(pos);
	}

	// simuluj zvlast
	FOR (r, 0, 2) {
		int pos = 1;
		int time = 0;
		FOR (i, 0, robots[r].size()) {
			time += abs(robots[r][i]-pos)+1;
			probots[r].push_back(time);
			pos = robots[r][i];
		}
	}


	int ind[2] = {0, 0}, delay[2] = {0, 0};
	int time = 0;
	FOR (i, 0, N) {
		if (probots[who[i]][ind[who[i]]]+delay[who[i]] > time)
			time = probots[who[i]][ind[who[i]]]+delay[who[i]];
		else {
			delay[who[i]] += time-( probots[who[i]][ind[who[i]]] + delay[who[i]] )+1;
			time++;
		}

		ind[who[i]]++;
	}

	printf("%d\n", time);
}

int main()
{
	int T;
	scanf(" %d", &T);
	FOR (t, 0, T)
		Solve(t);
	
	return 0;
}

#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <deque>
#include <queue>
#include <set>
#include <map>
#include <algorithm>
#include <functional>
#include <utility>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstdio>

using namespace std;

#define FOR(i,n) for((i)=0;(i)<(int)(n);(i)++)
#define foreach(c,itr) for(__typeof((c).begin()) itr=(c).begin();itr!=(c).end();itr++)

vector<pair<char,int>> positions;

int findNext(char robot, int whereNow)
{
	while (++whereNow < positions.size())
	{
		if (positions[whereNow].first == robot)
			break;
	}

	return whereNow;
}

int run_simple(char robot, int whereNow, int posNow)
{
	int result = 0;
	int next;

	while (whereNow < positions.size()) {
		next = positions[whereNow].second;

		result += abs(next - posNow) + 1;
		posNow = next;

		whereNow++;
	}

	return result;
}

int run_complex(char robot1, int &whereNow1, int &posNow1, char robot2, int &whereNow2, int &posNow2)
{
	int next1, next2;
	int travel;
	int travel2;

	next1 = positions[whereNow1].second;
	next2 = positions[whereNow2].second;

	travel = abs(next1 - posNow1) + 1;
	travel2 = abs(next2 - posNow2);

	if (travel < travel2)
		travel2 = travel;

	posNow1 = next1;
	if (next2 > posNow2)
		posNow2 += travel2;
	else
		posNow2 -= travel2;
	
	whereNow1 = findNext(robot1, whereNow1);

	return travel;
}

int solve(int test)
{
	int i;
	char robotID;
	int position;
	int count;
	int whereO = 0;
	int whereB = 0;
	int posO, posB;
	int time = 0;

	positions.resize(0);

	cout << "Case #" << test << ": ";

	cin >> count;

	FOR(i, count) {
		cin >> robotID >> position;
		
		positions.push_back(pair<char, int>(robotID, position));
	}

	posO = 1;
	posB = 1;

	whereO = findNext('O', -1);
	whereB = findNext('B', -1);

	while (whereO < positions.size() && whereB < positions.size()) {
		if (whereO < whereB) {
			time += run_complex('O', whereO, posO, 'B', whereB, posB);
		} else {
			time += run_complex('B', whereB, posB, 'O', whereO, posO);
		}
	}

	if (whereO < positions.size())
		time += run_simple('O', whereO, posO);

	if (whereB < positions.size())
		time += run_simple('B', whereB, posB);

	cout << time << endl;

	return 0;
}

int main()
{
	int cases = 0;
	int i;

	freopen("A_small_1.in", "r", stdin);
	freopen("A_small_1.out", "w", stdout);
	
	cin >> cases;

	FOR(i, cases) {
		solve(i + 1);
	}
	
	return 0;
}

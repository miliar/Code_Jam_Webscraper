#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <climits>
#include <cfloat>
#include <map>
#include <utility>
#include <set>
#include <iostream>
#include <memory>
#include <string>
#include <vector>
#include <algorithm>
#include <functional>
#include <sstream>
#include <complex>
#include <stack>
#include <queue>
#include <list>
#include <fstream>
#include <cstring>

using namespace std;
static const double EPS = 1e-5;
typedef long long ll;

struct EVENT
{
	int time;
	int station;
	int add;
	EVENT(int time, int station, int add) : time(time), station(station), add(add){}
	bool operator<(const EVENT& rh)const{
		return time != rh.time ? time < rh.time : 
			add != rh.add ? add > rh.add :
			station < rh.station;
	}
};

//イベント開始時間->(到着時間,出発駅)
bool check(int t, int na, int nb, const multiset<EVENT>& events)
{
	int trains[2] = {na, nb};
	for (multiset<EVENT>::const_iterator it = events.begin(); it != events.end(); ++it){
		trains[it->station] += it->add;
		
		if (trains[it->station] < 0){
			return false;
		}
	}

	return true;
}

int main() {
	int N;
	cin >> N;

	for (int testCase = 1; testCase <= N; ++testCase){
		int T, NA, NB;
		cin >> T >> NA >> NB;

		multiset<EVENT> events;

		for (int na = 0; na < NA; ++na){
			int h0, m0, h1, m1;
			char c;
			cin >> h0 >> c >> m0 >> h1 >> c >> m1;

			const int startTime = h0 * 60 + m0;
			const int goalTime = h1 * 60 + m1;
			events.insert(EVENT(startTime, 0, -1));
			events.insert(EVENT(goalTime + T, 1, 1));
		}

		for (int nb = 0; nb < NB; ++nb){
			int h0, m0, h1, m1;
			char c;
			cin >> h0 >> c >> m0 >> h1 >> c >> m1;

			const int startTime = h0 * 60 + m0;
			const int goalTime = h1 * 60 + m1;
			events.insert(EVENT(startTime, 1, -1));
			events.insert(EVENT(goalTime + T, 0, 1));
		}

		int minSum = INT_MAX;
		int answerA = INT_MAX;
		int answerB = INT_MAX;

		for (int na = 0; na <= NA; ++na){
			for (int nb = 0; nb <= NB; ++nb){
				if (check(T, na, nb, events)){
					if (minSum > na + nb){
						answerA = na;
						answerB = nb;
						minSum = na + nb;
					}
					break;
				}
			}
		}

		printf("Case #%d: %d %d\n", testCase, answerA, answerB);
	}
}

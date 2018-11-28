#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
#include <cstdlib>
#include <string>
using namespace std;

enum Type { AtoB, BtoA };

struct TimeData {
	int begin;
	int end;
	Type type;
};

class CompBeginTime
{
public:
	bool operator()(const TimeData &a, const TimeData &b)
	{
		return a.begin > b.begin;
	}
};

class CompEndTime
{
public:
	bool operator()(const TimeData &a, const TimeData &b)
	{
		return a.end > b.end;
	}
};

void solve(const vector<TimeData> &timeA, const vector<TimeData> &timeB, int &ac, int &bc)
{
	priority_queue<TimeData, vector<TimeData>, CompBeginTime> beginQue;
	priority_queue<TimeData, vector<TimeData>, CompEndTime> endQue;

	for (int i=0; i < timeA.size(); ++i) {
		beginQue.push(timeA[i]);
		endQue.push(timeA[i]);
	}
	for (int i=0; i < timeB.size(); ++i) {
		beginQue.push(timeB[i]);
		endQue.push(timeB[i]);
	}

	int trainA = 0;
	int trainB = 0;
	while (beginQue.empty()==false) {
		while (endQue.empty()==false) {
			if (endQue.top().end > beginQue.top().begin) break;
			TimeData d = endQue.top();
			endQue.pop();
			if (d.type==AtoB) ++trainB;
			else ++trainA;
		}

		TimeData now = beginQue.top();
		beginQue.pop();
		if (now.type==AtoB) {
			if (trainA==0) {
				++ac;
				++trainA;
			}
			--trainA;
		}
		else {
			if (trainB==0) {
				++bc;
				++trainB;
			}
			--trainB;
		}
	}
}


int main()
{
	int T;
	for (cin>>T; T>0; --T) {
		int t;
		cin >> t;
		int n, m;
		cin >> n >> m;

		vector<TimeData> timeA;
		for (int i=0; i < n; ++i) {
			int a, b, c, d;
			scanf("%d:%d %d:%d", &a, &b, &c, &d);
			TimeData td = { a*100 + b, c*100+d+t, AtoB };
			timeA.push_back(td);
		}
		vector<TimeData> timeB;
		for (int i=0; i < m; ++i) {
			int a, b, c, d;
			scanf("%d:%d %d:%d", &a, &b, &c, &d);
			TimeData td = { a*100 + b, c*100+d+t, BtoA };
			timeB.push_back(td);
		}

		int ac=0, bc=0;
		solve(timeA, timeB, ac, bc);
		static int counter = 0;
		cout << "Case #" << ++counter << ": " << ac << " " << bc << endl;
	}
	return 0;
}

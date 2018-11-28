#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <iostream>
#include <algorithm>
#include <vector>
#include <list>
#include <string>
#include <queue>
#include <map>
#include <set>
using namespace std;

class timetable_t {
	public:
	int s, e;
	int dir;
	
	bool operator<(const timetable_t &x) const { return s < x.s; }
};

void calc(int no)
{
	int na, nb, t;
	string x;
	vector<timetable_t> timetable;
	priority_queue<int, vector<int>, greater<int> > la, lb;
	int ca = 0, cb = 0;
	int i;
	
	cin >> t;
	cin >> na >> nb;
	
	timetable.resize(na + nb);
	
	for (i = 0; i < na + nb; i++) {
		cin >> x;
		timetable[i].s = ( (x[0] - '0') * 10 + (x[1] - '0') ) * 60 + (x[3] - '0') * 10 + (x[4] - '0');
		cin >> x;
		timetable[i].e = ( (x[0] - '0') * 10 + (x[1] - '0') ) * 60 + (x[3] - '0') * 10 + (x[4] - '0');
		if (i < na) timetable[i].dir = 0;
		else timetable[i].dir = 1;
	}
	
	sort(timetable.begin(), timetable.end() );
	
	for (i = 0; i < timetable.size(); i++) {
		if (timetable[i].dir == 1) {
			if (lb.empty() ) {
				cb++;
				la.push(timetable[i].e + t);
			} else {
				int s = lb.top();
				if (s <= timetable[i].s) {
					lb.pop();
					la.push(timetable[i].e + t);
				} else {
					cb++;
					la.push(timetable[i].e + t);
				}
			}
		} else {
			if (la.empty() ) {
				ca++;
				lb.push(timetable[i].e + t);
			} else {
				int s = la.top();
				if (s <= timetable[i].s) {
					la.pop();
					lb.push(timetable[i].e + t);
				} else {
					ca++;
					lb.push(timetable[i].e + t);
				}
			}
		}
	}
	
	printf("Case #%d: %d %d\n", no, ca, cb);
	
	return;
}

			
int main()
{
	int n;
	int i;
	
	cin >> n;
	
	for (i = 0; i < n; i++) calc(i + 1);
	
	return 0;
}

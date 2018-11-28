#include <cstdio>
#include <algorithm>
#include <vector>

using namespace std;

const int MAXN = 1000+6;
int X, S, R, t, N;

struct Walkway {
	int start;
	int stop;
	int speed;
	double timeCanRun;

	Walkway(int start, int stop, int speed) : start(start), stop(stop), speed(speed), timeCanRun(0) {}
};

vector<Walkway> v;

bool cmp(int i, int j) {
	return v[i].speed < v[j].speed;
}

double res;

double timeCanRun;

void solve(int caseNumber) {
	printf("Case #%d: ", caseNumber);	
	scanf("%d %d %d %d %d", &X, &S, &R, &t, &N); 

	timeCanRun = t;

	int prev = 0;

	for(int i = 0; i < N; i++) {
		int start, stop, speed;
		scanf("%d %d %d", &start, &stop, &speed);	
		v.push_back(Walkway(prev, start, S));
		v.push_back(Walkway(start, stop, S+speed));		
		prev = stop;
	}
	v.push_back(Walkway(prev, X, S));

	vector<int> t;
	for(int i = 0; i < v.size(); i++) t.push_back(i);
	sort(t.begin(), t.end(), &cmp);

	for(int i = 0; i < t.size(); i++) {
		Walkway &w = v[t[i]];

		int runningSpeed = w.speed-S+R;
		double distanceNeeded = w.stop-w.start;	
		double timeNeeded = distanceNeeded/runningSpeed;
		w.timeCanRun = min(timeNeeded, timeCanRun);
		timeCanRun -= w.timeCanRun;
	}

	
	res = 0;

	for(int i = 0; i < v.size(); i++) {
		Walkway &w = v[i];
		int runningSpeed = w.speed-S+R;
		double distanceNeeded = w.stop-w.start;	

		res += w.timeCanRun;
		distanceNeeded -= w.timeCanRun*runningSpeed;

		double timeNeeded = distanceNeeded/w.speed;
		res += timeNeeded;
	}

	v.clear();
	printf("%.8lf\n", res);
	
}


int main() {

	//freopen("in.txt", "r", stdin);
	int t;
	scanf("%d", &t);
	for(int i = 1; i <= t; i++) solve(i);
}
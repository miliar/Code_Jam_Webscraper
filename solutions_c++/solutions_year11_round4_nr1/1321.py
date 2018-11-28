#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <iomanip>

using namespace std;

ifstream fin("A-large.in");
ofstream fout("A-large.out");

int X,R,S,N;
double t;
double result;

struct Walkway {
	int dist,W;
};

bool compare(const Walkway& a, const Walkway& b) {
	if ((S + a.W) < (S + b.W)) return true;
	return false;
}

vector<Walkway> w;

const int maxN = 32;
const int maxT = 128;

void input() {
	fin >> X >> S >> R >> t >> N;
	w.clear();
	Walkway walking;
	walking.W = 0;
	walking.dist = X;
	w.push_back(walking);
	for (int i=0;i<N;i++) {	
		Walkway tmp;
		int E,B;
		fin >> B >> E >> tmp.W;
		tmp.dist = E - B;
		w.push_back(tmp);
		w[0].dist -= tmp.dist;
	}
	sort(w.begin(), w.end(), compare);
}

void solve() {
	result = 0;
	for (int i=0;i<w.size();i++) {
		double time = min(t, ((double)w[i].dist / (double)(w[i].W + R) ) );
		result += (double)(w[i].dist - (R + w[i].W)*time) / (double)(w[i].W + S) + (double)time;
		t -= time;
	}
}

int main() {

	int T;
	fin >> T;
	
	for (int testcase=1;testcase<=T;testcase++) {
		input();
		solve();
		fout << "Case #" << testcase << ": " << fixed << setprecision(9) << result << "\n";
	}

	fin.close();
	fout.close();

	return 0;
}
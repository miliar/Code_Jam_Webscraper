#include <algorithm>
#include <iostream>
#include <climits>
#include <list>
#include <map>
#include <cmath>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <cstdio>
#include <string>
#include <cstring>
#include <vector>

using namespace std;

#define REP(i, n) for(int i=0; i<(int)(n); i++)
#define FOR(i, s, e) for (int i = (int)(s); i < (int)(e); i++)

bool check(const vector<double> &xs, const vector<double> &ys, const vector<double> &rs) {

    int N = xs.size();
    
    REP(i, N) FOR (j, i+1, N) {
	double x = xs[i] - xs[j];
	double y = ys[i] - ys[j];
	double r = rs[i] + rs[j];

	if (x*x + y*y < r*r)
	    return false;
    }
    return true;
}

void debug(const vector<double> &xs, const vector<double> &ys, const vector<double> &rs) {
    int N = xs.size();

    REP(i, N) FOR (j, i+1, N) {
	cout << i << " " << j << endl;
	double x = xs[i] - xs[j];
	double y = ys[i] - ys[j];
	double r = rs[i] + rs[j];
	
	cout << x*x + y*y << "     > " << r*r << endl;
    }
    
}

int main() {
    int T;

    cin >> T;
    REP(t, T) {
	int N;
	double W, L;
	cin >> N >> W >> L;

	vector<double> arms(N);
	REP(i, N)
	    cin >> arms[i];


	vector<double> xs(N);
	vector<double> ys(N);

	while (!check(xs, ys, arms)) {
	    int p = rand() % N;
	    xs[p] = 1.0 * rand() / RAND_MAX * W ;
	    ys[p] = 1.0 * rand() / RAND_MAX * L;
	}

	cout <<	"Case #" << t+1 << ": ";
	REP(i, N)
	    printf("%.18lf %.18lf ", xs[i], ys[i]);

	cout << endl;
	
//	debug(xs, ys, arms);
    }


    return 0;
}

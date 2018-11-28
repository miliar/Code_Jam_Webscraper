#include <iostream>
#include <cstring>
#include <cstdlib>
#include <cstdio>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <list>
#include <stack>
#include <deque>
#include <algorithm>
#include <cassert>
#include <cmath>
#include <ctime>
#include <cctype>

using namespace std;

#define all(v) (v).begin(), (v).end()

const double PI = 3.1415926535897932384626433832795;
const double EPS = 1e-9;
const int INF = (1 << 31) - 1;

typedef long long ll;
typedef pair<int, int> pii;


struct state {
    double begin, end, speed;
    state(double b, double e, double s) 
        : begin(b)
        , end(e)
        , speed(s)
    {}
    bool operator < (const state& rhs) {
        return speed > rhs.speed;
    }
};

void solveProblem() {
    double total_length;
    cin >> total_length;
    double your_walk;
    cin >> your_walk;
    double your_run;
    cin >> your_run;
    double max_run_time;
    cin >> max_run_time;
    int n;
    cin >> n;
    vector<state> v;
    double rem = total_length;
    for (int i = 0; i < n; ++i) {
        int b, e, s;
        cin >> b >> e >> s;
        v.push_back(state(b, e, s));
        rem -= e - b;
    }
    if (rem >= 0.5) {
        v.push_back(state(0, rem, 0));
    }
    sort(all(v));
    double res = 0;
    double remain_run = max_run_time;
    int size = 0;
    while(!v.empty()) {
        double begin = v.back().begin;
        double end = v.back().end;
        double speed = v.back().speed;
        v.pop_back();
        double length = end - begin;
        double run_time = length / (your_run + speed);
        run_time = min(run_time, remain_run);
        res += run_time;
        double where_end = begin + (your_run + speed) * run_time;
        remain_run -= run_time;
        if (where_end < end) {
            double must_walk = (end - where_end) / (your_walk + speed);
            res += must_walk;
        }
    }
    printf("%0.18lf\n", res);
}


int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int T;
    cin >> T;
    for (int test = 1; test <= T; ++test) {
        double t = clock();
        printf("Case #%d: ", test);
        solveProblem();
        t = (clock() - t) / CLOCKS_PER_SEC;
        cerr << test << " time " << t << " s\n";
    }
	return 0;
}

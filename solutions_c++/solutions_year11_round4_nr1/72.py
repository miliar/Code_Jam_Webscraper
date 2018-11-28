#define _CRT_SECURE_NO_WARNINGS
#pragma comment(linker, "/STACK:64000000")
#include <iostream>
#include <vector>
#include <algorithm>
#include <ctime>
#include <cmath>
#include <set>
#include <map>
#include <cassert>
#include <queue>
#include <deque>
#include <stack>
#include <sstream>
#include <cstring>
#include <string>
#include <functional>
#include <numeric>

using namespace std;

#define MP make_pair
#define all(v) (v).begin(), (v).end()

const int INF = ((1 << 31) - 1);
const long long LLINF = (((1LL << 63) - 1LL));
const double eps = 1e-9;
const double PI = 3.14159265358979323846;

typedef long long ll;

struct Walkway{
    int begin;
    int end;
    int speed;
    void read() {
        cin >> begin >> end >> speed;
    }
    bool operator < (Walkway A) const {
        return speed > A.speed;
    }
    double time(int v) {
        return 1.0 * (end - begin) / (v + speed);
    }
};

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
    int tests;
    cin >> tests;
    for (int test = 0; test < tests; ++test) {
        printf("Case #%d: ", test + 1);
        int X;
        cin >> X;
        double walk, run;
        cin >> walk >> run;
        double time_to_run;
        cin >> time_to_run;
        int n;
        cin >> n;
        vector<Walkway> w(n);;
        for (int i = 0; i < n; ++i)
            w[i].read();
        sort(all(w));
        reverse(all(w));
        
        int not_covered = X;
        for (int i = 0; i < w.size(); ++i)
            not_covered -= w[i].end - w[i].begin;
        double t = 0.0;

        double if_run = 1.0 * not_covered / (run);
        if (if_run <= time_to_run) {
            t += if_run;
            time_to_run -= if_run;
        } else {
            t += time_to_run;
            t += (not_covered - time_to_run * run) * 1.0 / (walk);
            time_to_run = 0.0;
        }

        for (int i = 0; i < n; ++i) {
            double if_run = (w[i].end - w[i].begin) * 1.0 / (w[i].speed + run);
            if (if_run <= time_to_run) {
                t += if_run;
                time_to_run -= if_run;
            } else {
                t += time_to_run;
                t += (w[i].end - w[i].begin - time_to_run * (w[i].speed + run)) * 1.0 / (w[i].speed + walk);
                time_to_run = 0.0;
            }
        }
        
        printf("%0.18lf", t);
        /*
        int cur_point = 0;
        int pos = 0;
        double t = 0;
        while(cur_point != X) {
            int next = X;
            bool is_walkway = pos < n && w[pos].begin == cur_point;
            if (pos < n && cur_point < w[pos].begin) {
                next = w[pos].begin;
            }
            if (is_walkway) {
                next = w[pos].end;
                int speed = w[pos].speed;
                double time_need_when_run = 1.0 * (next - cur_point) / (speed + run);
                if (time_need_when_run <= time_to_run) {
                    t += time_need_when_run;
                    cur_point = next;
                    time_to_run -= time_need_when_run;
                } else {
                    double we_run = time_to_run;
                    t += we_run;
                    t += 1.0 * (next - cur_point - we_run * (speed + run)) / (walk + speed);
                    //assert((next - cur_point - we_run * (speed + run)) >= 0.0);
                    cur_point = next;
                    time_to_run = 0;
                }
                ++pos;
                continue;
            } else {
                double time_need_when_run = 1.0 * (next - cur_point) / run;
                if (time_need_when_run <= time_to_run) {
                    t += time_need_when_run;
                    cur_point = next;
                    time_to_run -= time_need_when_run;
                    continue;
                } else {
                    double we_run = time_to_run;
                    t += we_run;
                    t += 1.0 * (next - cur_point - we_run * run) / walk;
                    cur_point = next;
                    time_to_run = 0;
                    continue;
                }
            }
        }*/

        printf("\n");
        cerr << test + 1 << " - th of " << tests << " completed!\n";
        cerr << 1.0 * clock() / CLOCKS_PER_SEC << " sec.\n";
    }
	return 0;
}
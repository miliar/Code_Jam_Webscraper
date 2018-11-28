#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>

#include <algorithm>
#include <bitset>
#include <functional>
#include <iostream>
#include <iterator>
#include <limits>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>

using namespace std;

#include <ext/numeric>
#include <ext/functional>
using namespace __gnu_cxx;

ostringstream message;
template<typename T>
void assert(bool t, const T& ign);
void parse_arguments(int argc, char* argv[], int& case_begin, int& case_end);

int n;
long long D;
long long P[201], V[201];

bool can(long long t) {
    long long free = P[0] - t;
    for (int i = 0; i < n; ++i) {
        long long v = V[i];
        long long span = (v-1) * D;
        long long left = max(P[i] - t, free);
        long long right = P[i] + t;
        if (right - left < span) { 
            //cout << "time is " << t << " " << free << endl;
            //cout << "span " << span << " " << left << " " << right  << endl;
            //cout << "failed because of " << i+1 << " " << P[i] << " " << V[i] << endl;
            return false;
        }
        free = left + span + D;
    }
    return true;
}

void process(int cur_case, bool solve_case){
    cin >> n >> D;
    D *= 2;
    for (int i = 0; i < n; ++i) {
        cin >> P[i] >> V[i];
        P[i] *= 2;
    }

    if (solve_case) {
        cerr << "Case #" << cur_case << endl;
        long long lo = -1, hi = 4000000LL * 4000000LL;
        while (lo + 1 < hi) {
            long long t = (lo + hi) / 2;
            if (can(t)) hi = t; else lo = t;
        }
        cout.precision(14);
        cout << "Case #" << cur_case << ": " << (long double)hi/2.0 << endl;
    }
}

void test() {

}

int main(int argc, char* argv[]) {
    int case_begin = 1;
    int case_end = 2000000000;
    parse_arguments(argc, argv, case_begin, case_end);
    int cases;
    cin >> cases;
    assert(case_begin <= cases, message << "empty test case range");
    cerr << "Solving cases [" << case_begin << ".." 
                              << min(case_end, cases+1) << ")" << endl;
    for (int cur_case = 1; cur_case <= cases; ++ cur_case) {
        process(cur_case, case_begin <= cur_case && cur_case < case_end);
    }
    return 0;
}

void parse_arguments(int argc, char* argv[], int& case_begin, int& case_end) {
    if (argc == 2 && string("test") == string(argv[1])) {
        test();
        exit(0);
    }
    else if (argc == 2) {
        sscanf(argv[1], "%d", &case_begin);
        case_end = case_begin + 1;
    } else if (argc == 3) {
        sscanf(argv[1], "%d", &case_begin);
        sscanf(argv[2], "%d", &case_end);
        assert(case_begin < case_end, 
               message << "invalid test case range: " 
                       << case_begin << " " 
                       << case_end << endl);
    } else if (argc > 1) {
        cerr << "invalid arguments " << endl;
        exit(1);
    }
}

template<typename T>
void assert(bool t, const T& ign) {
    if (!t) {
        cerr << "bug: "<< message.str() << endl;
        exit(1);
    }
    message.clear();
}
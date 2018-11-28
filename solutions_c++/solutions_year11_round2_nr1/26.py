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
string a[100];
pair<int,int> w[100];
double ow[100];
double oow[100];

pair<int, int> sum(vector<pair<int, int> > w){
    pair<int, int> total = make_pair(0, 0);
    for (int i = 0; i < n; ++i) {
        total.first += w[i].first;
        total.second += w[i].second;
    }
    return total;
}

void wins(){
    for (int i = 0; i < n; ++i) {
        int ww = 0, tt = 0;
        for (int j = 0; j < n; ++j) 
        if (j != i) {
            if (a[i][j]=='1') ww++, tt++;
            else if (a[j][i]=='1') tt++;
        }
        w[i] = make_pair(ww, tt);
    }
}

void owins(){
    for (int i = 0; i < n; ++i) {
        double x = 0;
        for (int j = 0; j < n; ++j) 
        if (j != i && a[i][j] == '1' || a[j][i] =='1') {
            int ww, tt;
            ww = w[j].first;
            tt = w[j].second;
            if (a[j][i]=='1') ww--;
            tt--;
            x += (double)ww / (double)tt;
        }
        ow[i] = x / w[i].second;
    }
}


void oowins(){
    for (int i = 0; i < n; ++i) {
        double x = 0;
        for (int j = 0; j < n; ++j)
        if (j != i && a[i][j] == '1' || a[j][i] == '1') x += ow[j];
        oow[i] = x / w[i].second;
    }
}

void process(int cur_case, bool solve_case){
    cin >> n;
    for (int i=0; i < n; ++i) cin >> a[i];

    if (solve_case) {
        wins();
        owins();
        oowins();
        cout << "Case #" << cur_case << ":" << endl;
        for (int i = 0; i < n; ++i) {
            double A = 0;
            A += 0.25*(double)w[i].first / (double)w[i].second;
            A += 0.50*(double)ow[i];
            A += 0.25*(double)oow[i];
            cout.precision(12);
            cout << A << endl;
        }
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
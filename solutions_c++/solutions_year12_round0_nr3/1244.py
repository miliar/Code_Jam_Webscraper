#include <vector> // headers {{{
#include <list>
#include <queue>
#include <set>
#include <map>
#include <string>
#include <sstream>
#include <iostream>
#include <algorithm>
#include <functional>
#include <numeric>
#include <cstdlib>
#include <cmath>
#include <cstdio>
#include <fstream>
#include <time.h>

using namespace std; // }}}

int result(int a, int b)
{
    //ofstream fcout("log.out");
    set<int> s;
    string cur, next;
    int cnt = 0;

    for (int i = a; i < b; ++i) {
        s.clear();
        stringstream ss0;
        ss0 << i;
        cur = ss0.str();
        for (int j = 1; j < cur.size(); ++j) {
            next = cur.substr(j) + cur.substr(0, j);
            int n = atoi(next.c_str());
            if (n <= b && n > i) {
                s.insert(n);
            }
        }
        /*vector<int> v(s.begin(), s.end());
        for (int k = 0; k < v.size(); ++k) {
            fcout << i << "\t" << v[k] << endl;
        }*/
        cnt+= s.size();
    }

    return cnt;
}

int main()
{
    //time_t start, end;
    //time(&start);

    ifstream fcin("test.in");
    ofstream fcout("test.out");
    int T;
    fcin >> T;

    for (int i = 0; i < T; ++i) {
        int A, B;
        fcin >> A >> B;
        fcout << "Case #" << i + 1 << ": " << result(A, B) << endl;
    }

    //time(&end);
    //cout << difftime(end, start) << endl;

    return 0;
}

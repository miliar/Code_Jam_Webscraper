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

vector<vector<int> > result(vector<int>& v)
{
    //ofstream fcout("log.out", ios::app);
    int n = v.size();
    map<int, int> M;
    vector<vector<int> > res;

    for (int i = 1; i < (1 << n); ++i) {
        int cur = 0;
        for (int j = 0; j < n; ++j) {
            if (i & (1 << j))
                cur+= v[j];
        }
        if (M.find(cur) != M.end()) {
            vector<int> vcur;
            for (int j = 0; j < n; ++j) {
                if (i & (1 << j))
                    vcur.push_back(v[j]);
            }
            res.push_back(vcur);
            vcur.clear();
            i = M[cur];
            for (int j = 0; j < n; ++j) {
                if (i & (1 << j))
                    vcur.push_back(v[j]);
            }
            res.push_back(vcur);
            return res;
        }
        M[cur] = i;
    }

    return res;
}

int main()
{
    //time_t start, end;
    //time(&start);

    ifstream fcin("test.in");
    ofstream fcout("test.out");
    //fcout.precision(6);
    //fcout.setf(ios::fixed,ios::floatfield);

    int T;
    fcin >> T;

    for (int i = 0; i < T; ++i) {
        int N;
        fcin >> N;
        vector<int> v;
        int cur;
        for (int j = 0; j < N; ++j) {
            fcin >> cur;
            v.push_back(cur);
        }
        fcout << "Case #" << i + 1 << ":" << endl;
        vector<vector<int> > vv = result(v);
        if (vv.empty())
            fcout << "Impossible" << endl;
        else
            for (int j = 0; j < vv.size(); ++j) {
                for (int k = 0; k < vv[j].size(); ++k) {
                    fcout << (k ? " " : "") << vv[j][k];
                }
                fcout << endl;
            }

    }

    //time(&end);
    //cout << difftime(end, start) << endl;

    return 0;
}

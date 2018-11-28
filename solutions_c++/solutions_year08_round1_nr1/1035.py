#include <iostream>
#include <fstream>
#include <cstdio>
#include <climits>
#include <algorithm>
#include <vector>
#include <string>

using namespace std;

#define FOR(_i,a,b) for(int _i=a;_i<b;_i++)
#define REP(_i,n) for(int _i=0;_i<n;_i++)

typedef vector<int> VI;
typedef vector<string> VS;
typedef vector<VI> VVI;

VS tokenize(string s, string ch) {
    VS ret;
    for (int p = 0, p2; p < s.size(); p = p2+1) {
        p2 = s.find_first_of(ch, p);
        if (p2 == -1) p2 = s.size();
        if (p2-p > 0) ret.push_back(s.substr(p, p2-p));
    }
    return ret;
}

VI tokenize_int(string s, string ch) {
  VI ret;
  VS p = tokenize(s, ch);
  for( int i = 0; i < p.size(); i++ )
    ret.push_back(atoi(p[i].c_str()));
  return ret;
}

long long solve(VI &v1, VI &v2, int n) {
    long long min_prod = 0;

    // Initial guess
    REP(i, n) {
        min_prod += (v1[i]*v2[i]);
    }

    // Iterative improvement
    bool swapped;
    while (true) {
        swapped = false;
        REP(i1, n) {
             FOR(i2, i1+1, n) {
                if (v1[i1]*v2[i2] + v1[i2]*v2[i1] < v1[i1]*v2[i1] + v1[i2]*v2[i2]) {
                    min_prod -= (v1[i1]*v2[i1] + v1[i2]*v2[i2]);
                    int temp = v2[i2];
                    v2[i2] = v2[i1];
                    v2[i1] = temp;
                    min_prod += (v1[i1]*v2[i1] + v1[i2]*v2[i2]);
                    swapped = true;
                }
            }
        }
        if (!swapped) {
            break;
        }
    }

    return min_prod;
}

int main(int argc, char** argv) {
    ifstream input(argv[1]);
    string line;
    int t;
    input >> t; input.get();
    REP(i, t) {
        int n;
        input >> n; input.get();
        getline(input, line);
        VI v1 = tokenize_int(line, " ");
        getline(input, line);
        VI v2 = tokenize_int(line, " ");
        cout << "Case #" << i+1 << ": " << solve(v1, v2, n) << endl;
    }
    return 0;
}

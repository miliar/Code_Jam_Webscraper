#include <vector>
#include <iostream>
#include <sstream>
#include <algorithm>
#include <stdio.h>
#include <math.h>
#include <set>
#include <map>

using namespace std;

// BEGIN CUT HERE

template<typename T> std::ostream& operator<<(std::ostream& os, const vector<T> &v) {
        os << "[";
        int N = v.size();
        for (int i = 0; i < N; i++) {
                os << v[i];
                if (i != (N - 1)) os << ", ";
        }
        os << "]" << endl;
}

// END CUT HERE

// O(n)
long double getWP(vector<string> &inputs, int me, int omit) {
        int nGames = 0;
        int nWon = 0;
        for (int j = 0; j < inputs.size(); j++) {
                if (j == omit) continue;
                if (inputs[me][j] != '.') {
                        nGames++;
                        if (inputs[me][j] == '1') {
                                nWon++;
                        }
                }
        }
        long double wp = 0;
        if (nGames != 0) wp = (long double)nWon / nGames;
//        cerr << "WP of " << me << " omitting " << omit << ": " << wp << endl;
        return wp;
}

int main() {
        cout.precision(12);

        int T;
        cin >> T;
        for (int t = 1; t <= T; t++) {
                int n;
                cin >> n;
                vector<string> inputs(n);
                for (int i = 0; i < n; i++) {
                        cin >> inputs[i];
                }
                cout << "Case #" << t << ":" << endl;
                
                vector <long double> wps(n), owps(n);
                vector <int> nOpponents(n);
                for (int i = 0; i < n; i++) {
                        wps[i] = getWP(inputs, i, -1);
                        
                        nOpponents[i] = 0;
                        owps[i] = 0;
                        for (int j = 0; j < n; j++) {
                                if (inputs[i][j] != '.') { 
                                        nOpponents[i]++;
                                        owps[i] += getWP(inputs, j, i);
                                }
                        }
                        if (nOpponents[i] != 0) owps[i] /= nOpponents[i];
                }
                for (int i = 0; i < n; i++) {
                        long double rpi = 0.25 * wps[i] + 0.5 * owps[i];
                        long double oowp = 0;
                        for (int j = 0; j < n; j++) {
                                if (inputs[i][j] != '.') {
                                        oowp += owps[j];
                                }
                        }
                        if (nOpponents[i] != 0) oowp /= nOpponents[i];
                        rpi += 0.25 * oowp;
                        cout << rpi << endl;
                }
                                
        }

        return 0;

}


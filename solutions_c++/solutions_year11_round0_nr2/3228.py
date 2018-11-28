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

int main() {
        int T;
        cin >> T;
        for (int t = 1; t <= T; t++) {
                bool opposed[256][256] = {};
                char combineTo[256][256] = {};
                
                int C;
                cin >> C;
                for (int i = 0; i < C; i++) {
                        string tmp;
                        cin >> tmp;
                        combineTo[tmp[0]][tmp[1]] = tmp[2];
                        combineTo[tmp[1]][tmp[0]] = tmp[2];
                }
                int D;
                cin >> D;
                for (int i = 0; i < D; i++) {
                        string tmp;
                        cin >> tmp;
                        opposed[tmp[0]][tmp[1]] = true;
                        opposed[tmp[1]][tmp[0]] = true;
                }

                int N;
                cin >> N;
                string tmp;
                cin >> tmp;
                vector <char> ans;
                for (int i = 0; i < N; i++) {
                        char c = tmp[i];
                        // check combination
                        if (ans.size() > 0) {
                                char last = ans.back();
                                if (combineTo[c][last] != 0) {
                                        ans.pop_back();
                                        c = combineTo[c][last];
                                }
                        }
                        // check opposition
                        bool opposition = false;
                        for (char j = 'A'; j <= 'Z'; j++) {
                                if (opposed[c][j] && 
                                    find(ans.begin(), ans.end(), j) != ans.end()) {
                                        opposition = true;
                                }
                        }
                        if (opposition) {
                                ans.clear();
                        } else {
                                ans.push_back(c);
                        }
                }

                cout << "Case #" << t << ": [";
                for (int i = 0; i < ans.size(); i++) {
                        if (i != 0) cout << ", ";
                        cout << ans[i];
                }
                cout << "]" << endl;
        }

        return 0;        
}


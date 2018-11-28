#include <vector>
#include <iostream>
#include <map>
#include <algorithm>
#include <cassert>
#include <string>

using namespace std;

typedef pair<int, int> pii;

typedef long long int i64;

i64 count(const map<int, int>& mp, int delta) {
    int alternatives = 0;

    typedef map<int, int>::const_iterator It;


    i64 tgt_in_alternatives = 0;
    i64 ans = 0;

    for (It from = mp.begin(), to = mp.begin(); from != mp.end(); ++from) {
        while (to != mp.end() && to->first < from->first + delta) {
            alternatives += to->second;
            if( to->first == delta / 2) {
                tgt_in_alternatives = to->second;
            }
            ++to;
        }

        //assert (alternatives > 0);

        if (from->second) {
            i64 dt = i64(alternatives - from->second) * from->second * 3 * 4;
            if (from->first == delta / 2) {
                dt /= 3;
            } else {
                dt = i64(alternatives - from->second - tgt_in_alternatives) * from->second * 3 * 4;
                dt +=  i64(tgt_in_alternatives) * from->second * 3 * 4 / 3;
            }
            ans += dt;

            if (from->second > 1) {
                i64 dq = from->second * (from->second - 1) * 3 * 4 / 2;
                if (from->first == delta / 2) {
                    dq /= 6;
                }

                if (from->first <= delta/ 2) {
                    ans += dq;
                }
            }
        }

        alternatives -= from->second;
        if( from->first == delta / 2) {
                tgt_in_alternatives = 0;
            }
    }
    
    return ans;
}

i64 solve(vector<int> v) {
    map<int, int> counts;

    for(int i = 0; i < v.size(); ++i) {
        ++counts[v[i]];
    }

    i64 ans = 0;

    /*
    for (map<int, int>::iterator it = counts.begin(); it != counts.end(); ++it) {
        for (map<int, int>::iterator jt = counts.begin(); jt != it; ++jt) {
            if (it->second >= 2 && jt->second >= 2) {
                --ans;
            }
        }
    }

    std::cout << "after correction: " << ans << std::endl;*/

    for (map<int, int>::iterator it = counts.begin(); it != counts.end(); ++it) {
        if (it->second >= 2) {
            it->second -= 2;

            i64 cnt = count(counts, it->first * 2);
           // std::cout << "when edges are " << it->first << ": " << cnt << std::endl;

            it->second += 2;

            ans += cnt * it->second * (it->second - 1) / 2 / 3 / 4;
        }
    }

    return ans;
}

bool check(std::vector<string> v, char c) {
    for (string& s : v) {
        for (char& cx : s) {
            if (cx == 'T') {
                cx = c;
            }
        }
    }
    if (find(v.begin(), v.end(), string(4, c)) != v.end()) {
        return true;
    }

    bool ok = true;
    for (int i = 0; i< 4; ++i) {
        ok &= v[i][i] == c;
    }
    if (ok) return true;

    ok = true;
    for (int i = 0; i< 4; ++i) {
        ok &= v[i][3-i] == c;
    }
    if (ok) return true;

    for (int j = 0; j < 4; ++j) {
        ok = true;
        for (int i = 0; i< 4; ++i) {
            ok &= v[i][j] == c;
        }
        if (ok) return true;
    }

    return false;
}

bool draw(const vector<string> v) {
    auto s=  v[0] + v[1] + v[2]+ v[3];
    return find(s.begin(), s.end(), '.') == s.end();
}

int main() {
    freopen("c:/var/tmp/in.txt", "r", stdin);
    freopen("c:/var/tmp/out.txt", "w", stdout);

    int t; cin >> t;

    for (int i= 0; i < t; ++i) {
        std::vector<string> v(4);
        for (auto& s : v) {
            cin >> s;
        }

        cout << "Case #" << (i + 1) << ": ";
        if (check(v, 'X')) {
            cout << "X won" << std::endl;
        } else if (check(v, 'O')) {
            cout << "O won" << std::endl;
        } else if (draw(v)) {
            cout << "Draw" << std::endl;
        } else {
            cout << "Game has not completed" << std::endl;
        }
    }
    
}
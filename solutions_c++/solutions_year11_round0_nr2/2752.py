#include <iostream>
#include <sstream>
#include <vector>
using namespace std;

int main() {
    int n;
    cin >> n;
    for(int tcs = 1; tcs <= n; ++tcs) {
        cout << "Case #" << tcs << ": ";
        int y;
        string s;
        vector<int> v(26, -1);
        vector< vector<int> > COMBINE(26, v);
        vector< vector<int> > OPPOSED(26, v);
        vector<int> e_list, e_mark(26, 0), e_clear(26, 0);
        cin >> y;
        while(y--) {
            cin >> s;
            COMBINE[s[0] - 'A'][s[1] - 'A'] = s[2] - 'A';
            COMBINE[s[1] - 'A'][s[0] - 'A'] = s[2] - 'A';
        }
        cin >> y;
        while(y--) {
            cin >> s;
            OPPOSED[s[0] - 'A'][s[1] - 'A'] = 1;
            OPPOSED[s[1] - 'A'][s[0] - 'A'] = 1;
        }
        cin >> y >> s;
        for(int i = 0; i < y; ++i) {
            e_list.push_back(s[i] - 'A');
            ++e_mark[e_list[e_list.size() - 1]];
            while(e_list.size() >= 2) {
                int e1 = e_list[e_list.size() - 2];
                int e2 = e_list[e_list.size() - 1];
                int e3 = COMBINE[e1][e2];
                if(e3 != -1) {
                    --e_mark[e1];
                    --e_mark[e2];
                    ++e_mark[e3];
                    e_list.pop_back();
                    e_list.pop_back();
                    e_list.push_back(e3);
                } else {
                    break;
                }
            }
            for(int i = 0; i < 26; ++i) {
                if(e_mark[i] != 0) {
                    for(int j = 0; j < 26; ++j) {
                        if(e_mark[j] != 0) {
                            if(OPPOSED[i][j] == 1) {
                                e_list.clear();
                                e_mark = e_clear;
                                goto ROUND_END;
                            }
                        }
                    }
                }
            }
ROUND_END:
            ;
        }
        cout << "[";
        if(e_list.size() > 0) {
            cout << char(e_list[0] + 'A');
            for(unsigned i = 1; i < e_list.size(); ++i) {
                cout << ", " << char(e_list[i] + 'A');
            }
        }
        cout << "]" << endl;
    }
    return 0;
}

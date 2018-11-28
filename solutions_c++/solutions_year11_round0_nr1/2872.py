#include <iostream>
#include <vector>
using namespace std;

enum {ORANGE, BLUE};

int main() {
    int n;
    cin >> n;
    for(int tcs = 1; tcs <= n; ++tcs) {
        cout << "Case #" << tcs << ": ";
        int m;
        cin >> m;
        vector<int> O, B, S;
        string color;
        int button;
        while(m--) {
            cin >> color >> button;
            if(color == "O") {
                O.push_back(button);
                S.push_back(0);
            } else {
                B.push_back(button);
                S.push_back(1);
            }
        }
        int pos_o, pos_b, second = 0, index = 0, x_o = 0, x_b = 0;
        pos_o = pos_b = 1;
        while(index < (int)S.size()) {
            ++second;
            if(S[index] == ORANGE) {
                if(x_o < (int)O.size()) {
                    if(pos_o == O[x_o]) {
                        ++index;
                        ++x_o;
                    } else {
                        if(pos_o > O[x_o]) {
                            --pos_o;
                        } else {
                            ++pos_o;
                        }
                    }
                }
                if(x_b < (int)B.size()) {
                    if(pos_b == B[x_b]) {
                    } else {
                        if(pos_b > B[x_b]) {
                            --pos_b;
                        } else {
                            ++pos_b;
                        }
                    }
                }
            } else {
                if(x_o < (int)O.size()) {
                    if(pos_o == O[x_o]) {
                    } else {
                        if(pos_o > O[x_o]) {
                            --pos_o;
                        } else {
                            ++pos_o;
                        }
                    }
                }
                if(x_b < (int)B.size()) {
                    if(pos_b == B[x_b]) {
                        ++index;
                        ++x_b;
                    } else {
                        if(pos_b > B[x_b]) {
                            --pos_b;
                        } else {
                            ++pos_b;
                        }
                    }
                }
            }
        }
        cout << second << endl;
    }
    return 0;
}

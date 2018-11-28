#include <cstdlib>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <iostream>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <iomanip>
#include <fstream>
using namespace std;

bool same(string t1, string t2) {
    int len = t1.size();
    for (int i = 0; i < len; i++) {
        if (t1[i] != t2[i]) return false;
    }
    return true;
}

int main() {
        freopen("B-small-attempt0.in", "r", stdin);
        freopen("out.txt", "w", stdout);
    int t;
    int n, m;
    scanf("%d", &t);
    for (int i = 0; i < t; i++) {
        scanf("%d%d", &n, &m);
        vector<string>v[12];
        string str[1000];
        for (int i = 0; i < n; i++) {
            cin >> str[i];
            v[str[i].size()].push_back(str[i]);
        }
        printf("Case #%d:", i + 1);
        for (int i = 0; i < m; i++) {
            string list;
            cin >> list;
            int len = list.size();
            int maxn = -1;
            int place = 100000;
            for (int i = 1; i <= 10; i++) {
                int num = v[i].size();
                string cmp;
                for (int l = 0; l < i; l++) cmp.append(1, '?');
                string res[1000];
                for (int j = 0; j < num; j++) {
                    int cnt = 0;
                    for (int j = 0; j < num; j++) {
                        res[j] = cmp;
                    }
                    string tmp = v[i][j];
                    for (int k = 0; k < len; k++) {
                        char now = list[k];
                        bool find = false;
                        for (int l = 0; l < i; l++) {
                            if (tmp[l] == now) {
                                find = true;
                                res[j][l] = now;
                            }
                        }
                        if (find) {
                            for (int t = 0; t < num; t++) {
                                if (t != j) {
                                    for (int l = 0; l < i; l++) {
                                        if (v[i][t][l] == now) {
                                            res[t][l] = now;
                                        }
                                    }
                                }
                            }
                        } else {
                            bool can = false;
                            for (int t = 0; t < num; t++) {
                                if (t != j && res[t] == res[j]) {
                                    for (int l = 0; l < i; l++) {
                                        if (v[i][t][l] == now) {
                                            can = true;
                                            res[t][l] = now;
                                        }
                                    }
                                }
                            }
                            if (can) cnt++;
                        }
                    }
                    if (cnt > maxn) {
                        maxn = cnt;
                        for (int i = 0; i < n; i++) {
                            if (tmp == str[i]) {
                                place = i;
                                break;
                            }
                        }
                    } else if (cnt == maxn) {
                        for (int i = 0; i < n; i++) {
                            if (tmp == str[i]) {
                                place = min(place, i);
                                break;
                            }
                        }
                    }
                    // printf("%s %d\n", v[i][j].c_str(), cnt);
                }
            }
            cout << " " << str[place];
        }
        cout << endl;
    }
    return 0;
}


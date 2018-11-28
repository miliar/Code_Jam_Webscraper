/*
 * Author: code6
 * Created Time:  2011/5/21 10:02:35
 * File Name: B.cpp
 */
#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <algorithm>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <queue>
#include <bitset>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <ctime>
#include <string>

using namespace std;
#define out(v) cerr << #v << ": " << (v) << endl
#define SZ(v) ((int)(v).size())
const int maxint = -1u>>1;
template <class T> bool get_max(T& a, const T &b) {return b > a? a = b, 1: 0;}
template <class T> bool get_min(T& a, const T &b) {return b < a? a = b, 1: 0;}
typedef long long ll;
const double PI=acos(-1.0);
const double eps=1e-11;

vector<string> vd;
int point[10000+50];
int n, m;

int main() {
    
    freopen("B-small-attempt0.in", "r", stdin);
    freopen("B.out", "w", stdout);
    
    int t, cas = 0;
    cin>>t;
    while (t--) {
        cas++;
        cin>>n>>m;
        vd.clear();
        int i, j, k, u;
        for (i = 0; i < n; i++) {
            string st;
            cin>>st;
            vd.push_back(st);
        }
        printf("Case #%d:", cas);
        while (m--) {
            memset(point, 0, sizeof(point));
            string st;
            cin>>st;
            
            int best = -1;
            string ans;
            for (i = 0; i < vd.size(); i++) {
                string cs = vd[i];
                
                vector<int>cand;
                bool vis[26];
                memset(vis, 0, sizeof(vis));
                for (j = 0; j < vd.size(); j++) {
                    if (vd[j].size() == cs.size()) {
                        cand.push_back(j);
                        for (k = 0; k < vd[j].size(); k++) {
                            vis[vd[j][k] - 'a'] = true;
                        }
                    }
                }
                
                char rev[26];
                int ct = 0;
                memset(rev, -1, sizeof(rev));
                
                int lose = 0;
                
                for (j = 0; j < st.size(); j++) {
                    if (!vis[st[j] - 'a']) {
                        continue;
                    }
                    
                    bool found = false;
                    for (k = 0; k < cs.size(); k++) {
                        if (cs[k] == st[j]) {
                            rev[k] = st[j];
                            found = true;
                            ct++;
                        }
                    }
                    
                    //printf("\nAt round %d, cand size = %d:\n", j, cand.size());
                    //for (k = 0; k < cand.size();k++)
                        //printf("%s\n", vd[cand[k]].c_str());
                    
                    vector<int> ncand;
                    
                    if (!found) {
                        //printf("lose 1 point, ch = %c vis=%d\n", st[j], vis[st[j] - 'a']);
                       lose++; 
                       for (k = 0; k < cand.size(); k++) {
                           int at = cand[k];
                            for (u = 0; u < vd[at].size(); u++) {
                                if (vd[at][u] == st[j]) {
                                    break;
                                }
                            }
                           if (u == vd[at].size()) {
                                ncand.push_back(cand[k]);
                           }
                       }
                    } else {
                       for (k = 0; k < cand.size(); k++) {
                           int at = cand[k];
                            for (u = 0; u < vd[at].size(); u++) {
                                if ((vd[at][u] == st[j]) != (rev[u] == st[j])) {
                                    break;
                                }
                            }
                           if (u == vd[at].size()) {
                                ncand.push_back(cand[k]);
                           }
                       }
                    }
                    cand = ncand;
                    
                    memset(vis, 0, sizeof(vis));
                    for (k = 0; k < cand.size(); k++) {
                        int at = cand[k];
                        for (u = 0; u < vd[at].size(); u++) {
                            vis[vd[at][u] - 'a'] = true;
                        }
                    }
                    
                    if (ct == cs.size()) {
                        break;
                    }
                }
                
                //printf("M = %d, string = %s, lose = %d\n", m, vd[i].c_str(), lose);
                
                if (lose > best) {
                    best = lose;
                    ans = vd[i];
                }
            }
            
            printf(" %s", ans.c_str());
        }
        putchar('\n');
    }
    return 0;
}


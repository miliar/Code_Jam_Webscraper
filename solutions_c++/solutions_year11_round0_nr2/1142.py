//head               
#include <cstdlib>   
#include <cstring>   
#include <memory>    
#include <cstdio>    
#include <fstream>   
#include <iostream>  
#include <cmath>     
#include <string>    
#include <sstream>   
#include <stack>     
#include <queue>     
#include <vector>    
#include <set>       
#include <map>       
#include <algorithm> 
#include <deque>     
#include <list>      
                     
using namespace std; 

const int MAXN = 26;
int cnt[MAXN];
stack<char> sta;

inline void clear() {
    memset(cnt, 0, sizeof(cnt));
    while (!sta.empty()) {
        sta.pop();
    }
}

inline void insert(char ch) {
    ++cnt[ch - 'A'];
    sta.push(ch);
}

inline void pop() {
    --cnt[sta.top() - 'A'];
    sta.pop();
}

int main () {
    freopen("B-small-attempt0.in", "r", stdin);
    freopen("B-small-attempt0.out", "w", stdout);
    int T, C, D, N;
    scanf("%d", &T);
    for (int nCase = 1; nCase <= T; ++nCase) {
        map<char, pair<char, char> > form;
        map<char, char> dis;
        scanf("%d", &C);
        char str[128];
        for (int i = 0; i < C; ++i) {
            scanf("%s", str);
            form[str[0]] = make_pair(str[1], str[2]);
            form[str[1]] = make_pair(str[0], str[2]);
        }
        scanf("%d", &D);
        for (int i = 0; i < D; ++i) {
            scanf("%s", str);
            dis[str[0]] = str[1];
            dis[str[1]] = str[0];
        }
        scanf("%d", &N);
        scanf("%s", str);
        clear();
        for (int i = 0; i < N; ++i) {
            if (sta.empty()) {
                insert(str[i]);
            }
            else{
                if (form.find(str[i]) != form.end()) {
                    pair<char, char> P = form[str[i]];
                    if (sta.top() == P.first) {
                        pop();
                        insert(P.second);
                    }
                    else if (dis.find(str[i]) != dis.end()) {
                        char ch = dis[str[i]];
                        if (cnt[ch - 'A'] > 0) {
                            clear();
                        }
                        else {
                            insert(str[i]);
                        }
                    }
                    else {
                        insert(str[i]);
                    }
                }
                else if (dis.find(str[i]) != dis.end()) {
                    char ch = dis[str[i]];
                    if (cnt[ch - 'A'] > 0) {
                        clear();
                    }
                    else {
                        insert(str[i]);
                    }
                }
                else {
                    insert(str[i]);
                }
            }
        }
        vector<char> vec;
        while (!sta.empty()) {
            vec.push_back(sta.top());
            sta.pop();
        }
        reverse(vec.begin(), vec.end());
        printf("Case #%d: [", nCase);
        for (int i = 0; i < vec.size(); ++i) {
            if (i != 0) {
                printf(", ");
            }
            printf("%c", vec[i]);
        }
        printf("]\n");
    }
    return 0;
}



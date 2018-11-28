#include <iostream>
#include <stdio.h>
#include <vector>
using namespace std;

typedef pair<int,int> pii;
int T,N;
char c;
int cur;
int cur_b,cur_o;
int idx_b;
int idx_o;
int idx;
vector<int> blue;
vector<int> orange;
vector<pii> both;

void moveOrange() {
    if (idx_o < orange.size()) {
        if (cur_o < orange[idx_o])
            cur_o++;
        if (cur_o > orange[idx_o])
            cur_o--;
    } 
}

void moveBlue() {
    if (idx_b < blue.size()) {
        if (cur_b < blue[idx_b])
            cur_b++;
        if (cur_b > blue[idx_b])
            cur_b--;
    } 
}

void solve(int caseno) {
    cin >> N;
    orange.clear();
    blue.clear();
    both.clear();
    for (int i = 0; i < N; ++i) {
        cin >> c >> cur;
        --cur;
        if (c == 'O')
            orange.push_back(cur);
        if (c == 'B')
            blue.push_back(cur);
        both.push_back(pii(c,cur));
        //printf("cur=%d\n",cur);
    }

    cur_b = 0;
    cur_o = 0;
    cur = 0;
    idx_b = 0;
    idx_o = 0;
    idx = 0;
    int moves = 0;
    while (idx < both.size()) {
        //printf("orange: %d blue: %d\n",cur_o,cur_b);
        if (both[idx].first == 'B') {
            if (both[idx].second > cur_b) {
                cur_b++;
            } else if (both[idx].second < cur_b) {
                cur_b--;
            } else { // ==
                idx_b++;
                idx++;
            }
            moveOrange();
        } else {
            if (both[idx].second > cur_o) {
                cur_o++;
            } else if (both[idx].second < cur_o) {
                //printf("%d < %d\n",both[idx].second,cur_o);
                cur_o--;
            } else { // ==
                idx_o++;
                idx++;
            }

            moveBlue();
        }
        ++moves;
    }

    printf("Case #%d: %d\n",caseno,moves);
}

int main() {
    cin >> T;
    for (int i = 0; i < T; ++i) {
        solve(i+1);
    }
    return 0;
}
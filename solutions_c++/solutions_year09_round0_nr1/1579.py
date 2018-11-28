#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <queue>
using namespace std;

int main() {
    
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    
    int L, D, N;
    
    scanf("%d%d%d", &L, &D, &N);
    
    vector<string> dic(D);
    
    for(int i = 0; i < D; ++i)
        cin >> dic[i];
    
    for(int c = 1; c <= N; ++c) {
        string s;
        cin >> s;
        vector<string> pattern(0);
        for(int i = 0; i < L; ++i) {
            if(s[0] != '(') {
                pattern.push_back(s.substr(0, 1));
                s.erase(0, 1);
            }
            else {
                int pos = s.find(')');
                pattern.push_back(s.substr(1, pos - 1));
                s.erase(0, pos + 1);
            }
        }
        int ans = 0;
        for(int i = 0, j; i < D; ++i) {
            for(j = 0; j < L; ++j) {
                if(pattern[j].find(dic[i][j]) == string::npos)
                    break;
            }
            if(j == L) ++ans;
        }
        printf("Case #%d: %d\n", c, ans);
    }
    return 0;
}

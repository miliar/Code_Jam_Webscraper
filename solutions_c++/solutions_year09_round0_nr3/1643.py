#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <queue>
using namespace std;

int main() {
    
    freopen("C-small-attempt0.in", "r", stdin);
    freopen("C-small.out", "w", stdout);
  
    int T;
    
    scanf("%d ", &T);
    
    string pattern = "welcome to code jam";

    vector<int> C[19];

    for(int c = 1; c <= T; ++c) {
        string s;
        getline(cin, s);
        int len = 0;
        for(int i = 0; i < s.size(); ++i)
            if(pattern.find(s[i]) != string::npos)
                s[len++] = s[i];
        s.erase(len);
        
        for(int i = 0; i < 19; ++i)
            C[i] = vector<int>(len, 0);
        
        int ans = 0;
        
        for(int i = 0; i < 19; ++i)
            if(s[i] == 'w')
                C[0][i] = 1;
        
        for(int i = 1; i < 19; ++i) {
            for(int j = 0; j < len; ++j) {
                if(!C[i-1][j]) continue;
                for(int k = j + 1; k < len; ++k) {
                    if(pattern[i] == s[k]) {
                        C[i][k] += C[i-1][j];
                        C[i][k] %= 10000;
                        if(i == 18) {
                            ans += C[i-1][j];
                            ans %= 10000;
                        }
                    }
                }
            }
        }
        
        printf("Case #%d: %04d\n", c, ans);
    }
    
    return 0;
}

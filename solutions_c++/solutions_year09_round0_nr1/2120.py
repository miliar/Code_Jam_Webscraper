#include <cstdio>
#include <vector>
#include <algorithm>
#include <iostream>
#include <sstream>
#include <cstring>
#include <string>
using namespace std;

bool match(const string& pattern, const string& word) {
    int j = 0;
    for (unsigned int i = 0; i < word.length(); i++, j++) {
        if (pattern[j] == '(') {
            bool match = false;
            ++j;
            for (; pattern[j] != ')'; j++) {
                if (pattern[j] == word[i]) match = true;
            }
            if (!match) return false;
        } else {
            if (pattern[j] != word[i]) return false;
        }
    }
    return true;
}

int main() {
    int l, d, n;
    scanf("%d %d %d", &l, &d, &n);
    
    vector<string> dict(d);
    for (int i = 0; i < d; i++) {
        char buf[20]; scanf("%s", buf); dict[i] = buf;
    }
    
    for (int i = 1; i <= n; i++) {
        int ans = 0;
        
        char buf[30*15];
        scanf("%s", buf);
        string s = buf;
        for (int j = 0; j < d; j++) {
            if (match(s, dict[j])) ans++;
        }
        
        printf("Case #%d: %d\n", i, ans);
    }
}

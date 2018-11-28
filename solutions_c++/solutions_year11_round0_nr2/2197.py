#include <iostream>
#include <stdio.h>
#include <string.h>
#include <string>
#include <map>

using namespace std;

string ans;
bool g[26][26];
map <string, char> h;

bool find(char c)
{
    for (int i = 0; i < ans.length(); i++)
        if (g[ans[i] - 'A'][c - 'A']) return true;
    return false;
}

int main()
{
    int t, cases, c, i, d, n;
    char temp;
    string s, s1;
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    scanf("%d", &t);
    for (cases = 1; cases <= t; cases++) {
        h.clear();
        scanf("%d", &c);
        for (i = 1; i <= c; i++) {
            cin >> s;
            h[s.substr(0, 2)] = s[2];
            temp = s[0]; s[0] = s[1]; s[1] = temp;
            h[s.substr(0, 2)] = s[2];
        }
        memset(g, false, sizeof(g));
        scanf("%d", &d);
        for (i = 1; i <= d; i++) {
            cin >> s;
            g[s[0] - 'A'][s[1] - 'A'] = true; g[s[1] - 'A'][s[0] - 'A'] = true;
        }
        scanf("%d", &n);
        cin >> s;
        ans = "";
        for (i = 0; i < s.length(); i++)
            if (ans.empty()) ans += s[i];
            else {
                s1 = ans[ans.length() - 1]; s1 += s[i];
                if (h.find(s1) != h.end()) ans[ans.length() - 1] = h[s1];
                else if (find(s[i])) ans = "";
                     else ans += s[i];
            }
        printf("Case #%d: [", cases);
        if (ans.length() > 1)
            for (i = 0; i < ans.length() - 1; i++) printf("%c, ", ans[i]);
        if (ans.length() > 0) printf("%c]\n", ans[ans.length() - 1]);
        else printf("]\n");
    }
    return 0;
}

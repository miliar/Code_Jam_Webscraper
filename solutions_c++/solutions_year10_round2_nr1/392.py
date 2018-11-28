# include <iostream>
# include <cstdio>
# include <cstring>
# include <vector>
# include <set>
# include <queue>
# include <string>
using namespace std;

int main()
{
    int t, n, m, i, j, p, ans;
    string str, temp;
    scanf("%d", &t);
    for (int tt = 1; tt <= t; tt++) {
        ans = 0;
        set <string> s;
        scanf("%d%d", &n, &m);
        for (i = 0; i < n; i++) {
            cin >> str;
            s.insert(str);
        }
        for (i = 0; i < m; i++) {
            cin >> str;
            p = str.size();
            temp = "/";
            for (j = 1; j < p;) {
                while (j < p && str[j] != '/') {
                    temp.push_back(str[j]);
                    j++;
                }
                j++;
                if (s.find(temp) == s.end()) {
                    ans++;
                    s.insert(temp);
                }
                if (j < p) {
                    temp.push_back('/');
                }
            }
        }
        printf("Case #%d: %d\n", tt, ans);
    }
    return 0;
}

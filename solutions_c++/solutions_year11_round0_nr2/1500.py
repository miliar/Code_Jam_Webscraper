# include <iostream>
# include <cstdio>
# include <string>
# include <vector>
# include <map>
# include <cstring>
using namespace std;

char f(char c)
{
    return c - 'A';
}

int main()
{
    int t, tt, i, j, n, c, d;
    string str, temp, ans;
    char cs[30][30], ds[30][30], ca, cb;

    tt = 1;
    cin >> t;
    while(t--) {
        memset(cs, 0, sizeof cs);
        memset(ds, 0, sizeof ds);
        ans = "";

        cin >> c;
        for (i = 0; i < c; i++) {
            cin >> temp;
            cs[f(temp[0])][f(temp[1])] = temp[2];
            cs[f(temp[1])][f(temp[0])] = temp[2];
        }

        cin >> d;
        for (i = 0; i < d; i++) {
            cin >> temp;
            ds[f(temp[0])][f(temp[1])] = ' ';
            ds[f(temp[1])][f(temp[0])] = ' ';
        }

        cin >> n;
        cin >> str;
        for (i = 0; i < n; i++) {
            if ((int) ans.size() == 0) {
                ans.push_back(str[i]);
            }
            else {
                ca = f(ans[ans.size() - 1]);
                cb = f(str[i]);

                if (cs[ca][cb] != 0) {
                    ans[ans.size() - 1] = cs[ca][cb];
                }
                else {
                    for (j = 0; j < (int) ans.size(); j++) {
                        ca = f(ans[j]);
                        cb = f(str[i]);

                        if (ds[ca][cb] != 0) {
                            ans = "";
                            break;
                        }
                    }

                    if (ans != "") {
                        ans.push_back(str[i]);
                    }
                }
            }
        }

        printf("Case #%d: [", tt++);
        for (i = 0; i < (int) ans.size(); i++) {
            printf("%s%c", i == 0 ? "" : ", ", ans[i]);
        }
        printf("]\n");
    }

    return 0;
}

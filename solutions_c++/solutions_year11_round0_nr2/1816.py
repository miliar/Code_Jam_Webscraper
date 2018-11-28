#include <iostream>
#include <vector>
#include <cstring>

using namespace std;

char    com[30][30];
char    opp[30][30];
char    el[150];
int     ncom;
int     nopp;
int     nel;

void
getClosure(vector<char> &ans) {
    char        c1, c2;
    int         len, i;

  retry:
    if ((len = ans.size()) < 2) return;

    c1 = ans[len-1];
    c2 = ans[len-2];

    if (com[c1-'A'][c2-'A'] != '\0') {
        ans.pop_back();
        ans.pop_back();
        ans.push_back(com[c1-'A'][c2-'A']);
        goto retry;
    }
    else {
        for (i=0;i<len-1;++i) {
            if (opp[c1-'A'][ans[i]-'A']) {
                ans.clear();
                return;
            }
        }
    }
}

void
solve(void) {
    int     i, len;
    vector<char>    ans;

    ans.push_back(el[0]);

    for (i=1;i<nel;++i) {
        ans.push_back(el[i]);
        getClosure(ans);
    }

    len = ans.size();
    cout << "[";
    for (i=0;i<len-1;i++) {
        cout << ans[i] << ", ";
    }
    if (len) cout << ans[len-1];
    cout << "]" << endl;
}

int main(void) {
    int     t, i, j;
    string  str;

    cin >> t;

    for (i=0;i<t;++i) {
        memset(com, 0, sizeof(com));
        memset(opp, 0, sizeof(opp));
        cin >> ncom;
        for (j=0;j<ncom;++j) {
            cin >> str;
            com[str[0] - 'A'][str[1] - 'A'] = str[2];
            com[str[1] - 'A'][str[0] - 'A'] = str[2];
        }
        cin >> nopp;
        for (j=0;j<nopp;++j) {
            cin >> str;
            opp[str[0] - 'A'][str[1] - 'A'] = true;
            opp[str[1] - 'A'][str[0] - 'A'] = true;
        }
        cin >> nel;
        cin >> el;
        cout << "Case #" << (i+1) << ": ";
        solve();
    }

    return 0;
}

#include <iostream>
#include <string>
#include <cstdio>


using namespace std;

int T, tc;
int n, m;
string dic[200];
string gstr;

bool strch(string s, char ch) {
    for (int i = 0; i < s.length(); i++)
        if (s[i] == ch) return true;
    return false;
}

bool fit(string s, string t) {
    if (s.length() != t.length()) return false;
    for (int i = 0; i < s.length(); i++)
        if (t[i] != '*' && s[i] != t[i]) return false;
    return true;
}

int getscore(string chkword) {
    int i, j;
    int s;
    s = 0;
    string gs = "";
    bool found;
    bool pass[200];
    for (i = 0; i < n; i++) 
        if (dic[i].length() == chkword.length()) pass[i] = false;
        else pass[i] = true;
    for (i = 0; i < chkword.length(); i++) gs += "*";
    for (i = 0; i < gstr.length(); i++) {
        found = false;
        for (j = 0; j < n; j++) {
            if (pass[j]) continue;
            if (!strch(dic[j], gstr[i])) continue;
            if (!fit(dic[j], gs)) continue;
            found = true;
            break;
        }
        if (!found) continue;
        if (!strch(chkword, gstr[i])){
            s++;
            for (j = 0; j < n; j++)
                if (strch(dic[j], gstr[i])) pass[j] = true;
        } else {
            for (j = 0; j < chkword.length(); j++) {
                if (chkword[j] == gstr[i]) gs[j] = gstr[i];
            }
            if (!strch(gs, '*')) break;
        }
    }
    return s;
}

int main() {
    int i, k;
    int maxs, maxi, tmps;
    freopen("E:\\B-small-attempt5.in", "r", stdin);
    freopen("E:\\B-small.out", "w", stdout);
    cin >> T;
    for (tc = 1; tc <= T; tc++) {
        cin >> n >> m;
        for (i = 0; i < n; i++) cin >> dic[i];
        cout << "Case #" << tc << ":";
        for (k = 0; k < m; k++) {
            cin >> gstr;
            maxs = -1;
            maxi = 0;
            for (i = 0; i < n; i++) {
                tmps = getscore(dic[i]);
                if (tmps > maxs) {
                    maxs = tmps;
                    maxi = i;
                }
            }
            cout << " " << dic[maxi];
        }
        cout << endl;
    }
    return 0;
}

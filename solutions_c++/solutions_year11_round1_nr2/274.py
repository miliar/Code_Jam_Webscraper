#include<iostream>
#include<string>
#include<cmath>
using namespace std;

const int maxn = 10000 + 100;
string words[maxn];
string guess;
int include[maxn][26];
bool f[maxn];
int n, m;

void init() {
    cin >> n >> m;
    memset(include, 0, sizeof (include));
    for (int i = 0; i < n; i++) {
        cin >> words[i];
        for (int ch = 'a'; ch <= 'z'; ch++) {
            int temp = 1;
            for (int j = 0; j < words[i].length(); j++) {
                if (words[i][j] == ch) temp = (temp << 1) + 1;
                else temp = temp << 1;
            }
            include[i][ch - 'a'] = temp;
        }
    }
}

void solve() {
    string ans = "";
    int maxCount = -1;
    int count, left;
    for (int choose = 0; choose < n; choose++) {
        string correct = words[choose];
        left = n;
        count = 0;
        memset(f, 1, sizeof (f));

        for (int i = 0; i < n; i++)
            if (words[i].length() != correct.length()) {
                f[i] = false;
                left--;
            }
        for (int i = 0; i < 26 && left != 1; i++) {
            bool isExit = false;
            for (int j = 0; j < n; j++) {
                if (include[j][guess[i] - 'a'] != (1 << words[j].length()) && f[j]) isExit = true;
                if (isExit) break;
            }
            if (!isExit) continue;

            if (include[choose][guess[i] - 'a'] == (1 << words[choose].length())) count++;
            for (int j = 0; j < n; j++) {
                if (include[j][guess[i] - 'a'] != include[choose][guess[i] - 'a'] && f[j]) {
                    f[j] = false;
                    left--;
                }
            }
        }
        if (count > maxCount) {
            ans = correct;
            maxCount = count;
        }
    }
    cout<<ans;
}

int main() {
    freopen("B-small-attempt0.in", "r", stdin);
    freopen("B-small-attempt0.out", "w", stdout);
    int T;
    cin >> T;
    for (int i = 1; i <= T; i++) {
        cout << "Case #" << i << ": ";
        init();
        for (int j = 1; j <= m; j++) {
            cin >> guess;
            solve();
            if (j != m) cout << ' ';
            else cout << endl;
        }
    }
    return 0;
}
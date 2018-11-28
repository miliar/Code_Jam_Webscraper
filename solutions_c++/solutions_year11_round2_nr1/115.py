#include <iostream>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <queue>
#include <cmath>
#include <cassert>
#include <iomanip>
#include <cstring>
using namespace std;

typedef long long LL ;
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef pair<int,int> PII;

const int INF = 1000*1000*1000 + 1000;
#define PB push_back
#define MP make_pair
#define FI first
#define SE second

string s[103];
int a[103];
int b[103];
double x[103];
double y[103];
double z[103];

int solve() {
    int n;
    cin >> n;
    for (int i = 0; i < n; i++) {
        cin >> s[i];
    }
    for (int i = 0; i < n; i++) {
        x[i] = y[i] = z[i] = 0;
        a[i] = b[i] = 0;
        for (int j = 0; j < n; j++) {
            if (s[i][j] == '1') {
                a[i]++;
                b[i]++;
            }
            else if (s[i][j] == '0') b[i]++;
        }
        double sum = (double) a[i] / b[i];
        z[i] += 0.25 * sum;
    }
    for (int i = 0; i < n; i++) {
        double sum = 0;
        int ile = 0;
        for (int j = 0; j < n; j++) {
            if (s[i][j] == '.') continue;
            ile++;
            int aa = a[j] - (s[i][j] == '0');
            int bb = b[j] - 1;
            sum += (double)aa / bb;
        }
        y[i] = sum / ile;
        z[i] += 0.5 * y[i];
    }
    for (int i = 0; i < n; i++) {
        double sum = 0;
        int ile = 0;
        for (int j = 0; j < n; j++) {
            if (s[i][j] == '.') continue;
            sum += y[j];
            ile++;
        }
        sum /= ile;
        z[i] += 0.25 * sum;
        cout << setprecision(12) << z[i] << '\n';
    }
}

int main()
{
    ios_base::sync_with_stdio(0) ;
    int te;
    cin >> te;
    for (int u = 1; u <= te; u++) {
        cout << "Case #" << u << ":\n";
        solve();
    }
}


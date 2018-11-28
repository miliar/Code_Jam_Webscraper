#include <iostream>
#include <cstring>
#include <vector>
#include <cmath>

using namespace std;

int mem[101][101];

vector<int> sc;
int P;
int N, S;

int getMaxNonSup(int a) {
    int best = -1;
    for (int i = 0; i <= a; ++i) {
        for (int j=i;j<=a;++j) {
            int k = a-i-j;
            if (k >= 0 && abs(i-j) < 2 && abs(j-k) < 2 && abs(i-k) < 2) {
                best = max(best, max(i, max(j, k)));
            }
        }
    }
    return best;
}

int getMaxSup(int a) {
    int best = -1;
    for (int i = 0; i <= a; ++i) {
        for (int j=i;j<=a;++j) {
            int k = a-i-j;
            if (k >= 0 && abs(i-j) <= 2 && abs(j-k) <= 2 && abs(i-k) <= 2 && (abs(j-k) == 2 || abs(i-k)==2 || abs(i-j)==2)) {
                best = max(best, max(i, max(j, k)));
            }
        }
    }
    return best;
}

int solve(int a, int sl) {
    int &ans = mem[a][sl];
    if (ans != -1) return ans;

    if (a == N) {
        if (sl == 0) { return ans = 0; }
        else { return ans = -1000; }
    }

    int maxNonSup = getMaxNonSup(sc[a]);
    ans = solve(a+1, sl) + (maxNonSup >= P);
    if (sl > 0) {
        int maxSup = getMaxSup(sc[a]);
        ans = max(ans, solve(a+1, sl-1) + (maxSup >= P));
    }

    return ans;
}

int main() {
    int n;
    cin>>n;
    for (int t=1;t<=n;++t) {
        sc.clear();
        cin>>N>>S>>P;
        for (int i=0;i<N;++i) {
            int x;
            cin>>x;
            sc.push_back(x);
        }
        memset(mem,-1,sizeof(mem));
        cout << "Case #" << t << ": " << solve(0, S) << endl;
    }
}

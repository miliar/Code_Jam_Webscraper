#include <iostream>
#include <iterator>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>
#include <cstdio>
#include <cctype>
#include <cstring>

using namespace std;

int D[10000], L[10000];
int best[10000];
int main() {
    cin.sync_with_stdio(false);
    int T;
    cin >> T;
    for (int t=1; t<=T; ++t) {
        int n;
        cin >> n;
        for (int i=0; i<n; ++i) {
            cin >> D[i] >> L[i];
            best[i] = D[i] + 1;
        }
        int dist;
        cin >> dist;

        best[0] = 0;
        int next = 1;
        bool ok = false;
        for (int i=0; i<n; ++i) {
            if (best[i] > D[i]) {
                ok = false;
                break;
            }
            int curlen = D[i] - best[i];
            int maxreach = D[i] + curlen;
            if (maxreach >= dist) {
                ok = true;
                break;
            }
            while (next<n && maxreach>=D[next]) {
                best[next] = D[next] - min(L[next], D[next]-D[i]);
                ++next;
            }
        }
        cout << "Case #" << t << ':' << (ok ? " YES" : " NO") << '\n';
    }
	return 0;
}

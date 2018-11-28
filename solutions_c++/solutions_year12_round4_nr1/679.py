#include <cstring>
#include <string>
#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;
int a[10010], b[10010], f[10010], n, test;
int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    cin >> test;
    for (int t = 1; t <= test; t++) {
        int n;
        cin >> n;
        for (int i = 1; i <= n; i++) {
            scanf("%d%d", &a[i], &b[i]);
            //c[i] = a[i] - b[i];
            //cout << a[i] << ' ' << b[i] << endl;
        }
        memset(f, -1, sizeof(f)); f[1] = 0;
        if (b[1] > a[1]) b[1] = a[1];
        bool u = false;
        int len;
        cin >> len;
        for (int i = 1; i <= n; i++)
		if (f[i] >= 0) {
			int tmp = a[i] - f[i] + a[i];
			if (tmp >= len) {
				u = true;
				break;
			}
			for (int j = i+1; j <= n; j++)
			if (tmp >= a[j]){
				int x = max(a[i], a[j] - b[j]);
				if (f[j] == -1 || x < f[j]) f[j] = x;
			} else break;
		}
        printf("Case #%d: ", t);
        if (u) cout << "YES"; else cout << "NO";
        cout << endl;
    }
}

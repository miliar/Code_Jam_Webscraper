#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <map>
#include <cmath>
#include <set>
using namespace std;

int a[10000];

int main()
{
    int i, j, k, tt;
    cin >> tt;
    for (int test = 1; test <= tt; test++) {
        int n, l, h;

        cin >> n >> l >> h;

        for (i = 0; i < n; i++) cin >> a[i];

        for (i = l; i <= h; i++) {
            for (j = 0; j < n; j++)
                if (i % a[j] && a[j] % i) break;
            if (j == n) break;
        }

        cout << "Case #" << test << ": ";
        if (i > h) cout << "NO" << endl;
        else cout << i << endl;
    }
    return 0;
}

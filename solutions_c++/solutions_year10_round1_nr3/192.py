#include <iostream>
#include <vector>
#include <map>
using namespace std;

typedef map<int, bool> MAP;
typedef vector<MAP> Vmap;

Vmap calc;

bool f(int a, int b) {
//     cerr << a << ' ' << b << endl;
    if (a < b) swap(a, b);
    if (calc[a].find(b) != calc[a].end()) return calc[a][b];
    /*for (int k = 1; b*k < a; ++k)
        if (not f(a - b*k, b)) return calc[a][b] = true;*/
    int m = a/b;
    for (int k = m - 50; k <= m + 50; ++k)
        if (k > 0 and b*k < a and not f(a - b*k, b))
            return calc[a][b] = true;
    return calc[a][b] = false;
}

int main() {
    int tcas;
    cin >> tcas;
    for (int cas = 1; cas <= tcas; ++cas) {
        int a1, a2, b1, b2;
        cin >> a1 >> a2 >> b1 >> b2;
        int r = 0;
        calc = Vmap(max(a2, b2) + 17);
        for (int i = a1; i <= a2; ++i)
            for (int j = b1; j <= b2; ++j)
                if (f(i, j)) ++r;
        cout << "Case #" << cas << ": " << r << endl;
    }
}

#include <iostream>
#include <set>
#include <algorithm>
#include <vector>
using namespace std;

#define X first
#define Y second

typedef vector<int> Vi;
typedef vector<Vi> Mi;
typedef pair<int, int> P;
typedef set<P> SET;
typedef SET::iterator Sit;

void next(SET& a, SET& b) {
    SET mor, neix;
    for (Sit it = a.begin(); it != a.end(); ++it) {
        int x = it->X;
        int y = it->Y;
        if (a.find(P(x - 1, y)) == a.end() and a.find(P(x, y - 1)) == a.end())
            mor.insert(P(x, y));
        if (a.find(P(x + 1, y - 1)) != a.end())
            neix.insert(P(x + 1, y));
    }
    b = a;
    for (Sit it = mor.begin(); it != mor.end(); ++it) {
        P p = *it;
        b.erase(p);
    }
    for (Sit it = neix.begin(); it != neix.end(); ++it) {
        P p = *it;
        b.insert(p);
    }
}

int main() {
    int tcas;
    cin >> tcas;
    for (int cas = 1; cas <= tcas; ++cas) {
        int r;
        cin >> r;
        SET ini;
        for (int k = 0; k < r; ++k) {
            int x1, y1, x2, y2;
            cin >> y1 >> x1 >> y2 >> x2;
            for (int i = x1; i <= x2; ++i)
                for (int j = y1; j <= y2; ++j)
                    ini.insert(P(i, j));
        }
        SET act = ini;
        int pas = 0;
        while (act.size() > 0) {
//             Mi mat(7, Vi(7, 0));
//             for (Sit it = act.begin(); it != act.end(); ++it) mat[it->X][it->Y] = 1;
//             for (int i = 0; i < 7; ++i) {
//                 for (int j = 0; j < 7; ++j)
//                     cerr << mat[i][j];
//                 cerr << endl;
//             }
//             cerr << endl;
            SET sig;
            next(act, sig);
            act = sig;
            ++pas;
        }
        cout << "Case #" << cas << ": " << pas << endl;
    }
}

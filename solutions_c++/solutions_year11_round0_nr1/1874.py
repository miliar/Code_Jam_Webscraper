#include <cstdio>
#include <vector>
#include <cmath>
#include <algorithm>
using namespace std;

typedef pair <int, int> TPair;
#define pos first
#define id second

const int oo = 1000;

int nTests;

int main() {
    freopen("EXAMPLE.INP", "r", stdin);
    freopen("A.OUT", "w", stdout);
    scanf("%d", &nTests);
    for (int t = 1; t <= nTests; t++) {
        int n; scanf("%d", &n);
        vector <TPair> Orange, Blue;

        for (int i = 0; i < n; i++) {
            char ch;
            do ch = getchar();
            while (ch != 'O' && ch != 'B');
            int x; scanf("%d", &x);

            if (ch == 'O')
                Orange.push_back(TPair(x, i));
            else
                Blue.push_back(TPair(x, i));
        }

        vector <TPair> :: iterator itO, itB;
        itO = Orange.begin();
        itB = Blue.begin();
        int nowO = 1, nowB = 1, res = 0;

        for (int i = 0; i < n; i++) {
            if (itO != Orange.end() && i == itO->id) {
                int delta = abs(itO->pos - nowO) + 1;
                nowO = itO->pos;
                res += delta; ++itO;

                if (itB != Blue.end())
                    if (itB->pos > nowB)
                        nowB += min(itB->pos - nowB, delta);
                    else
                        nowB -= min(nowB - itB->pos, delta);
            }
            else if (itB != Blue.end() && i == itB->id) {
                int delta = abs(itB->pos - nowB) + 1;
                nowB = itB->pos;
                res += delta; ++itB;

                if (itO != Orange.end())
                    if (itO->pos > nowO)
                        nowO += min(itO->pos - nowO, delta);
                    else
                        nowO -= min(nowO - itO->pos, delta);
            }
        }

        printf("Case #%d: %d", t, res);
        if (t < nTests) printf("\n");
    }
}

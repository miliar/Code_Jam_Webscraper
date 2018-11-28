#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

typedef long long ent;
typedef vector<ent> Vi;
typedef vector<Vi> Mi;

ent D, I, M, N;
Vi A;
Mi calc;

/*int f(int pos, int ant) {
    if (pos == N) return 0;
    if (calc[pos][ant] != -1) return calc[pos][ant];
    int act = A[pos];
    int mini = D + f(pos + 1, ant);
    if (M > 0) {
        int ins = (ant == 256 ? 0 : max(0, abs(ant - act) - 1)/M);
        mini = min(mini, ins*I + f(pos + 1, act));
    }
    int a = max(0, ant - M);
    int b = min(255, ant + M);
    if (ant == 256) {
        a = 0;
        b = 255;
    }
    for (int i = a; i <= b; ++i)
        mini = min(mini, abs(act - i) + f(pos + 1, i));
    return calc[pos][ant] = mini;
}*/

ent f(int pos, int ant) {
    if (pos == N) return 0;
    if (calc[pos][ant] != -1) return calc[pos][ant];
    ent act = A[pos];
    ent mini = D + f(pos + 1, ant);
    for (ent i = 0; i <= 255; ++i)
        if (ant == 256 or abs(i - ant) == 0 or M > 0) {
            ent ins = 0;
            if (ant != 256 and abs(ant - i) > 0) ins = (abs(ant - i) - 1)/M;
            mini = min(mini, ins*I + abs(act - i) + f(pos + 1, i));
        }
    return calc[pos][ant] = mini;
}

int main() {
    ent tcas;
    cin >> tcas;
    for (ent cas = 1; cas <= tcas; ++cas) {
        cin >> D >> I >> M >> N;
        A = Vi(N);
        for (ent i = 0; i < N; ++i) cin >> A[i];
        calc = Mi(N + 1, Vi(260, -1));
        cout << "Case #" << cas << ": " << f(0, 256) << endl;
    }
}

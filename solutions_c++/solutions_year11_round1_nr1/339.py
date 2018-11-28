#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

int gcd(int a, int b) {
    if (a == 0) return b;
    if (a > b) return gcd(b, a);
    return gcd(a, b % a);
}

string doit() {
    long long N;
    long long PD;
    long long PG;
    cin >> N;
    cin >> PD;
    cin >> PG;
    if (PD > 0 && PG == 0) return "Broken";
    if (PD < 100 && PG == 100) return "Broken";
    if (PD == 0) return "Possible";
    if (N >= 100) return "Possible";
    for (long long i = 1; i <= N; i++) {
        if ((i * PD) % 100 == 0)
            return "Possible";
    }
    return "Broken";
}

int main(int argc, char *argv[]) {
    int C;
    cin >> C;
    for (int i = 1; i <= C; i++) {
        string res = doit();
        cout << "Case #" << i << ": " << res << endl;
    }
    return 0;
}

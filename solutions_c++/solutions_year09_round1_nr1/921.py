#include <iostream>
#include <string>
#include <sstream>
#include <vector>
#include <set>

using namespace std;

int digsum(int x, int b) {
    int sum = 0;
    while (x != 0) {
        sum += (x%b) * (x%b);
        x /= b;
    }
    return sum;
}

bool happy(int x, int b) {
    set<int> S;
    S.insert(x);
    do {
        x = digsum(x, b);
        //cerr << "x = " << x << '\n';
    } while (S.insert(x).second);
    return x == 1;
}

int main() {
    int T; cin >> T; cin.ignore();
    for (int c = 1; c <= T; c++) {
        string line; getline(cin, line);
        istringstream buff(line);
        vector<int> V; int x;
        while (buff >> x) V.push_back(x);
        int p = 1, k;
        //cerr << "ok\n";
        do {
            ++p;
            for (k = 0; k < V.size(); k++)
                if (!happy(p, V[k])) {
                    //cerr << p << " is not happy in base " << V[k] << '\n';
                    break;
                }
        } while (k < V.size());
        cout << "Case #" << c << ": " << p << '\n';
    }
    return 0;
}

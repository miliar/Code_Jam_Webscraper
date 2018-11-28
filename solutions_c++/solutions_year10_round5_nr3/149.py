#include <iostream>
#include <map>
using namespace std;

#define X first
#define Y second

typedef map<int, int> MAP;
typedef MAP::iterator Mit;

int main() {
    int tcas;
    cin >> tcas;
    for (int cas = 1; cas <= tcas; ++cas) {
        int n;
        cin >> n;
        MAP m;
        for (int i = 0; i < n; ++i) {
            int a, b;
            cin >> a >> b;
            m[a] += b;
        }
        int mov = 0;
        while (true) {
            Mit it = m.begin();
            while (it != m.end() and it->Y <= 1) ++it;
            if (it == m.end()) break;
            int pos = it->X;
            m[pos] -= 2;
            ++m[pos - 1];
            ++m[pos + 1];
            ++mov;
        }
        cout << "Case #" << cas << ": " << mov << endl;
    }
}

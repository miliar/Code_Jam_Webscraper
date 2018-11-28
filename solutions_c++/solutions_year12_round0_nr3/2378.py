#include <iostream>
#include <cstdlib>
#include <set>

using namespace std;

int main() {
    int n;
    cin >> n;
    for (int i = 1; i <= n; i++) {
        set<pair<int,int> > ins;

        int a, b;
        cin >> a >> b;
        for (int j = a; j <= b; j++) {
            char c[10];
            itoa(j, c, 10);
            string s(c);
            for (int k = 1; k < (int)s.length(); k++) {
                string s2 = s.substr(k).append(s.substr(0,k));
                if (s2[0] != '0') {
                    int j2 = atoi(s2.c_str());
                    if (j2 > j && j2 <= b) {
                        ins.insert(make_pair(j, j2));
                    }
                }
            }

        }

        cout << "Case #" << i << ": " << ins.size() << "\n";
    }


}

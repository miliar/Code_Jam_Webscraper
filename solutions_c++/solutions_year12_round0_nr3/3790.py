#include <cstdio>
#include <iostream>
#include <set>
#include <string>
#include <sstream>
using namespace std;


int main(void) {
    int test; scanf("%d", &test);

    for (int cs = 1; cs <= test; ++cs) {
        fprintf(stderr, "%d\n", cs);
        int a, b; scanf("%d%d", &a, &b);
        ostringstream A; A << a;
        ostringstream B; B << b;

        set<pair<int, int> > S;

        for (int i = a; i <= b; ++i) {
            ostringstream O; O << i;
            const string& n = O.str();

            for (int j = 0; j < n.size(); ++j) {
                string m = n.substr(j) + n.substr(0, j);
                if (*m.begin() == '0') continue;
                if (A.str() <= n && n < m && m <= B.str()) {
                    //cout << n << " " << m << endl;
                    istringstream I(m); int nm; I >> nm;
                    S.insert(make_pair(i, nm));
                    //S.insert(m);
                }
            }
        }

        printf("Case #%d: %d\n", cs, (int)S.size());
    }
return 0;
}

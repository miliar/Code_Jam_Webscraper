#include <iostream>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <algorithm>

using namespace std;

#define uint unsigned int

#define FOR(i, n) for (int i = 0; i < (n); i++)
#define FORU(i, n) for (uint i = 0; i < (n); i++)
#define FORR(i, n) for (int i = (n)-1; i >= 0; i--)
#define FORRU(i, n) for (uint i = (n)-1; i >= 0; i--)
#define FOREACH(it, v) for (__typeof__(v.begin()) it = (v).begin(); it != (v).end(); ++it)

int main() {
    int cases;
    cin >> cases;

    FOR(tcase, cases) {
        string number;
        cin >> number;

        vector<int> vn;

        FORU(i, number.length()) {
            vn.push_back(number[i]-'0');
        }

        int nulls = 0;
        if (!next_permutation(vn.begin(), vn.end())) {
            nulls = 1;
        }

        printf("Case #%d: ", tcase+1);
        FORU(i, vn.size()) {
            if (vn[i] == 0) {
                nulls++;
            } else {
                break;
            }
        }

        bool n = false;
        bool d = false;
        FORU(i, vn.size()) {
            if (vn[i] != 0 || n == true) {
                printf("%c", vn[i] + '0');
            }
            if (vn[i] != 0 && n == false) n = true;

            if (n && !d) {
                FOR(j, nulls) {
                    printf("%c", '0');
                }
                d = true;
            }
        }
        printf("\n");
    }

    return 0;
}

#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
using namespace std;

int main(void) {
    int test; scanf("%d", &test);

    for (int cs = 0; cs < test; ++cs) {
        int com; cin >> com;
        vector<string> comrules(com);
        for (int i = 0; i < com; ++i) {
            cin >> comrules[i];
            string t = comrules[i];
            swap(t[0], t[1]);
            comrules.push_back(t);
        }

        int opp; cin >> opp;
        vector<string> opprules(opp);
        for (int i = 0; i < opp; ++i) {
            cin >> opprules[i];
            string t = opprules[i];
            swap(t[0], t[1]);
            opprules.push_back(t);
        }

        int n;
        string seq; cin >> n >> seq;

        vector<char> stek;
        for (int i = 0; i < seq.size(); ++i) {
            char curr = seq[i];
            int ok = 1;

            if (!stek.empty()) { // provjeri dal kombiniraju
                for (int j = 0; j < comrules.size(); ++j) {
                    if (comrules[j][0] == curr && comrules[j][1] == stek.back()) {
                        stek.pop_back();
                        curr = comrules[j][2];
                        break;
                    }
                }
                for (int j = 0; j < opprules.size(); ++j) {
                    for (int k = 0; k < stek.size(); ++k) {
                        if (opprules[j][0] == curr && opprules[j][1] == stek[k]) {
                            stek.clear();
                            ok = 0;
                        }
                    }
                }
            }
            if (ok) {
                stek.push_back(curr);
            }
        }

        printf("Case #%d: [", cs+1);
        for (int i = 0; i < stek.size(); ++i) {
            if (i) printf(", ");
            printf("%c", stek[i]);
        }
        puts("]");
    }
return 0;
}

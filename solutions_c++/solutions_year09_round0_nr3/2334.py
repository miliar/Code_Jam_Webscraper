#include <iostream>
#include <string>
#include <iomanip>

#define MAXLEN 512
#define MATCHLEN 19

using namespace std;

int main() {
    freopen("C-small.in", "r", stdin);
    freopen("C.out", "w", stdout);

    int i, j, n, l;
    char match[] = "welcome to code jam";
    char str[MAXLEN];

    int pos[MATCHLEN];

    int ps, pm, pstart, plast, total;

    cin >> n;
    cin.get();

    for(i = 0; i < n; i++) {
        cin.getline(str, MAXLEN);

        l = strlen(str);
        plast = l - MATCHLEN;

        total = 0;
        pm = 0;
        ps = 0;

        while(true) {
            if(str[ps] == match[pm]) {
                //cout << pm << endl;
                pos[pm] = ps;
                pm++;
                if(pm == MATCHLEN) {
                    total++;
                    pm--;
                }
            }

            if(ps > l - (MATCHLEN - pm)) {
                if(pm ==  0) break;
                pm--;
                ps = pos[pm];
                //cout << "pm: " << pm << "; ps: " << ps << endl;
            }

            ps++;
        }

        cout << "Case #" << (i+1) << ": " << setw(4) << setfill('0') << (total%10000) << endl;
    }

    return 0;
}

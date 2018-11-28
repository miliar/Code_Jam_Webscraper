#include <iostream>
#include <stdio.h>
#include <string.h>
#include <map>
#include <vector>
#include <fstream>
#include <sstream>
#include <cmath>

using namespace std;

int main() {
//     freopen("input.txt", "rt", stdin);
//     freopen("A-small-attempt0.in", "rt", stdin);
    freopen("A-large.in", "rt", stdin);
    freopen("output.txt", "wt", stdout);
    int MAXN = 118;
    int tt,res,n;
    char who[MAXN];
    int how[MAXN];
    cin >> tt;
    int pos1,pos2,cur1,cur2,curcom;
    bool moved1,moved2;
    for (int ii = 1; ii <= tt; ii++) {
        cin >> n;
        for (int i = 1; i <= n; i++)
            cin >> who[i] >> how[i];
        res = 0;
        curcom = 1;
        cur1 = 1;
        cur2 = 1;
        pos1 = 1;
        pos2 = 1;
        while ((cur1 <= n) && (who[cur1] != 'O'))
            cur1++;
        while ((cur2 <= n) && (who[cur2] != 'B'))
            cur2++;
        while (curcom <= n) {
            res++;
            moved1 = false;
            moved2 = false;
            if ((who[curcom] == 'O') && (how[curcom] == pos1)) {
                curcom++;
                moved1 = true;
                cur1++;
                while ((cur1 <= n) && (who[cur1] != 'O'))
                    cur1++;
            }
            else if ((who[curcom] == 'B') && (how[curcom] == pos2)) {
                curcom++;
                moved2 = true;
                cur2++;
                while ((cur2 <= n) && (who[cur2] != 'B'))
                    cur2++;
            }
            if ((!moved1) && (pos1 != how[cur1]))
                pos1 += (how[cur1]-pos1)/abs(how[cur1]-pos1);
            if ((!moved2) && (pos2 != how[cur2]))
                pos2 += (how[cur2]-pos2)/abs(how[cur2]-pos2);
//             cout << curcom << endl;
//             cout << pos1 << " " << pos2 << endl;
        }
        cout << "Case #" << ii << ": " << res << endl;
    }
    return 0;
}

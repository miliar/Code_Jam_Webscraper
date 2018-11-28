#include <vector>
#include <list>
#include <queue>
#include <map>
#include <set>
#include <string>
#include <iostream>
#include <sstream>
#include <cmath>
#include <algorithm>
#include <cstdio>
#include <cstdlib>

using namespace std;

int
main(void)
{
    int i, j, pos, k;
    int T, C, D, N;
    char com[256][256];
    char opp[256][256];
    char cnt[256];
    char ret[101];
    char lst[8] = {
        'Q', 'W', 'E', 'R', 'A', 'S', 'D', 'F'
    };
    string s;

    cin >> T;

    for(i=0;i<T;i++) {
        memset(com, 0, sizeof(com));
        memset(opp, 0, sizeof(opp));
        memset(ret, 0, sizeof(ret));
        memset(cnt, 0, sizeof(cnt));
        cin >> C;
        for(j=0;j<C;j++) {
            cin >> s;
            com[s[0]][s[1]] = s[2];
            com[s[1]][s[0]] = s[2];
        }
        cin >> D;
        for(j=0;j<D;j++) {
            cin >> s;
            opp[s[0]][s[1]] = 1;
            opp[s[1]][s[0]] = 1;
        }
        cin >> N;
        cin >> s;
        pos = 0;
        for(j=0;j<N;j++) {
            ret[pos] = s[j];
            cnt[s[j]]++;
            if ((pos > 0) && com[ret[pos-1]][ret[pos]]) {
                cnt[ret[pos]]--;
                cnt[ret[pos-1]]--;
                cnt[com[ret[pos-1]][ret[pos]]]++;
                ret[pos-1] = com[ret[pos-1]][ret[pos]];
                ret[pos] = 0;
            } else {
                bool flg = false;
                for(k=0;k<8;k++) {
                    if ((opp[ret[pos]][lst[k]] && (ret[pos] == lst[k]) && (cnt[lst[k]]>2))
                        || (opp[ret[pos]][lst[k]] && (ret[pos] != lst[k]) && cnt[lst[k]])) {
                        flg = true;
                    }
                }
                if (flg) {
                    pos = 0;
                    memset(cnt, 0, sizeof(cnt));
                } else {
                    pos++;
                }
            }
        }
        cout << "Case #" << (i+1) << ": [";
        for(j=0;j<pos;j++) {
            if (j > 0) {
                cout << ", ";
            }
            cout << ret[j];
        }
        cout << "]" << endl;
    }
    
    return 0;
}

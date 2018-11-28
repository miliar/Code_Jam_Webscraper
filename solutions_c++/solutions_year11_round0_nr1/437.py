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
    int i, j;
    int T, N;
    string s_col;
    int n_pos;
    int col[101];
    int pos[101];
    int p_blu, p_org;
    int t_blu, t_org;

    cin >> T;

    for(i=0;i<T;i++) {
        cin >> N;
        for(j=0;j<N;j++) {
            cin >> s_col >> n_pos;
            pos[j] = n_pos;
            if (s_col[0] == 'O') {
                col[j] = 'O';
            } else {
                col[j] = 'B';
            }
        }
        p_blu = p_org = 1;
        t_blu = t_org = 0;
        for(j=0;j<N;j++) {
            if (col[j] == 'O') {
                if (t_org < t_blu) {
                    t_org = t_org+max(abs(pos[j]-p_org),(t_blu-t_org))+1;
                } else {
                    t_org += (abs(pos[j]-p_org)+1);
                }
                p_org = pos[j];
            } else {
                if (t_org > t_blu) {
                    t_blu = t_blu+max(abs(pos[j]-p_blu),(t_org-t_blu))+1;
                } else {
                    t_blu += (abs(pos[j]-p_blu)+1);
                }
                p_blu = pos[j];
            }
//             cout << "t=" << t_org << "," << t_blu << endl;
//             cout << "p=" << p_org << "," << p_blu << endl;
        }
        cout << "Case #" << (i+1) << ": " << max(t_blu, t_org) << endl;
    }
    
    return 0;
}

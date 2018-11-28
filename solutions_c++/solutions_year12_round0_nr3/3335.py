#include <string.h>
#include <map>
#include <deque>
#include <queue>
#include <stack>
#include <sstream>
#include <bitset>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <fstream>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <algorithm>
#include <vector>
#include <set>
#include <complex>
#include <list>
#include <valarray>
#include <memory.h>
#include<algorithm>
using namespace std;
set<string> H;
string toString( int i)
{
    
       string r;
       stringstream s;

       s << i;
       r = s.str();

       return r;

}
int main() {
        freopen("C-small-attempt0.in", "r", stdin);
        freopen("y.out", "w", stdout);
    
    int t, n, m, p, num, count;
        scanf("%d", &t);
//    t = 1;
    string sn, sm, s, g, g1, g2;
    for (int i = 0; i < t; i++) {
        scanf("%d%d",&n,&m);
//        sn = "10";
//        sm = "40";
        sn=toString(n);
        sm=toString(m);
        H.clear();
//        cout << n << " " << m << endl;
        for (int j = n; j < m; j++) {
            s =toString(j);
            for (int k = s.size() - 1; k > 0; k--) {
                g1 = s.substr(k);
                if (g1[0] == '0')continue;
                g2 = s.substr(0, k);
                g = g1 + g2;
//                cout << sn << " : " << sm << " : " << s << " : " << g << endl;
                if (atoi(g.c_str()) >= atoi(sn.c_str()) && atoi(g.c_str()) <= atoi(sm.c_str()) && atoi(g.c_str()) > atoi(s.c_str())) {
                    H.insert(s + " :: " + g);
//                    cout << s << " " << g << endl;
                }
            }

        }

        printf("Case #%d: %d\n", (i + 1), H.size());

    }


}

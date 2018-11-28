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
    int C;
    int N, M, A;
    int x2, y2;
    int x3, y3;
    int i, j;
    double l1, l2, l3;
    double s, a;

    cin >> C;

    for(i=1;i<=C;i++) {
        cin >> N >> M >> A;
        bool found = false;
        for(x2=0;x2<=N;x2++) {
            for(y2=0;y2<=M;y2++) {
                for(x3=0;x3<=N;x3++) {
                    for(y3=0;y3<=M;y3++) {
                        l1 = sqrt(x2*x2+y2*y2);
                        l2 = sqrt(x3*x3+y3*y3);
                        l3 = sqrt((x3-x2)*(x3-x2)+(y3-y2)*(y3-y2));
                        s = (l1+l2+l3)/2.0;
                        a = 2.0*sqrt(s*(s-l1)*(s-l2)*(s-l3));
                        if (fabs(a-A) < 0.1) {
                            found = true;
                            break;
                        }
                    }
                    if (found)
                        break;
                }
                if (found)
                    break;
            }
            if (found)
                break;
        }
        if (found) {
            cout << "Case #" << i << ": " << 0 << " "  << 0 << " ";
            cout << x2 << " " << y2 << " " << x3 << " " << y3 << endl;
        } else {
            cout << "Case #" << i << ": IMPOSSIBLE" << endl;
        }
    }
    
    return 0;
}

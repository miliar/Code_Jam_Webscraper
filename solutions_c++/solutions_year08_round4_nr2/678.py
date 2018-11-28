#include <algorithm>
#include <string>
#include <cstdio>
#include <cmath>
#include <map>
#include <vector>
#define X first
#define Y second
#define PII pair<int, int>
#define PB push_back
#define FOREACH(c, it) for(typeof(c.begin()) it = c.begin(); it != c.end(); ++it)
#define ll long long

using namespace std;

int main() {
    int ncase;
    scanf("%d", &ncase);
    for (int icase = 0; icase < ncase; ++icase) {
        int n, m, a;
        scanf("%d %d %d", &n, &m, &a);
        if (a > n*m) {
            printf("Case #%d: IMPOSSIBLE\n", icase+1);
            continue;
        }           
        bool found = false;
        int x1s, y1s, x2s, y2s;
        
        //for (int y0 = 0; !found && y0 <= m; ++y0)
        //for (int x0 = 0; !found && x0 <=n; ++x0)
        for (int y1 = 0; !found && y1 <= m; ++y1)
            for (int x1 = 0; !found && x1 <= n; ++x1)
                for (int y2 = 0; !found && y2 <= m; ++y2)
                    for (int x2 = 0; !found && x2 <= n; ++x2)            
                        if (abs((x1*y2-x2*y1)/* +(0*y1-x1*0)+(x2*0-0*y2)*/) == a) {
                            x1s = x1;
                            y1s = y1;
                            x2s = x2;
                            y2s = y2;
                            found = true;
                        } 
        
        if (found)
            printf("Case #%d: %d %d %d %d %d %d\n", icase+1, 0, 0, x1s, y1s, x2s, y2s);
        else
            printf("Case #%d: IMPOSSIBLE\n", icase+1);
    }
    return 0;
}

#include <stdio.h>
#include <vector>
#include <algorithm>
#include <cmath>

using namespace std;

int main()
{
    int t;
    scanf("%d", &t);
    
    for (int k = 1; k <= t; ++k) {
        int n;
        scanf("%d", &n);
  
        int oPos, bPos, oTime, bTime;
        oPos = bPos = 1;
        oTime = bTime = 0;

        for (int i = 0; i < n; ++i) {
            char robot[2];
            int pos;
            scanf("%s %d", robot, &pos);
            
            if (robot[0] == 'O') {
                oTime = max(oTime + abs(pos - oPos) + 1, bTime + 1);
                oPos = pos;
            } else {
                bTime = max(bTime + abs(pos - bPos) + 1, oTime + 1);
                bPos = pos;
            }
        }
        
        printf("Case #%d: %d\n", k, max(oTime, bTime));
    }

    return 0;
}


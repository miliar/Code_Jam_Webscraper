#include<cstdio>
#include<algorithm>

using namespace std;

int main() {
    int zw;
    scanf("%d", &zw);
    for(int zz=1; zz<=zw; zz++) {
        int n;
        scanf("%d", &n);
        int posO, posB;
        int timeO, timeB;
        posO = posB = 1;
        timeO = timeB = 0;
        int allTime = 0;
        for(int i=0; i<n; i++) {
            char player;
            int field;
            player = ' ';
            while(player != 'O' && player != 'B')
                player = getchar();
            
            scanf("%d", &field); 
            if(player == 'O') {
                int timeToGo = abs(posO - field);
                int saved = min(timeO, timeToGo);
                timeO = 0;
                timeToGo -= saved;
                timeToGo++; // for the push
                allTime += timeToGo;
                timeB += timeToGo;
                posO = field;
            }
            else {
                int timeToGo = abs(posB - field);
                int saved = min(timeB, timeToGo);
                timeB = 0;
                timeToGo -= saved;
                timeToGo++; // for the push
                allTime += timeToGo;
                timeO += timeToGo;                
                posB = field;
            }
//            printf("after request %d : %c %d now stats are O: pos %d time %d B: pos %d time %d all time %d\n", i, player, field, posO, timeO, posB, timeB, allTime);
        }
        printf("Case #%d: %d\n", zz, allTime);
    }
    return 0;
}

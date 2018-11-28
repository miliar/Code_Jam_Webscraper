#include <cstdio>
#include <cstring>

int probCount;
int engineCount;
int queryCount;
char engine[105][105];
char query[105];
bool tick[105];
int tickCount;
int switchCount;

void clearTick() {
    tickCount = 0;
    for(int i=0; i<engineCount; i++) {
        tick[i] = false;
    }
}

int main() {
    int i,j,probIndex;
    scanf("%d\n", &probCount);
    for(int probIndex=1; probIndex<=probCount; probIndex++) {
        switchCount = 0;
        scanf("%d\n", &engineCount);
        for(i=0; i<engineCount; i++) {
            gets(engine[i]);
        }
        scanf("%d\n", &queryCount);
        clearTick();
        for(i=0; i<queryCount; i++) {
            gets(query);
            for(j=0; strcmp(query, engine[j]); j++);
            if(tick[j] == false) {
                tick[j] = true;
                tickCount++;
                if(tickCount == engineCount) {
                    clearTick();
                    switchCount++;
                    tickCount = 1;
                    tick[j] = true;
                }
            }
        }
        printf("Case #%d: %d\n", probIndex, switchCount);
    }
}

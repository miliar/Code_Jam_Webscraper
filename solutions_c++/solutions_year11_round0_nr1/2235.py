#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    int t, n;
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    scanf("%d",&t);
    for (int cases = 1; cases <= t; ++cases) {
        char str[10];
        int step;
        scanf("%d",&n);
        int posB = 1;
        int posO = 1;
        int timesB = 0;
        int timesO = 0;
        for (int i = 0; i < n; ++i) {
            scanf("%s%d",&str, &step);
            if (str[0] == 'B') {
               int gap = abs(posB - step);
               timesB = max(timesO, timesB + gap) + 1;
               posB = step;
            } else{
               int gap = abs(posO - step);
               timesO = max(timesB, timesO + gap) + 1;    
               posO = step;
            }
            //printf("%d %d\n",timesB, timesO);
        }
        
        printf("Case #%d: %d\n",cases, max(timesB, timesO));
    }
    fclose(stdin);
    fclose(stdout);
    return 0;
}

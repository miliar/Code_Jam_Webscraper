#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <vector>
#include <map>
#include <algorithm>

using namespace std;

#define MAXN 10001

int vine[MAXN][2];
int n;
int loved;

bool daSie(int currVine, int swing) {
    bool result = 0;
    //printf("dasie: vine: %d, swing: %d\n", currVine, swing);
    if(swing + vine[currVine][0] >= loved)
        return 1;
    for(int j = currVine + 1; j < n; j++) {
        int d = vine[j][0] - vine[currVine][0];
        //printf("D = %d\n", d);
        if(d > swing) // odleglsoc
            break;
        int nextSwing = min(d, vine[j][1]);
        int nextVine = j;
        result = result || daSie(nextVine, nextSwing);
        if(result)
            break;
    }
    return result;
}

void solve() {
    scanf("%d", &n);
    //printf("%d ", n);
    for(int i = 0; i < n; i++)
        scanf("%d %d", &vine[i][0], &vine[i][1]);
    scanf("%d", &loved);
    int currVine = 0;
    int nextVine = 0;
    int swing = vine[0][0];
    int nextSwing = -1;
    int result = 0;
    result = daSie(currVine, swing);
    if(result)
        printf("YES\n");
    else printf("NO\n");
}

int main()
{
    int n;
    scanf("%d", &n);
    for(int i = 0; i < n; i++) {
        printf("Case #%d: ", i + 1);
        solve();
        for(int j = 0; j < MAXN; j++)
            vine[j][0] = vine[j][1] = 0;
    }
    return 0;
}

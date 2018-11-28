#include <iostream>
#include <algorithm>
#include <cstring>
#include <cstdio>
using namespace std;

int itemCount;

void init() {
    int sequence[1010];
    int sortedSequence[1010];
    int lenSequence;
    scanf("%d", &lenSequence);
    for (int i = 1; i <= lenSequence; i ++)
        scanf("%d", &sequence[i]);
    memmove(sortedSequence, sequence, sizeof(sequence));
    sort(sortedSequence+1, sortedSequence+lenSequence+1);
    itemCount = 0;
    for (int i = 1; i <= lenSequence; i ++)
        if (sequence[i] != sortedSequence[i])
            itemCount ++;
}

void solve(int case_id) {
    printf("Case #%d: %d.000000\n", case_id, itemCount);
}

int main() {
    freopen("D-small-attempt0.in", "r", stdin);
    freopen("D-small-attempt0.out", "w", stdout);
    int cs;
    scanf("%d", &cs);
    for (int case_id = 1; case_id <= cs; case_id ++) {
        init();
        solve(case_id);
    }
    return 0;
}

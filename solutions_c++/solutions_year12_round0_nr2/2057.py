#include <string>
#include <cstdio>
#include <algorithm>

using namespace std;


int main() {

    int t;
    scanf("%d\n", &t);

    for(int tt=0; tt<t; ++tt) {
        int n, s, p;
        scanf("%d %d %d\n", &n, &s, &p);

        int score, basescore;

        int justbelow = 0;
        int above = 0;

        for(int i=0; i<n; ++i) {
            scanf("%d", &score);

            basescore = (score + 2) / 3;

            if(basescore >= p) {
                above++;
            }
            else if((basescore == (p-1)) && (score > 1) && (score < 29) && ((score % 3) != 1) ) {
                justbelow++;
            }
        }

        int result = above + min(justbelow, s);

        printf("Case #%d: %d\n", tt+1, result);
    }

    return 0;
}

#include <stdio.h>
#include <vector>
#include <algorithm>

using namespace std;

int getLevel(int n) {
    if (n == 0)
        return 0;
    int re = 0;
    while (n > 0) {
        n /= 2;
        re++;
    }
    return re - 1;
}

void make(bool state[], int n) {
    for (int i = 0; i < 22; i++) {
        if (n % 2 == 1)
            state[i] = !state[i];
        n /= 2;
    }
    printf("debug:");
    for (int i = 21; i >= 0; i--)
        printf(" %d", state[i]);
    printf("\n");
}

int main() {
    int ecase, ecount;
    
    scanf("%d", &ecase);
    for (ecount = 1; ecount <= ecase; ecount++) {
        int en;
        vector<int> kinds[22];
        scanf("%d", &en);
        
        int xorTotal = 0;
        int sum = 0;
        int min = 999999999;
        while (en > 0) {
            int et;
            scanf("%d", &et);
            int tl = getLevel(et);
            kinds[tl].push_back(et);
            xorTotal ^= et;
            sum += et;
            if (et < min)
                min = et;
            en--;
        }
        
        if (xorTotal != 0) {
            printf("Case #%d: NO\n", ecount);
        }
        else {
            /*int ans = 0;
            for (int i = 0; i < 22; i++)
                sort(kinds[i].begin(), kinds[i].end());
            
            bool astate[22];
            bool bstate[22];
            for (int i = 0; i < 22; i++) {
                astate[i] = false;
                bstate[i] = false;
            }
            
            for (int i = 21; i >= 0; i--) {
                int aoffset = 0;
                int boffset = 0;
                if (astate[i] ^ bstate[i])
                    aoffset = 1;
                printf("aoffset = %d, boffset = %d\n", aoffset, boffset);
                int amany = kinds[i].size() / 2 + aoffset;
                int bmany = kinds[i].size() / 2 + boffset;
                
                printf("amany=%d  bmany=%d  (%d)\n", amany, bmany, kinds[i].size());
                for (int j = kinds[i].size() - 1; j >= (int)kinds[i].size() - amany; j--) {
                    //printf("a %d %d\n", i, j);
                    ans += kinds[i][j];
                    //printf("k\n");
                    make(astate, kinds[i][j]);
                    printf("a %d %d (%d)\n", i, j, kinds[i][j]);
                }
                for (int j = kinds[i].size() - amany - 1; j >= 0; j--) {
                    make(bstate, kinds[i][j]);
                    printf("b %d %d\n", i, j);
                }
            }
            */
            printf("Case #%d: %d\n", ecount, sum - min);
        }
    }
    
    return 0;
}

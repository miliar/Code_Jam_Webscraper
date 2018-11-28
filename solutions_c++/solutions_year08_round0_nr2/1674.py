#include <cstdio>
#include <cstdlib>

int probCount;
int rev;
int c1, c2;
int train1[102][2];
int train2[102][2];

int qsort1(const void *a, const void *b) {
    return ((int *)a)[0] - ((int *)b)[0];
}

int qsort2(const void *a, const void *b) {
    return ((int *)a)[1] - ((int *)b)[1];
}

int main() {
    scanf("%d\n", &probCount);
    for(int probIndex=1; probIndex<=probCount; probIndex++) {
        scanf("%d\n", &rev);
        scanf("%d %d\n", &c1, &c2);
        for(int i=0; i<c1; i++) {
            int hr1, mi1, hr2, mi2;
            scanf("%d:%d %d:%d\n", &hr1, &mi1, &hr2, &mi2);
            train1[i][0] = hr1*60+mi1;
            train1[i][1] = hr2*60+mi2;
        }
        for(int i=0; i<c2; i++) {
            int hr1, mi1, hr2, mi2;
            scanf("%d:%d %d:%d\n", &hr1, &mi1, &hr2, &mi2);
            train2[i][0] = hr1*60+mi1;
            train2[i][1] = hr2*60+mi2;
        }
        int ans1 = c1;
        int ans2 = c2;
        qsort((void *)&train1[0][0], c1, sizeof(train1[0][0])*2, qsort1);
        qsort((void *)&train2[0][0], c2, sizeof(train2[0][0])*2, qsort2);
        for(int i=0, j=0;i<c1&&j<c2;i++) {
            if((train2[j][1] + rev) <= train1[i][0]){
                j++;
                ans1--;
            }
        }
        qsort((void *)&train1[0][0], c1, sizeof(train1[0][0])*2, qsort2);
        qsort((void *)&train2[0][0], c2, sizeof(train2[0][0])*2, qsort1);
        for(int i=0, j=0;i<c1&&j<c2;j++) {
            if( (train1[i][1] + rev) <= train2[j][0] ){
                i++;
                ans2--;
            }
        }
        printf("Case #%d: %d %d\n", probIndex, ans1, ans2);
    }
    return 0;
}

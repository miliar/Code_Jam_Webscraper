#include<cstdio>
#include<cstring>
int isRecycledPairMemo[1001][1001];
int isRecycledPair(int n, int m) {
    char buf1[100];
    char buf2[100];
    sprintf(buf1,"%d",n);
    sprintf(buf2,"%d",m);
    int len1 = strlen(buf1);
    int len2 = strlen(buf2);
    if (len1 != len2) return 0;
    for (int i=0; i<len1; i++) {
        // start of chunk
        int ind = i;
        bool laterPart = true;
        bool formerPart = true;
        int j;
        for (j=0; j<len2 && ind < len1; j++, ind++) {
            if (buf1[ind] != buf2[j]) laterPart = false;
        }
        for (ind = 0; j<len2; ind++, j++) {
            if (buf1[ind] != buf2[j]) formerPart = false;
        }
        if (formerPart && laterPart) return 1;
    }
    return 0;
}
void init() {
    int A = 1;
    int B = 1000;
    for (int n=A; n < B; n++) {
        for (int m = n+1; m <= B; m++) {
            isRecycledPairMemo[n][m] = isRecycledPair(n, m);
        }
    }
}
int main() {
    // freopen("C-small-attempt0.in", "r", stdin);
    // freopen("C-small-attempt0.out", "w", stdout);
    int T;
    init();
    scanf("%d",&T);
    for (int kase = 1; kase <= T; kase++) {
        int A, B;
        scanf("%d %d", &A, &B);
        int ans = 0;
        for (int n=A; n < B; n++)
            for (int m = n+1; m <= B; m++)
                ans += isRecycledPairMemo[n][m];
        printf("Case #%d: %d\n",kase, ans);
    }
    return 0;
}

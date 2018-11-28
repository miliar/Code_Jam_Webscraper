#include <cstdio>
#include <cstdlib>
#include <cstring>

#define f0(i, n) for(int i=0; i<n; i++)
#define f1(i, n) for(int i=1; i<=n; i++)
#define max(a, b) ((a) > (b) ? (a) : (b))
#define min(a, b) ((a) < (b) ? (a) : (b))

#define OR 0
#define AND 1

int qsortt(const void *a, const void *b) {
    return ((int *) a)[0] - ((int *) b)[0];
}

int probCount;
int nodeCount;
int inCount;
int wantAll;

int value[10010];
int type[505];
int change[5005];

void getValue(int a) {
    if(value[a] != -1) {
        return;
    }
    getValue(a*2+1);
    getValue(a*2+2);
    if(type[a] == OR) {
        value[a] = value[a*2+1] | value[a*2+2];
    } else {
        value[a] = value[a*2+1] & value[a*2+2];
    }
}

int wantValue(int node, int want) {
    if(value[node] == want) {
        return 0;
    }
    if(node >= inCount) {
        return 9999;
    }
    int left = value[node*2+1];
    int right = value[node*2+2];
    if(change[node] == 0) {
        if(want == 1) {
            if(type[node] == OR) {
                return min(wantValue(node*2+1, 1), wantValue(node*2+2, 1));
            } else {
                return wantValue(node*2+1, 1)+wantValue(node*2+2, 1);
            }
        } else {
            if(type[node] == AND) {
                return min(wantValue(node*2+1, 0), wantValue(node*2+2, 0));
            } else {
                return wantValue(node*2+1, 0)+wantValue(node*2+2, 0);
            }
        }
    } else {
        if(type[node] == AND && (left|right) == want) {
            return 1;
        }
        if(type[node] == OR && (left&right) == want) {
            return 1;
        }
        if(want == 1) {
            if(type[node] == OR) {
                return min(wantValue(node*2+1, 1), wantValue(node*2+2, 1));
            } else {
                return min(wantValue(node*2+1, 1)+wantValue(node*2+2, 1), min(wantValue(node*2+1, 1), wantValue(node*2+2, 1))+1);
            }
        } else {
            if(type[node] == AND) {
                return min(wantValue(node*2+1, 0), wantValue(node*2+2, 0));
            } else {
                return min(wantValue(node*2+1, 0)+wantValue(node*2+2, 0), min(wantValue(node*2+1, 0), wantValue(node*2+2, 0))+1);
            }
        }
    }
    return 9999;
}

int main() {
    scanf("%d", &probCount);
    f1(probIndex, probCount) {
        scanf("%d%d", &nodeCount, &wantAll);
        inCount = (nodeCount-1) / 2;
        int i;
        for(i=0; i<inCount; i++) {
            scanf("%d %d", &type[i], &change[i]);
            value[i] = -1;
        }
        for(; i<nodeCount; i++) {
            scanf("%d", &value[i]);
        }
        getValue(0);
        int ans = wantValue(0, wantAll);
        printf("Case #%d: ", probIndex);
        if(ans < 6000) {
            printf("%d", ans);
        } else {
            printf("IMPOSSIBLE");
        }
        printf("\n");
    }
    return 0;
}

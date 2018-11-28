// 2

#include<cstdio>
#include<cstring>
#include<algorithm>

using namespace std;

const int maxN = 128;

int N, S, P;
int A[maxN];

int make2(int sc)
{
    int i, j, k, mc = -1;
    for(i = 0; i <= 10; i++)
        for(j = i; (j <= i + 2) && (j <= 10); j++)
            for(k = j; (k <= i + 2) && (k <= j + 2) && (k <= 10); ++k) {
                if( i + j + k == sc ) {
                    if( (i + 2 == j) || (i + 2 == k) || (j + 2 == k) ) {
                        //printf("i = %d, j = %d, k = %d\n", i, j, k);
                        mc = max(mc, k);
                    }
                }
            }
    //printf("make2(%d) = %d\n", sc, mc);
    return mc;
}

int big(int sc)
{
    int i, j, k, mc = -1;
    for(i = 0; i <= 10; i++)
        for(j = i; (j <= i + 2) && (j <= 10); j++)
            for(k = j; (k <= i + 2) && (k <= j + 2) && (k <= 10); ++k) {
                if( i + j + k == sc ) {
                    if( (i + 2 != j) && (i + 2 != k) && (j + 2 != k) ) {
                        mc = max(mc, k);
                    }
                }
            }
    //printf("big(%d) = %d\n", sc, mc);
    return mc;
}

struct node
{
    int mk2, big, sel;
};
node B[maxN];

int main()
{
    //freopen("data.in", "r", stdin);
    //freopen("data.out", "w", stdout);
    int nt, idx = 0; scanf("%d", &nt);
    while( (nt --) > 0 ) {
        scanf("%d %d %d", &N, &S, &P);
        for(int i = 0; i < N; ++i) scanf("%d", A + i);
        for(int i = 0; i < N; ++i) {
            B[i].mk2 = make2(A[i]);
            B[i].big = big(A[i]);
            B[i].sel = 0;

            if( S && B[i].big == -1 ) {
                B[i].sel = -1;
                -- S;
            }
        }

        for(int i = 0; S && i < N; ++i) {
            if( B[i].sel == 0 ) {
                if( B[i].big < P && B[i].mk2 >= P ) {
                    --S;
                    B[i].sel = -1;
                }
            }
        }

        for(int i = 0; S && i < N; ++i) {
            if( B[i].sel == 0 ) {
                if( B[i].big < P ) {
                    --S;
                    B[i].sel = -1;
                }
            }
        }

        for(int i = 0; S && i < N; ++i) {
            if( B[i].sel == 0 ) {
                if( B[i].mk2 >= P ) {
                    --S;
                    B[i].sel = -1;
                }
            }
        }

        int ans = 0;
        for(int i = 0; i < N; ++i)
            if( B[i].sel == 0 )
                ans += (B[i].big >= P);
            else
                ans += (B[i].mk2 >= P);

        printf("Case #%d: %d\n", ++idx, ans - S);
    }
    return 0;
}

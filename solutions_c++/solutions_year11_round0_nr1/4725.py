#include<cstdio>
#include<cstring>
#include<iostream>
#include<algorithm>

using namespace std;

const int maxN = 128;

template<class T> T cAbs(T x) { if(x < 0) return -x; return x; }

struct node
{
    int idx, pos;
};

node O[maxN], B[maxN];
int N, pos; char str[3];
int cntO, cntB;

int calc()
{
    int curO = 1, curB = 1;
    int tO = 0, tB = 0;
    for(int i = 0, j = 0; i < cntO || j < cntB; ) {
        //printf("curO = %d, tO = %d; curB = %d, tB = %d\n", curO, tO, curB, tB);
        if( i == cntO ) {
            if( B[j].pos == curB ) ++tB, ++j;
            else if( B[j].pos > curB ) {
                tB += B[j].pos - curB + 1;
                curB = B[j].pos;
                ++j;
            } else {
                tB += curB - B[j].pos + 1;
                curB = B[j].pos;
                ++j;
            }
        } else if(j == cntB) {
            if( O[i].pos == curO ) ++tO, ++i;
            else if( O[i].pos > curO ) {
                tO += O[i].pos - curO + 1;
                curO = O[i].pos;
                ++i;
            } else {
                tO += curO - O[i].pos + 1;
                curO = O[i].pos;
                ++i;
            }
        } else {
            int _O = cAbs(O[i].pos - curO) + 1;
            int _B = cAbs(B[j].pos - curB) + 1;

            if( O[i].idx < B[j].idx ) {
                tO += _O;
                if(_B <= _O) curB = B[j].pos, tB = tO;
                else {
                    if( B[j].pos >= curB ) curB += _O;
                    else curB -= _O;
                    tB += _O;
                }
                curO = O[i].pos;

                ++i;
            } else {
                tB += _B;
                if(_O <= _B) curO = O[i].pos, tO = tB;
                else {
                    if( O[i].pos >= curO ) curO += _B;
                    else curO -= _B;
                    tO += _B;
                }
                curB = B[j].pos;

                ++j;
            }
        }
    }

    return max(tO, tB);
}

int main()
{
    //freopen("data.in", "r", stdin);
    //freopen("data.out", "w", stdout);
    int t, tt = 1;
    scanf("%d", &t);
    for(tt = 1; tt <= t; ++tt) {
        scanf("%d", &N);
        cntO = cntB = 0;
        for(int i = 0; i < N; ++i) {
            scanf("%s %d", str, &pos);

            if(str[0] == 'O') {
                O[cntO].idx = i;
                O[cntO].pos = pos;
                ++cntO;
            } else {
                B[cntB].idx = i;
                B[cntB].pos = pos;
                ++cntB;
            }
        }

        printf("Case #%d: %d\n", tt, calc());
    }
    return 0;
}

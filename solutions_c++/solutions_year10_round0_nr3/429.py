#include<iostream>
#include<cstring>
#include<stdio.h>
#include<algorithm>
#include<set>
#include<cmath>
#include<map>
#include<string>
#include<sstream>
#include<queue>

using namespace std;

int G[1003];
int EveryStart[1003];
long long EverySum[1003];
int lis[1003];
long long sum[1003];

int main() {

    // freopen("C-small.in", "r", stdin);
    // freopen("C-small.out", "w", stdout);
    freopen("C-large.in", "r", stdin);
    freopen("C-large.out", "w", stdout);
    int cas;
    scanf("%d", &cas);
    for (int nth = 1; nth <= cas; nth++) {
        int N, K, R;
        scanf("%d%d%d", &R, &K, &N);
        for (int i = 0; i < N; i++) scanf("%d", &G[i]);
        long long HaveRun = 0;
        memset(EveryStart, -1, sizeof (EveryStart));
        memset(lis, -1, sizeof (lis));
        memset(sum, 0, sizeof (sum));
        int next = 0, last = 0;
        for (int i = 0; i <= N * N + 1; i++) {
            int p = 0;
            long long CurP = 0, Ans;

            //  cout << next << endl;
            // cout << EveryStart[next] << "**" << endl;

            if (EveryStart[next] != -1) {
                if (R <= HaveRun) Ans = sum[R];
                else {
                    long long Circle = sum[HaveRun] - sum[EveryStart[next] - 1];
                    Ans = sum[HaveRun]+(R - HaveRun) / (HaveRun - EveryStart[next] + 1) * Circle;
                    long long Lef = (R - HaveRun) % (HaveRun - EveryStart[next] + 1);
                    int CurLocation = next;
                    //  cout << Ans << " " << Lef << endl;

                    while (Lef--) {
                        Ans += EverySum[CurLocation];
                        // cout << "location" << CurLocation << " " << EverySum[CurLocation] << endl;
                        CurLocation = lis[CurLocation];
                    }
                }
                cout << "Case #" << nth << ": " << Ans << endl;
                break;
            }
            while (p < N && CurP + G[(next + p) % N] <= K) {
                CurP += G[(next + p) % N], p++;
            }
            EveryStart[next] = HaveRun + 1;
            EverySum[next] = CurP;
            // cout << CurP << "*********" << endl;

            lis[last] = (next + p) % N;
            next = last = (next + p) % N;
            sum[HaveRun + 1] = sum[HaveRun] + CurP;
            HaveRun++;
        }


    }



    return 0;
}


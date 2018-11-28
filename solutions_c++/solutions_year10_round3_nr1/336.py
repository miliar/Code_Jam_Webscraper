

#include<vector>
#include<sstream>
#include<iostream>
#include<cstring>
#include<cmath>
#include<string>
#include<map>


using namespace std;

int Y1[1003], Y2[1003];

int main() {
    //  freopen("A-small.in", "r", stdin);
    //  freopen("A-small.out", "w", stdout);
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    int cas;
    scanf("%d", &cas);
    for (int nth = 1; nth <= cas; nth++) {
        int N;
        scanf("%d", &N);
        for (int i = 1; i <= N; i++) {
            scanf("%d%d", &Y1[i], &Y2[i]);
        }
        int ans = 0;
        for (int i = 1; i <= N; i++) {
            for (int j = i + 1; j <= N; j++) {
                if (Y1[i] > Y1[j] && Y2[i] < Y2[j]) ans++;
                if (Y1[i] < Y1[j] && Y2[i] > Y2[j]) ans++;
            }
        }
        printf("Case #%d: %d\n", nth, ans);

    }
}

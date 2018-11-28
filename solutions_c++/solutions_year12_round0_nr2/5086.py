#include<iostream>
using namespace std;
int main(){

    freopen("B-small-attempt0.in", "r", stdin);
    int T, N, S, p;
    int answer[200];
    scanf("%d", &T);
    for(int i=0; i<T; i++){
        scanf("%d %d %d", &N, &S, &p);
        int ans = 0;
        int t;
        int p3 = p*3;
        for(int j=0; j<N; j++){
            scanf("%d", &t);
            if(t >= p3-2)
                ans++;
            int big = p;
            big +=(p-1>=0? p-1:0);
            big +=(p-2>=0? p-2:0);
            int small = p;
            small += (p-2>=0?p-2:0)*2;
            if(S>0 && (t>=small && t<=big)){
                S--;
                ans++;
            }
        }

        answer[i]=ans;
    }

    freopen("B-small-attempt0.out", "w", stdout);
    for(int i=0; i<T; i++)
        printf("Case #%d: %d\n", i+1, answer[i]);
    return 0;
}

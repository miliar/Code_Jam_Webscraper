#include<iostream>
#include<algorithm>
#include<cstring>
using namespace std;
int P, Q;
bool prison[128];
int a[6],b[6];
int find(int id){
    int i, cnt = 0;
    for(i = id -1; i > 0 && prison[i]; i--)cnt++;
    for(i = id + 1; i <= P && prison[i]; i++)cnt++;
    return cnt;
}
int main() {
    freopen("C-small-attempt0.in", "r", stdin);
    freopen("ans.txt", "w", stdout);
    int cas, T, i;
    cin >> T;
    for (cas = 1; cas <= T; cas++) {
        printf("Case #%d: ", cas);
        scanf("%d %d",&P, &Q);
        for(i = 0; i < Q; i++)
        {
            scanf("%d",&a[i]);
            b[i] = i;
        }
        int best = 1<<28;
        do{
           memset(prison, true, sizeof(prison) );
           int ans = 0;
           for(i = 0; i < Q; i++)
           {
               ans += find(a[b[i]]);
               prison[ a[b[i]] ] = false;
           }
           if(ans < best)best = ans;
        }while(next_permutation(b, b + Q));

        printf("%d\n", best);
    }

}


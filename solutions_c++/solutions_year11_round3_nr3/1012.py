#include <iostream>
#include <cstdio>
using namespace std;
long long fre[10010];
int main()
{
    int t, n;
    int flag, con = 1;
    long long l, h;
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    scanf("%d", &t);
    while(t--){
        scanf("%d %lld %lld", &n, &l, &h);
        printf("Case #%d: ", con++);
        for(int i = 0; i < n; i++)  scanf("%lld", &fre[i]);
        for(long long i = l; i <= h; i++){
            flag = 0;
            for(int j = 0; j < n; j++){
                if((i % fre[j]) && (fre[j] % i)){
                    flag = 1;
                    break;
                }
            }
            if(!flag) {
                printf("%lld\n", i);
                break;
            }
        }
        if(flag) printf("NO\n");
    }
    return 0;
}

#include<iostream>
using namespace std;
int n;
int a[10000],b[10000];
bool cmp(const int &a,const int &b){
    return a > b;
}
int main(){
    int cnt;
    freopen("out.txt","w",stdout);
    scanf("%d", &cnt);
    for(int t = 1; t <= cnt; t++){
        scanf("%d",&n);
        for(int i = 0; i < n; i++)
            scanf("%d", &a[i]);
        for(int i = 0; i < n; i++)
            scanf("%d", &b[i]);
        sort(a,  a + n);
        sort(b, b + n, cmp);
        long long ans = 0;
        for (int i = 0; i < n ; i++)
            ans += (long long)(a[i]) * (b[i]);
        printf("Case #%d: %lld\n", t, ans);
    }
}

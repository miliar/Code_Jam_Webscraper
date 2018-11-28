#include<iostream>
#include<cstdio>
#include<cmath>
#include<algorithm>
using namespace std;

int main(){
    //freopen("B-large.in", "r", stdin);
    //freopen("B-large.out", "w", stdout);
    int n, s, p, T, i, a[105], ans, cas=1;
    scanf("%d", &T);
    while(T--){
        ans=0;
        scanf("%d%d%d", &n, &s, &p);
        for(i=0; i<n; i++)
        scanf("%d", &a[i]);
        sort(a, a+n);
        for(i=0; i<n; i++){
            if(a[i]%3==1){
                if(a[i]/3+1>=p)ans++;
            }
            else if(a[i]%3==0){
                if(a[i]/3>=p)ans++;
                else if(s&&a[i]/3-1>=0&&a[i]/3+1>=p){s--;ans++;}
            }
            else {
                if(a[i]/3+1>=p)ans++;
                else if(s&&a[i]/3+2>=p){s--;ans++;}
            }
        }
        printf("Case #%d: %d\n", cas++, ans);
    }
    return 0;
}

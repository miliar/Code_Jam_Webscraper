#include<iostream>
#include<cstdio>
#include<cmath>
#include<cstring>
using namespace std;
int p[10];
bool check(int x, int y){
    if(x==y)return false;
    char s1[10], s2[10], s3[10];
    int len=0, i=x;
    while(i){
        i/=10;len++;
    }
    for(i=0; i<len; i++){
        if((x/p[len-i]+(x%p[len-i])*p[i])==y)
        return true;
    }
    return false;
}
int main(){
    //freopen("C-small-attempt0.in", "r", stdin);
    //freopen("C-small-attempt0.out", "w", stdout);
    int T, i, j, a, b, ans, cas=1;
    p[0]=1;
    for(i=1; i<=9; i++)p[i]=p[i-1]*10;
    scanf("%d", &T);
    while(T--){
        ans=0;
        scanf("%d%d", &a, &b);
        for(i=a; i<=b; i++){
            for(j=i; j<=b; j++){
                if(check(i, j))
                    ans++;
                    //printf("Tt");
            }
        }
        printf("Case #%d: %d\n", cas++, ans);
    }
    return 0;
}

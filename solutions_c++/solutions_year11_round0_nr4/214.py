#include<iostream>
#include<cstring>
#include<cstdio>
#include<algorithm>
#include<cmath>
using namespace std;

#define N 1111
int n;
int array[N];
bool vis[N];
int main(){
    int i,j,k;
    int cas,ans;
    //freopen("D.in","r",stdin);
    //freopen("D.out","w",stdout);
    scanf("%d",&cas);
    for(k = 1; k <= cas; k++){
        scanf("%d",&n);
        ans = n;
        for(i = 1; i <= n; i++){
            scanf("%d",&array[i]);
            if(array[i] == i) ans--;
        }
        printf("Case #%d: %.6f\n",k,(double)ans);
    }
    return 0;
}

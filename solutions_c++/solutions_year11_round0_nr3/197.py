#include<iostream>
#include<cstdio>
#include<cmath>
#include<cstdlib>
#include<cstring>
#include<string>
#include<algorithm>
#include<vector>
using namespace std;
int a[2000];
int N;
int main(){
    freopen("C-large.in","r",stdin);
    freopen("C-large.out","w",stdout);
    int cas;
    scanf("%d",&cas);
    for(int ca=1;ca<=cas;ca++){
        scanf("%d",&N);
        for(int i=0;i<N;i++){
            scanf("%d",&a[i]);
        }
        sort(a,a+N);
        int sum=0,tmp=0;;
        for(int i=1;i<N;i++){
            sum+=a[i];
            tmp^=a[i];
        }
        if(tmp==a[0]){
            printf("Case #%d: %d\n",ca,sum);
        }else{
            printf("Case #%d: NO\n",ca);
        }
    }
    return 0;
}

#include<stdio.h>
#include<stdlib.h>
#include<algorithm>
using namespace std;
#define MAXN 2000
int a[MAXN];
int cal(int n){
    int sum=0,t=0,mina=10000000;
    for(int i=0;i<n;i++){
        sum+=a[i];
        t^=a[i];
        mina=min(mina,a[i]);
    }
    if(t!=0)return 0;
    return sum-mina;
}
int main(){
    freopen("C-large.in.txt","r",stdin);
    freopen("C-large.out","w",stdout);
    int kase,kases=1;
    scanf("%d",&kase);
    while(kase--){
        int n;
        scanf("%d",&n);
        for(int i=0;i<n;i++)scanf("%d",&a[i]);
        int ans = cal(n);
        printf("Case #%d: ",kases++);
        if(ans==0)printf("NO\n");
        else printf("%d\n",ans);
    }
}
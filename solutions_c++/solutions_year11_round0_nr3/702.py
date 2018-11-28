#include <stdio.h>
#include <iostream>
using namespace std;

int t,n,f;
int a[1010];
int i,m,sum,tmp;

int main(){
    freopen("C-large.in","r",stdin);
    freopen("C-large.txt","w",stdout);
    scanf("%d",&t);
    for(i=1;i<=t;++i){
        scanf("%d %d",&n,&f);
        --n;
        sum=m=f;
        while(n--){
            scanf("%d",&tmp);
            sum+=tmp;
            f^=tmp;
            if(m>tmp) m=tmp;
        }
        printf("Case #%d: ",i);
        if(f==0)
            printf("%d\n",sum-m);
        else
            printf("NO\n");
    }
}

#include<stdio.h>
#include<algorithm>
using namespace std;
int main(){
    int C,n,a[1000],result,sum,Case=1;
    scanf("%d",&C);
    while(C--){
        scanf("%d",&n);
        result=sum=0;
        for(int i=0;i<n;i++){
            scanf("%d",&a[i]);
            result^=a[i];
            sum+=a[i];
        }
        printf("Case #%d: ",Case++);
        if(result==0){
            sort(a,a+n);
            printf("%d\n",sum-a[0]);
        }else puts("NO");
    }
}

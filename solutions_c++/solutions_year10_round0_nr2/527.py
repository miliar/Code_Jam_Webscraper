#include<stdio.h>
#include<stdlib.h>

int main(){
    freopen("out2.out","w",stdout);
    freopen("B-small-attempt1.in","r",stdin);
    int t;
    scanf("%d",&t);
    for(int i=1;i<=t;i++){
        int n;
        scanf("%d",&n);
        int a[10];
        for(int j=0;j<n;j++)scanf("%d",&a[j]);
        int min=a[0];
        for(int j=0;j<n;j++)if(a[j]>min)min=a[j];
        int con=0;
        while(min>=0&&con==0){
            int k=a[0]%min;
            con=1;
            for(int j=1;j<n;j++)if(a[j]%min!=k)con=0;
            if(con==1){
                    if(a[0]%min==0)
                    printf("Case #%d: 0\n",i);
                    else printf("Case #%d: %d\n",i,min- (a[0]%min));
            }
            min--;
        }
    }
}

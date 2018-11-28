# include <stdio.h>
# include <stdlib.h>
# include <vector>
using namespace std;
int main(){
    freopen("C-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    int c,i,j,k,n,sum,men;
    scanf("%d",&c);
    for(k=1;k<=c;k++){
        scanf("%d",&n);
        int res=0,val;
        men=30000000,sum=0;
        for(i=0;i<n;i++){
            scanf("%d",&val);
            res=res^val;
            sum+=val;
            men=min(men,val);
        }
        printf("Case #%d: ",k);
        if(res!=0){
            printf("NO\n");
        }else{
            printf("%d\n",sum-men);
        }
    }
    return 0;
}

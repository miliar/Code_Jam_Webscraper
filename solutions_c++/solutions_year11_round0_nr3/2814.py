#include<stdio.h>

int main(){
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    int t,data[110],n,Case=1;
    scanf("%d",&t);
    while(t--){
        scanf("%d",&n);
        for(int i=0;i<n;++i){
            scanf("%d",&data[i]);
        }
        int m=1<<(n-1);
        int max=-1;
        for(int i=1;i<m;++i){
            int sum1=0,sum2=0;
            int a=0,b=0;
            int x=i;
            for(int j=0;j<n;++j){
                if(x&1==1){
                    sum1+=data[j];
                    a^=data[j];
                }else{
                    sum2+=data[j];
                    b^=data[j];
                }
                x>>=1;
            }
            if(a==b){
                if(sum1>max)max=sum1;
                if(sum2>max)max=sum2;
            }
        }
        if(max==-1){
            printf("Case #%d: NO\n",Case++);
        }
        else{
            printf("Case #%d: %d\n",Case++,max);
        }
    }
    return 0;
}



//    freopen("in", "r", stdin);
//       freopen("out", "w", stdout);

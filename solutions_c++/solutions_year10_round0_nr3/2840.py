//Theme park

#include"cstdio"
#include"cstdlib"

int g[10000005];

int main(){
    int t,r,k,n;
    int sum,tk,ind,count;
    freopen("A-small.in","r",stdin);
    freopen("A-smal.txt","w",stdout);
    scanf("%d",&t);
    for(int i = 1;i<=t;i++){
        scanf("%d %d %d",&r,&k,&n);
        for(int j = 0;j<n;j++) scanf("%d",&g[j]);
        sum = 0;
        ind = 0;
        for(int j = 0;j<r;j++){
            tk = 0;
            count = 0;
            while(tk<k&&count<n){
                tk += g[ind];
                count++;
                ind = (ind+1)%n;
            }
            //ind = (ind+n-1)%n;
            //printf("tk = %d g[%d] = %d\n",tk,ind,g[ind]);
            if(tk>k){
                tk -= g[(ind+n-1)%n];
                ind = (ind+n-1)%n;
            }
            //printf("tk = %d g[%d] = %d\n",tk,ind,g[ind]);
            sum+=tk;        
        }    
        printf("Case #%d: %d\n",i,sum);
    }    
    fclose(stdin);
    fclose(stdout);
    system("pause");
    return 0;
}    

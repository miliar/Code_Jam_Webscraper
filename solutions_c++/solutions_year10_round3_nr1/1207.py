#include"cstdio"
#include"cstdlib"

int list[1010][2];
int main(){
    freopen("A-small-attempt0.in","r",stdin);
    freopen("A-small-attempt0.out","w",stdout);
    int t,n,count;
    scanf("%d",&t);
    for(int i = 1;i<=t;i++){
        scanf("%d",&n);
        count = 0;
        for(int j = 0;j<n;j++){
            scanf("%d %d",&list[j][0],&list[j][1]);
        }
        for(int j = 0;j<n-1;j++){
            for(int x = j+1;x<n;x++){
                if(list[j][0]<list[x][0]&&list[j][1]>list[x][1]||list[j][0]>list[x][0]&&list[j][1]<list[x][1])
                count++;
            }    
        }
        printf("Case #%d: %d\n",i,count);        
    }    
    return 0;
}    

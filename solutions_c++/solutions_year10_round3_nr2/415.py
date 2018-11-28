#include"iostream"
#include"cmath"
using namespace std;
__int64 data[11][100];
int main(){
    freopen("B-large.in","r",stdin);
    freopen("bsout4.txt","w",stdout);
    for(int i=2;i<=10;i++){
         __int64 res=1;
         data[i][0]=1;
         for(int j=1;res<2000000000;j++){
            res=res*i;
            data[i][j]=res;
         }
    }
    int T,L,P,C;
    scanf("%d",&T);
    for(int i=1;i<=T;i++){
        scanf("%d%d%d",&L,&P,&C);
        int t=-1;
        while(1){
           if(L*data[C][++t]>=P)break;
        }
        int k=-1;
        while(1){
           if(data[2][++k]>=t)break;
        }
        printf("Case #%d: %d\n",i,k);
    }
    return 0;
}

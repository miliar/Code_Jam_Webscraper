#include<stdio.h>
#include<algorithm>
#include<math.h>
using namespace std;
#define eps 1e-9
#define SIZE 1000
struct data{
    int No,P,L;
    bool operator<(const data b)const{
        double tmp1=(P*0.01*b.P*0.01*(L+b.L)+P*0.01*(1-b.P*0.01)*(L+b.L)+(1-P*0.01)*L);
        double tmp2=(P*0.01*b.P*0.01*(L+b.L)+b.P*0.01*(1-P*0.01)*(L+b.L)+(1-b.P*0.01)*L);
        if(fabs(tmp1-tmp2)<eps)return No<b.No;
        return tmp1<tmp2;
    }
}a[SIZE];
int main(){
    int cs=0,i,j,T,N;
    scanf("%d",&T);
    while(T--){
        scanf("%d",&N);
        for(i=0;i<N;i++)a[i].No=i;
        for(i=0;i<N;i++)scanf("%d",&a[i].L);
        for(i=0;i<N;i++){
            scanf("%d",&a[i].P);
            a[i].P=100-a[i].P;
        }
        sort(a,a+N);
        printf("Case #%d:",++cs);
        for(i=0;i<N;i++)printf(" %d",a[i].No);
        puts("");
    }
    return  0;
}

#include"stdio.h"
#include"string.h"
#include"math.h"
#include"iostream"
#include"algorithm"
using namespace std;
int t,n;
struct Line{
    int L,R;
}pp[10];

int main(){
    freopen("A-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    scanf("%d",&t);
    for(int i=1;i<=t;i++){
        scanf("%d",&n);
        for(int i=1;i<=n;i++) scanf("%d%d",&pp[i].L,&pp[i].R);
        int num=0;
        for(int i=1;i<=n;i++){
            for(int j=i+1;j<=n;j++){
                int c1=pp[j].L-pp[i].L;
                int c2=pp[j].R-pp[i].R;
                if(c1>0&&c2<0||c1<0&&c2>0) num++;
            }
        }
        printf("Case #%d: %d\n",i,num);
    }
    return 0;
}

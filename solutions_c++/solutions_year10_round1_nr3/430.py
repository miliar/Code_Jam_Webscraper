#include<stdio.h>
#include<algorithm>
#include<math.h>
#include<string.h>
#include<vector>
#include<map>
#include<queue>
#include<string>
#include<stdlib.h>
using namespace std;
int t=0;
bool mytest(int x,int y){
    bool flag;
    if(x==y)return 0;
    if(x<y)return mytest(y,x);
    if(x/y>=2)return 1;
    flag=mytest(y,x-y);
    if(flag==1)return 0;
    else return 1;
}
main(){
    freopen("C-small-attempt0.in","r",stdin);
    freopen("C-small.out","w",stdout);
    int i,j,T,an,A1,A2,B1,B2;
    scanf("%d",&T);
    while(T--){
        t++;
        scanf("%d %d %d %d",&A1,&A2,&B1,&B2);
        an=0;
        for(i=A1;i<=A2;i++)
            for(j=B1;j<=B2;j++)if(mytest(i,j))an++;
        printf("Case #%d: %d\n",t,an);
    }
}

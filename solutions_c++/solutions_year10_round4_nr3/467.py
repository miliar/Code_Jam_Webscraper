#include<stdio.h>
#include<algorithm>
#include<math.h>
#include<string.h>
#include<vector>
#include<map>
#include<queue>
#include<string>
#include<stdlib.h>
#define SIZE 110
using namespace std;
int Max(int x,int y){return x>y?x:y;}
int Min(int x,int y){return x<y?x:y;}
int Map[SIZE][SIZE],t,Mx,My;
void Fill(int x1,int y1,int x2,int y2){
    int i,j;
    for(i=x1;i<=x2;i++){
        for(j=y1;j<=y2;j++)Map[i][j]=t;
    }
}
bool Go(){
    int i,j;
    bool flag=0;
    for(i=Mx;i>0;i--)
        for(j=My;j>0;j--){
            if(Map[i][j]==t)flag=1;
            if(Map[i-1][j]==t&&Map[i][j-1]==t)Map[i][j]=t;
            if(Map[i-1][j]!=t&&Map[i][j-1]!=t)Map[i][j]=0;
        }
    return flag;
}
main(){
    freopen("C-small-attempt0.in","r",stdin);
    freopen("C-small.out","w",stdout);
    int an,i,T,R,x1,x2,y1,y2;
    scanf("%d",&T);
    while(T--){
        t++;
        scanf("%d",&R);
        Mx=My=0;
        for(i=0;i<R;i++){
            scanf("%d %d %d %d",&x1,&y1,&x2,&y2);
            Fill(x1,y1,x2,y2);
            Mx=Max(Mx,x1);
            Mx=Max(Mx,x2);
            My=Max(My,y1);
            My=Max(My,y2);
        }
        an=0;
        while(Go())an++;
        printf("Case #%d: %d\n",t,an);
    }
}

// small
/*
   其面积A和内部格点数目i、边上格点数目b的关系：A = i + b/2 - 1；
   gcd（|x1－x2|，|y1－y2|）；
*/
#include <stdio.h>
#include <iostream>
#include <algorithm>
using namespace std;
int n,m,A;

int det(int x1,int y1,int x2,int y2){
    int t=x1*y2-x2*y1;
    if(t<0)t=-t;
    return t;
}

void work(){
     bool f=false;
     for(int i=0;i<n*m;i++)
        for(int j=0;j<n*m;j++){
           if(det(i/m,i%m,j/m,j%m)==A){
                   printf("0 0 %d %d %d %d\n",i/m,i%m,j/m,j%m);
                   f=true;
                   return ;
               } 
     } 
     if(f==false)printf("IMPOSSIBLE\n");       
}
int main(){
    freopen("data.in","r",stdin);
    freopen("data.out","w",stdout);
    int cases,k=1;
    scanf("%d",&cases);
    while(cases-->0){
         scanf("%d%d%d",&n,&m,&A);
         n++;m++;
         printf("Case #%d: ",k++);
         work();     
    }
    return 0;   
}

#include<stdio.h>
#include<conio.h>
#include<string.h>
int main()
{
    int b[120][120]={0},T,cases,rowcount,i,j,x1,x2,y1,y2,ans,c,flag;
    scanf("%d",&T);
    for(cases=1;cases<=T;cases++){
       int a[120][120],mx,my;
       memset(a,0,120*120*sizeof(int));                           
       scanf("%d",&rowcount);
       for(c=0;c<rowcount;c++){
           scanf("%d%d%d%d",&x1,&y1,&x2,&y2);
           if(mx<x2) mx=x2;
           if(my<y2) my=y2;
           for(i=y1;i<=y2;i++){
               for(j=x1;j<=x2;j++){
                   a[i][j]=1;
               }
           }
       }
       ans=0;
       while(1){
//           for(i=1;i<=6;i++){
//               for(j=1;j<=6;j++){
//                   printf("%d",a[i][j]);
//               }
//               printf("\n");
//           }
//           printf("\n");
//           getch();
           flag=0;
                if(!memcmp(a,b,120*120*sizeof(int) ));
                ans++;
                for(i=my;i>0;i--){
                    for(j=mx;j>0;j--){
                        if(a[i][j]){
                             if(a[i][j]=a[i-1][j]|a[i][j-1])
                                flag=1;
                        }
                        else{
                             if(a[i][j]=a[i-1][j]&a[i][j-1])
                                 flag=1;
                        }
                    }
                }
                if(!flag) break;
       }
       printf("Case #%d: %d\n",cases,ans);
    }
//   while(1);
   return 0;
}

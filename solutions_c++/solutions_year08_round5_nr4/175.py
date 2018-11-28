#include<iostream>
#define INF 1000000
#define MD 10007
int v[1000][1000],f[1000][1000];
main(){
     int tt,t,n,i,j,w,h,x,y,r;
     freopen("d2.in","r",stdin);
     freopen("d2.out","w",stdout);
     scanf("%d",&t);
     for(tt=1;tt<=t;tt++){
          scanf("%d",&h);
          scanf("%d",&w);
          scanf("%d",&r);
           for(i=1;i<=h;i++){
               for(j=1;j<=w;j++){
                    v[i][j]=0;
               }
          }
          for(i=0;i<r;i++){
               scanf("%d",&x);
               scanf("%d",&y);
               f[x][y]=tt;
          }
          for(x=1;x<=h;x++){
               for(y=1;y<=w;y++){
                    if(x==1&&y==1){v[x][y]=1;}else{v[x][y]=0;}
                    if(f[x][y]==tt){continue;}
                    if(x>=2&&y>=3){v[x][y]+=v[x-1][y-2];v[x][y]%=MD;}
                    if(x>=3&&y>=2){v[x][y]+=v[x-2][y-1];v[x][y]%=MD;}
                    //printf("%5d ",v[x][y]);
               }//printf("\n");
          }
          printf("Case #%d: %d\n",tt,v[h][w]%MD);
     }
     return 0;
}

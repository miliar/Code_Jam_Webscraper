#include<iostream>
#include<cstring>
char p[6006][6006],s[1000];
int mnx[6006],mxx[6006],mny[6006],mxy[6006];
main(){
     int tt,t,n,i,j,x,y,c,k,l,dir;
     int ans,hvlf,cnt,md;
     freopen("al.in","r",stdin);
     freopen("al.out","w",stdout);
     scanf("%d",&t);
     for(tt=1;tt<=t;tt++){
          scanf("%d",&n);
          ans = 0;
          x = 3001;
          y = 3001;
          dir = 1;
          for(i=0;i<=6003;i++){
               for(j=0;j<=6003;j++){
                    p[i][j]=0;
               }
               mnx[i]=6006;
               mny[i]=6006;
               mxx[i]=-6006;
               mxy[i]=-6006;
          }
          for(i=0;i<n;i++){
               scanf("%s",s);
               scanf("%d",&c);
               l = strlen(s);
               for(j=0;j<c;j++){
                    for(k=0;k<l;k++){
                         if(s[k]=='F'){
                              if(dir==1){p[x][y]=1;x--;}
                              if(dir==2){y++;}
                              if(dir==3){x++;p[x][y]=1;}
                              if(dir==0){y--;}
                         }else if(s[k]=='R'){
                              dir = (dir+1)%4;
                         }else{
                              dir = (dir+3)%4;
                         }
                    }
               }
          }
          for(i=0;i<=6003;i++){
               hvlf=0;
               cnt =0;
               md  =0;
               for(j=0;j<=6003;j++){
                    if(p[i][j]==1){
                         if(md==0){
                              md=1;
                         }else if(md==1){
                              md=0;
                         }
                    }
                    if(md==1){
                         mnx[i]<?=j;
                         mxx[i]>?=j;
                         mny[j]<?=i;
                         mxy[j]>?=i;
                    }
               }
          }
          for(i=0;i<=6003;i++){
               hvlf=0;
               cnt =0;
               md  =0;
               for(j=0;j<=6003;j++){
                    if(p[i][j]==1){
                         if(md==0){
                              md=1;
                         }else if(md==1){
                              md=0;
                         }
                    }
                    if(md==0&&((mnx[i]<=j&&j<=mxx[i])||(mny[j]<=i&&i<=mxy[j]))){
                         ans++;
                    }
               }
          }
          printf("Case #%d: %d\n",tt,ans);
     }
     return 0;
}

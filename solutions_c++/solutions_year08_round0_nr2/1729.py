#include<iostream>
using namespace std;
pair<int,int> p[300];
main(){
     int t,tt,na,nb,idl,hr,mn,a,b,ca,cb,i;
     freopen("B-large.in","r",stdin);
     freopen("B-large.out","w",stdout);
     scanf("%d",&t);
     for(tt=1;tt<=t;tt++){
          scanf("%d",&idl);
          scanf("%d",&na);
          scanf("%d",&nb);
          for(i=0;i<na;i++){
               scanf("%d:%d",&hr,&mn);
               p[i*2]  =pair<int,int>(hr*60+mn,2);
               scanf("%d:%d",&hr,&mn);
               p[i*2+1]=pair<int,int>(hr*60+mn+idl,1);
          }
          for(i=na;i<na+nb;i++){
               scanf("%d:%d",&hr,&mn);
               p[i*2]  =pair<int,int>(hr*60+mn,3);
               scanf("%d:%d",&hr,&mn);
               p[i*2+1]=pair<int,int>(hr*60+mn+idl,0);
          }
          sort(p,p+(2*(na+nb)));
          a = 0; ca = 0;
          b = 0; cb = 0;
          for(i=0;i<2*(na+nb);i++){
               if(p[i].second==0){
                    a++;
               }else if(p[i].second==1){
                    b++;
               }else if(p[i].second==2){
                    if(a<=0){
                         a++;
                         ca++;
                    }
                    a--;
               }else if(p[i].second==3){
                    if(b<=0){
                         b++;
                         cb++;
                    }
                    b--;
               }
          }
          printf("Case #%d: %d %d\n",tt,ca,cb);
     }
     return 0;
}

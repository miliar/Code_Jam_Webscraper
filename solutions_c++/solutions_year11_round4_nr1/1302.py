#include <cstdio>
#include <math.h>
#include <algorithm>
#include <cstdlib>
int Q,X,S,R,E;
double res,r,d,T,a,b,c,tmp;
double ES[1024][3];
using namespace std;
int main(){
    scanf("%d",&Q);
    for(int q=1;q<=Q;q++){
      res=0;
      scanf("%d %d %d %Lf %d",&X,&S,&R,&T,&E);
      for(int i=0;i<E;i++){
        scanf("%Lf %Lf %Lf",&ES[i][0],&ES[i][1],&ES[i][2]);
        X-=ES[i][1]-ES[i][0];
      }
      if (X>0){
      r=1.0*X/R;
      d=1.0*X/S;
      if(T>0){
          if (T>=r){
            res+=r;
            T-=r;
          }else{
            X-=(T*(R));
            res+=T;
            res+=1.0*X/(S);
            T=-1;
          }
        }else{
          res+=d;
        }  
        
      }
      for(int i=0;i<E;i++){
        for(int j=0;j<E;j++){
          if(ES[i][2]<ES[j][2]){
            tmp=ES[i][0];ES[i][0]=ES[j][0];ES[j][0]=tmp;
            tmp=ES[i][1];ES[i][1]=ES[j][1];ES[j][1]=tmp;
            tmp=ES[i][2];ES[i][2]=ES[j][2];ES[j][2]=tmp;
          } 
        }
      }
      for(int i=0;i<E;i++){
        a=ES[i][0];b=ES[i][1];c=ES[i][2];
        X-=(b-a);
        r=(1.0*(b-a))/(c+R);
        d=(1.0*(b-a))/(c+S);
        if(T>0){
          if (T>=r){
            res+=r;
            T-=r;
          }else{
            a=a+(T*(c+R));
            res+=T;
            res+=1.0*(b-a)/(c+S);
            T=-1;
          }
        }else{
          res+=d;
        }
      }      
      printf("Case #%d: %Lf\n",q,res);
    }
}



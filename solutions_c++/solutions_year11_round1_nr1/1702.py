#include <cstdio>
#include <cmath>
using namespace std;

int T,N,pd,pg;
bool deu;
double ganhei,total;
double p;
int d;

int main(){

  scanf("%d",&T);
  for(int t=0;t<T;t++){
    scanf("%d %d %d",&N,&pd,&pg);
    if(pd==0 and pg==0){
      printf("Case #%d: %s\n",t+1,"Possible");
      continue;
    }
    if(pd>0 and pg==0){
      printf("Case #%d: %s\n",t+1,"Broken");
      continue;
    }

    deu=false;
    for(d=1;d<=N;d++){
      for(int g=0;g<=d;g++){
        if((g*100)%d==0 and pd==(g*100/d)){ //prob exata

//          printf("%d %d\n",d,g);

          ganhei=g;
          total=d;
          p=(ganhei/total)*100;
          while(true){
            if(p>pg){
              total++;
            } else {
              ganhei++;
              total++;
            }
            p=(ganhei/total)*(100);
            if(fabs(p-pg)<1e-3) break;
          }
          if((int)p==pg){
            deu=true;
            break;
          }
        }
      }
    }
    printf("Case #%d: %s\n",t+1,deu?"Possible":"Broken");

/*
    if(deu)
      printf("%d %d %d: d:%d -> %d/%d\n",N,pd,pg,d,(int)ganhei,(int)total);
    else
      printf("%d %d %d\n",N,pd,pg);
*/
  }

  return 0;
}

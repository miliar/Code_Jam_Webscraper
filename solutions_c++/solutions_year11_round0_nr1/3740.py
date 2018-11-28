#include<iostream>
using namespace std;
int t ,n ,seq ,b[100],posO,posB,i;
char bot[100];
int tym ,maxO,maxB;
int dtym, do1,db;
void solve(){
    maxO=0;
    maxB=0;
    tym=0;
    i=0;
    while(n--){
               if(bot[i]=='O'){
                     //        maxO+=b[i]-posO;
                     do1=maxO;
                     dtym=tym;

//((b[i]-posO-maxB)>0)||posO>b[i]?maxO+=((b[i]-posO)>0?b[i]-posO-maxB+1:posO-b[i]-maxB+1):0;
                             maxO+=max(0,abs(b[i]-posO)-maxB)+1;
                             tym+=max(0,abs(b[i]-posO)-maxB)+1;

//((b[i]-posO-maxB)>0)||posO>b[i]?tym+=((b[i]-posO)>0?b[i]-posO-maxB+1:posO-b[i]-maxB+1):tym++;
                       if(do1>maxO) maxO=do1;
                       if(dtym>tym) tym=dtym;
                       //      tym+=b[i]-posO+1;

                             posO=b[i];
                             maxB=0;
   //                          printf("maxo =%d\n",maxO);
               }
               if(bot[i]=='B'){
                               db=maxB;
                               dtym=tym;
                             maxB+=max(0,abs(b[i]-posB)-maxO)+1;
                             tym+=max(0,abs(b[i]-posB)-maxO)+1;

//((b[i]-posB-maxO)>0)||posB>b[i]?maxB+=((b[i]-posB)>0?b[i]-posB-maxO+1:posB-b[i]-maxO+1):0;

//((b[i]-posB-maxO)>0)||posB>b[i]?tym+=((b[i]-posB)>0?b[i]-posB-maxO+1:posB-b[i]-maxO+1):tym++;
                       if(db>maxB) maxB=db;
                       if(dtym>tym) tym=dtym;
                             posB=b[i];
                             maxO=0;
 //                            printf("maxb =%d\n",maxB);
               }
               i++;
//                printf("time=%d \n",tym);
    }
    n=i;
}
void ip(){
    i=0;
    scanf("%d",&n);
//     printf("%d\n",n);
    while(n--){
           scanf(" %c %d",&bot[i],&b[i]);
           i++;
      //     fflush(stdin);
    }
    n=i;
    posO=1;
    posB=1;
    solve();
}
int main(){
   freopen("A-large.in", "r",stdin);
   freopen("A-large.out", "w",stdout);
   scanf("%d",&t);
   int k=0;
   while(k<t){
              ip();
              printf("Case #%d: %d\n",k+1,tym);
              k++;
   }
   return 0;
}

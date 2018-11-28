#include<iostream>
using namespace std;

struct iHour{int h,min,used;};

struct Hour{
    struct iHour t1;
    struct iHour t2;
};

// returns distance between times
int diffTimes(struct iHour ha, struct iHour hb, int T){
    int ta, tb;
    
    ta=(60*ha.h + ha.min);
    tb=(60*hb.h + hb.min);

    return (ta-(tb+T));
}

int main(int argc, char** argv){

    int N,T,NA,NB; // input variables
    struct Hour at[50]; // times on A
    struct Hour bt[50]; // times on B
    int flag,aCount,bCount;
    int curThing,curDiff,temp;

    scanf("%d",&N);

    for(int n=0;n<N;n++){
        
        scanf("%d %d %d",&T,&NA,&NB);
        aCount=0;
        bCount=0;

        for(int na=0;na<NA;na++){
            scanf("%2d:%2d %2d:%2d",&at[na].t1.h,&at[na].t1.min,
                    &at[na].t2.h,&at[na].t2.min);
            at[na].t2.used=0;
        }

        for(int nb=0;nb<NB;nb++){
            scanf("%2d:%2d %2d:%2d",&bt[nb].t1.h,&bt[nb].t1.min,
                    &bt[nb].t2.h,&bt[nb].t2.min);
            bt[nb].t2.used=0;
        }

        for(int na=0;na<NA;na++){
            flag=0;
            
            /* for(int nb=0;nb<NB;nb++){
                if(isOk(at[na].t1,bt[nb].t2,T) && !(bt[nb].t2.used)){
                    flag=1;
                    bt[nb].t2.used=1;
                }
            }*/
            
            curThing=-1;
            curDiff=1000000;
            for(int nb=0;nb<NB;nb++){
                temp=diffTimes(at[na].t1,bt[nb].t2,T);
                if(temp<curDiff && temp>=0 && !(bt[nb].t2.used)){
                    curDiff=temp;
                    curThing=nb;
                }
            }
            if(curThing>=0){
                flag=1;
                bt[curThing].t2.used=1;
            }


            if(!flag) aCount++;
        }
        for(int nb=0;nb<NB;nb++){
            flag=0;
            
            /* for(int na=0;na<NA;na++){
                if(isOk(bt[nb].t1,at[na].t2,T) && !(at[na].t2.used)){
                    flag=1;
                    at[na].t2.used=1;
                }
            }*/

            curThing=-1;
            curDiff=10000000;
            for(int na=0;na<NA;na++){
                temp=diffTimes(bt[nb].t1,at[na].t2,T);
                if(temp<curDiff && temp>=0  && !(at[na].t2.used)){
                    curDiff=temp;
                    curThing=na;
                }
            }
            if(curThing>=0){
                flag=1;
                at[curThing].t2.used=1;
            }

            if(!flag) bCount++;
        }
        printf("Case #%d: %d %d\n",(n+1),aCount,bCount);
    }
    return 0;
}

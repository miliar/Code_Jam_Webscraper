#include <iostream>
#include <stdio.h>
#include <string>

using namespace std;

#define REP(i,n) for(int (i)=0;(i)<(int)(n);++(i))

int heightFromTop(int i){
    int d=0;
    while (i >0){
        i = i >> 1;
        ++d;
    }
    return d;
}

int printar(int ar[], int sz){
    REP(i, sz) printf("%d ", ar[i]);
    printf("\n");
}

int main(){
    int cases=0;
    int casenr=0;
    scanf("%d", &cases);

    while (--cases >=0){
        ++casenr;
        int P;
        scanf("%d", &P);
        int size = 1 << P; // THATS RIGHT MICHAEL! A BITSHIFT!
        int ar[size];
        REP(i,size) scanf("%d", &ar[i]);
        int cost;
        REP(i, (1 << P)-1) //AND ANOTHER ONE! HOLY COW!!
        {
            scanf("%d", &cost);
        }
        int heapish[1 << (P+1)]; //Note: indexed at 1
        REP(i, 1<<(P+1)) heapish[i] = 0;
        
        for (int i=1<<P;i< 1<<(P+1);i++){
            //printf("%d ", ar[i - size]);
            int canmiss = ar[i-size];
            int pos=i;
            bool flag=false;
            while (true){
                if (flag) break;
                if (pos==1) flag=true;
                //printar(heapish, 1<<(P+1));

                //Note: canmiss should eventually == P
                //printf("%d %d\n", heightFromTop(pos), P-canmiss);
                if (heightFromTop(pos) >P-canmiss){
                    //heapish[pos] = 0;
                    pos /=2;
                    continue;
                }
                heapish[pos] = cost;
                pos /=2;
                ++canmiss;
            }
        }
        //printf("finally...");
        //printar(heapish, 1<<(P+1));
        int sum=0;
        REP(i, 1<<(P+1)) {
            //printf("%d %d\n", i, heapish[i]); 
            sum += heapish[i];

        }
        printf("Case #%d: %d\n", casenr, sum);
        //printf("%d %d\n", P, ar[2]);
    }

    return 0;
}

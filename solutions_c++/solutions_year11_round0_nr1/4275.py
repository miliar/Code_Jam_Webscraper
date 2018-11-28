#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cmath>
using namespace std;

#define IN freopen("A-large.in","r",stdin);
#define OUT freopen("A.out","w",stdout);

#define SIZE 110

int O[SIZE],B[SIZE],T,N,ans;
char seq[SIZE];

int main(){
    IN
    OUT
    int i,t,tmp,o,b,posO,posB;
    scanf("%d",&T);
    for(t=1;t<=T;t++){

        scanf("%d",&N);
        o=b=0;
        for(i=0;i<N;i++){
            getchar();
            seq[i] = getchar();
            getchar();
            scanf("%d",&tmp);
            if(seq[i] == 'O')    O[o++] = tmp;
            else   B[b++] = tmp;
            //printf("%c %d\n",seq[i],tmp);
        }

        ans = 0;
        o = b = 0;
        posO = posB = 1;
        int dO,dB;
        for(i=0;i<N;i++){
            dO = abs(O[o]-posO)+1;
            dB = abs(B[b]-posB)+1;
            //printf("%c %d %d\n",seq[i],dO,dB);
            if(seq[i] == 'O'){
                ans += dO;
                posO = O[o++];
                if(dB <= dO)    posB = B[b];
                else    posB = (B[b] > posB)? posB+dO:posB-dO;
            }else{
                ans += dB;
                posB = B[b++];
                if(dO <= dB)    posO = O[o];
                else    posO = (O[o] > posO)? posO+dB:posO-dB;
            }
            //printf("%d %d\n",posO,posB);
        }
        printf("Case #%d: %d\n",t,ans);
    }
    return 0;
}

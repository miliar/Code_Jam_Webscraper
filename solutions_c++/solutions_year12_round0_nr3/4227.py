#include<stdio.h>

int ShiftLeft(int Number,int nShift){
    int i,Moder = 1000000,tmp;
    while(Number/Moder == 0){
        Moder/=10;
    }
    for(i=0; i<nShift; i++){
        tmp = Number/Moder;
        Number = (Number%Moder)*10 + tmp;
    }
    return Number;
}

int main(){
    int nCase,i,j,n,m,A,B,tmp,numberlong,Ans[50];
    scanf("%d",&nCase);
    for(i=0;i<nCase;i++){
        scanf("%d %d",&A,&B);
        tmp = A;
        numberlong = 1;
        while(tmp > 10){
            numberlong++;
            tmp /= 10;
        }
        Ans[i]=0;
        for(n=A; n<B; n++){
            for(m=n+1; m<=B; m++){
                tmp = n;
                for(j=1; j<=numberlong; j++){
                    if(ShiftLeft(n,j)==m){
                        Ans[i]++;
                        j = 1000;
                    }
                }
            }
        }
    }
    for(i=0;i<nCase;i++){
        printf("Case #%d: %d\n",i+1,Ans[i]);
    }
    return 0;
}

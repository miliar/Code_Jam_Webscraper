#include <algorithm>
#include <cstdio>
#include <iostream>
using namespace std;
int main (){
    bool YN,YN_2;
    int T,A,B,s[7],t[7],total,temp,digit,d,i,j,k,m;
    scanf("%d",&T);
    for (i=1;i<=T;i++){
        scanf("%d %d",&A,&B);
        total=0;
        temp=A;
        digit=0;
        while (temp>0){
              temp/=10;
              digit++;
        }
        for (j=A;j<B;j++){
            temp=j;
            d=1;
            while (temp>0){
                  s[digit-d]=temp%10;
                  temp/=10;
                  d++;
            }
            for (k=0;k<digit;k++){
                t[k]=0;
                for (m=0;m<digit;m++){
                    t[k]=t[k]*10+s[(k+m)%digit];
                }
            }
            sort(t,t+digit);
            for (k=1;k<digit;k++){
                if (t[k]!=t[k-1] && j<t[k] && t[k]<=B){
                                 total++;
                }
            }
        }
        printf("Case #%d: %d\n",i,total);
    }
    //system("pause");
    return 0;
}

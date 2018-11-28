#include <cstdio>
#include <iostream>
using namespace std;
int main (){
    int T,N,S,p,t,num,temp,i,j;
    scanf("%d",&T);
    for (i=1;i<=T;i++){
        scanf("%d %d %d",&N,&S,&p);
        num=0;
        temp=0;
        for (j=0;j<N;j++){
            scanf("%d",&t);
            if (t>=3*p-2){
                          num++;
            } else if (t>=3*p-4 && t>0){
                   temp++;
            }
        }
        if (temp<S){
                    num+=temp;
        } else {
               num+=S;
        }
        printf("Case #%d: %d\n",i,num);
    }
    //system("pause");
    return 0;
}

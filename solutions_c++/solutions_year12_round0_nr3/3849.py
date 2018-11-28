#include<stdio.h>
#include<stdlib.h>
#include<string.h>
int use[2000005];
int main (){
    int n,a,b,T,k;
    int tmp,cnt,h,ten,ans,ca=0,i,j;
    scanf("%d",&T);
    while(T--){
        scanf("%d%d",&a,&b);
        ans = 0;
        for(i=a;i<=b;i++){
            tmp = i;
            k = 1;
            while(tmp > 0){
                k *= 10;
                tmp /=10;
            }
            /*ten = 1;
            //printf("i %d\n",i);
            while(ten <= k){
                tmp = i / ten + (i % ten)*(k/ten);
                //printf("tmp %d\n",tmp);
                if(tmp <= b && tmp >= a && i < tmp){
                    printf("(%d %d)\n",i,tmp);
                    //system("pause");
                    ans++;
                }
                ten *= 10;
            }*/
            tmp = i;
            //printf("k = %d\n",k);
            do{
                tmp = (tmp%(k/10))*10 + ((tmp*10) / k);
                //printf("tmp %d\n",tmp);
                //system("pause");
                if(tmp <= b && tmp >= a && i < tmp){
//                    printf("(%d %d)\n",i,tmp);
                    //system("pause");
                    ans++;
                }
            }while(tmp != i);
        }
        ca++;
        printf("Case #%d: %d\n",ca,ans);
    }
    return 0;
}
/*
4
1 9
10 40
100 500
1111 2222
*/

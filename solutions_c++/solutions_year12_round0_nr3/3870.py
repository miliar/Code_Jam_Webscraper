#include<cstdio>
#include<cmath>
#include<cstdio>
#include<cstring>
#define MAX 2000001
using namespace std;
int digits,result,A,B;
int test[MAX]={1};
void func(int num,int depth){
    int lastpart,mod=1,frontpart,newnum;
    while(mod<digits){
        test[num]=0;
        lastpart=num%((int)pow(10,mod));
        frontpart=num/pow(10,mod);
        newnum=lastpart*(pow(10,digits-mod))+frontpart;
        //if((newnum/((int)pow(10,digits-1)))!=0)
          //  printf(" newnum=%d\n",newnum);
        if(newnum>=A && newnum<=B && newnum!=num && test[newnum]==1 && (newnum/((int)pow(10,digits-1)))!=0){
			//printf(" newnum=%d\n",newnum);
            //printf("pair was (%d,%d)\n",num,newnum);
            result+=depth;
            func(newnum,depth+1);
        }
        mod++;
//        getchar();
    }
}
main(){
    int T,temp,level=1;
    scanf("%d",&T);
    while(T--){
        scanf("%d %d",&A,&B);
        for(temp=0;temp<MAX;temp++)
            test[temp]=1;
        temp=A;
        digits=0;
        result=0;
        while(temp!=0){
            temp=temp/10;
            digits++;
        }
        //printf(" digits=%d A=%d B=%d\n",digits,A,B);
        while(A<=B){
            //printf("inside lop A=%d",A);
            if(test[A]==1){
                //printf(" in the while of main A=%d\n",A);
                func(A,1);
            }
            A++;
        }
        printf("Case #%d: %d\n",level,result);
		level++;
    }

}


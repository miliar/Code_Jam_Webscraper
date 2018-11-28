#include<cstdio>
#include<string>

using namespace std;

int main(){
    int T;
    scanf("%d",&T);
    for(int i=0;i<T;i++){
        int A,B;
        scanf("%d%d",&A,&B);
        float p[A],prodp[A+1];
        prodp[0]=1;
        float x=1;
        for(int j=0;j<A;j++){
            scanf("%f",&p[j]);
            x*=p[j];
            prodp[j+1]=prodp[j]*p[j];
            //printf("%f",p[j]);
        }
        float last=B+2,middle[A]; 
        float out=last,index;
        for(int k=0;k<=A;k++){
            middle[k]=-A+2*(B+k+1)-(B+1)*prodp[A-k];
            if(out>middle[k]){
                out=middle[k];
                //index=k;
            }
        }
        printf("Case #%d: %f\n",i+1,out);
    }
}

#include<stdio.h>
#include<stdlib.h>
#include<algorithm>

using namespace std;

int a,b,ans,n,power,N;
double p[10],pr[4],q[10],t[5],w[5]; 

double sum(int a,int b)
{   double ss=1;
    if(a<0) return 1;
    for(int i=a;i<b;i++)
    ss*=pr[i];
    return ss;
}

int main(){
    freopen("output.txt","w",stdout);
    scanf("%d",&N);
    for(int I=1;I<=N;I++)
    {
        scanf("%d %d",&a,&b);
        for(int i=0;i<a;i++)
        scanf("%lf",&pr[i]);
    /*    for(int i=0;i<3;i++)
        q[i]=1-pr[i];
        
        p[2]=pr[0]*q[1]*q[2]; //NYY
        p[5]=pr[1]*q[0]*q[2]; //YNY
        p[6]=pr[2]*q[1]*q[0]; // YYN
        p[1]=pr[0]*pr[1]*q[2]; // NNY
        p[3]=pr[0]*pr[2]*q[1];// NYN
        p[4]=pr[1]*pr[2]*q[0]; // YNN
        p[0]=pr[0]*pr[1]*pr[2]; // NNN
        p[7]=q[0]*q[1]*q[2]; //YYY
        */
        w[0]=sum(0,a);
        w[1]=(1-sum(a-1,a))*sum(0,a-1);
        w[2]=(1-sum(a-2,a-1))*sum(0,a-2);
        w[3]=(1-sum(a-3,a-2))*sum(0,a-3);
        
        
/*        for(int i=0;i<4;i++)
       printf("%lf ",w[i]);*/
       
        t[0]=b+2;
        t[1]=(b-a+3)*(w[0]+w[1])+(b-a+3+b+1)*(w[2]+w[3]);
        t[2]=(b-a+5)*(w[0]+w[1]+w[2])+(b-a+5+b+1)*(w[3]);
        t[3]=(b-a+7)*(w[0]+w[1]+w[2]+w[3]);
        t[4]=(b-a+1)*w[0]+(b-a+1+b+1)*(w[1]+w[2]+w[3]);
 
        sort(t,t+5);
       
   //   for(int i=0;i<5;i++)
  //      printf("%lf ",t[i]);
       
        printf("Case #%d: %.6lf\n",I,t[0]);
        
       
    }
     //  system("pause");    
    return 0;
}

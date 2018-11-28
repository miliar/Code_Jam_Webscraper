#include<iostream>
#include <cstring>
#include<algorithm>
#include<cmath>
#define MAXN 40
using namespace std;
double X[MAXN],Y[MAXN],R[MAXN];
double sqr(double x)
{return x*x;}
double dis(int i,int j)
{ return sqrt(sqr(X[i]-X[j])+sqr(Y[i]-Y[j]));
}
int main()
{
    int T,CASE,i,j,N;
    double x1,x2,x3;
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    scanf("%d",&T);
    
    for(CASE=1;CASE<=T;++CASE)
    {  printf("Case #%d: ",CASE);
    
        scanf("%d",&N);
       for(i=0;i<N;++i)
         scanf("%lf%lf%lf",&X[i],&Y[i],&R[i]);
       if(N==1) printf("%lf\n",R[0]);
       else if(N==2) printf("%lf\n",max(R[0],R[1]));
       else if(N==3) 
       {
           x1=max(R[0],0.5*(R[1]+R[2]+dis(1,2)));
           x2=max(R[1],0.5*(R[2]+R[0]+dis(0,2)));
           x3=max(R[2],0.5*(R[0]+R[1]+dis(0,1)));
          printf("%lf\n",min(x1,min(x2,x3)));  
       }
       
               
       
    
    }
}

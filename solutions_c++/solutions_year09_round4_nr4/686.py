#include <cstdlib>
#include <iostream>
#include <cmath>

using namespace std;
int n,T, Px[41],Py[41],R[41];
int main(int argc, char *argv[])
{
    scanf("%d",&T);
    for(int t=1;t<=T;t++)
    {
    double r1,r2,r3,res;
    scanf("%d",&n);
    for(int i=1;i<=n;i++)
    scanf("%d%d%d",&Px[i], &Py[i], &R[i]);
    if(n==1)res=R[1];
    if(n==2)res=max(R[1],R[2]);
    if(n==3)
    {
    
    r1=sqrt((Px[1]-Px[2])*(Px[1]-Px[2])+(Py[1]-Py[2])*(Py[1]-Py[2]))+R[1]+R[2];
    r2=sqrt((Px[1]-Px[3])*(Px[1]-Px[3])+(Py[1]-Py[3])*(Py[1]-Py[3]))+R[1]+R[3];
    r3=sqrt((Px[2]-Px[3])*(Px[2]-Px[3])+(Py[2]-Py[3])*(Py[2]-Py[3]))+R[2]+R[3];
    r1=max(r1,(double)R[3]);
    r2=max(r2,(double)R[2]);
    r3=max(r3,(double)R[1]);
    res=min(r1,min(r2,r3));
    res=res/2.0;
    }
    
    printf("Case #%d: %f\n",t,res);   
 
}
    
  //  system("PAUSE");
    return 0;
}

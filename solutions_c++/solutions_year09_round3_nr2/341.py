#include<iostream>
#include<fstream>
#include<cmath>
using namespace std;
double getdistance(double A,double B,double C,double X,double Y,double Z,double time,double size)
{
     double ans=0;
     ans=(A+X*time)*(A+X*time);
     ans+=(B+Y*time)*(B+Y*time);
     ans+=(C+Z*time)*(C+Z*time);
     return sqrt(ans)/(double)size;
}
     
using namespace std;
int main()
{
    ifstream input("input.txt");
    double T,A,B,C,X,Y,Z,temp,j,k,l,m,n,o,p,q,r,time,time1,time2;
    int size,i;
    input>>T;
    for(i=0;i<T;i++)
    {
             input>>size;
             A=B=C=X=Y=Z=0;
             for(j=0;j<size;j++)
             {
                           input>>k>>l>>m>>n>>o>>p;
                           A+=k;
                           B+=l;
                           C+=m;
                           X+=n;
                           Y+=o;
                           Z+=p;
             }
             double time_f;
             if((X*X+Y*Y+Z*Z)!=0)
             time_f=-((A*X+B*Y+C*Z)/(X*X+Y*Y+Z*Z));
             else
             time_f=0;
             if(time_f<0)
             time_f=0;
             
               printf("Case #%d: ",(i+1));
               printf("%0.8f ",getdistance(A,B,C,X,Y,Z,time_f,size));
               printf("%0.8f\n",time_f);

    }    
    
    input.close();

    
    return 0;
}

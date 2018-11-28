#include <iostream>
#include <cmath>
using namespace std;
double dis(double x1,double y1,double x2,double y2)
{
	return sqrt((double)(x1-x2)*(x1-x2)+(y1-y2)*(y1-y2));
}
int check(int x1,int y1,int x2,int y2,int x3, int y3)
{
    if(x1==x2&&y1==y2)return 0;
    if(x1==x3&&y1==y3)return 0;
    if(x3==x2&&y3==y2)return 0;
    return 1;
}
int main()
{
   int num;
   cin>>num;
   for(int i=0;i<num;i++)
   {
       double N,M,AA;
       int flag=0;
       cin>>N>>M>>AA;
       cout<<"Case #"<<i+1<<":";
       if(N*M>=AA)
       {
           for(int x1=0;x1<=N;x1++)
           {
               for(int y1=0;y1<=M;y1++)
               {
                   for(int x2=0;x2<=N;x2++)
                   {
                       for(int y2=0;y2<=M;y2++)
                       {
                           for(int x3=0;x3<=N;x3++)
                           {
                               for(int y3=0;y3<=M;y3++)
                               {
                                   if(check(x1,y1,x2,y2,x3,y3)==1)
                                   {
                                    double A=dis(x1,y1,x2,y2);
                                    double B=dis(x1,y1,x3,y3);
                                    double C=dis(x3,y3,x2,y2);
                                    double p=(A+B+C)/2;
                                    double S=sqrt(p*(p - A)*(p - B)*(p - C));
                                    if(abs(S-AA/2)<0.000000001)
                                    {
                                        cout<<" "<<x1<<" "<<y1<<" "<<x2<<" "<<y2<<" "<<x3<<" "<<y3<<endl;
                                        x1=N+1;x2=N+1;x3=N+1;y1=M+1;y2=M+1;y3=M+1;
                                        flag=1;
                                    }
                                   }
                               }
                           }
                       }
                   }
               }
           }
       }
       if(flag==0)cout<<" IMPOSSIBLE"<<endl;
   }
    return 0;
}

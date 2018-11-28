#include<fstream>
#include<iostream>
#include <iomanip>
using namespace std;
int main()
{
    ifstream fin("A-small-attempt1.in");
    ofstream fout("output.txt");
    int a,d,t,i,p=1;
    double ar[5],c[5],b[10],min;
    
    fin>>t;
    while(t--)
    {
              min=10000.0;
              fin>>a>>d;
              for(i=0;i<a;i++)
              fin>>ar[i];
              fout<<"Case #"<<p<<": ";
              p++;
              if(a==3)
              {
                  b[0]=ar[0]*ar[1]*ar[2];
                  b[1]=(1-ar[0])*ar[1]*ar[2];
                  b[2]=ar[0]*(1-ar[1])*ar[2];
                  b[3]=(1-ar[0])*(1-ar[1])*ar[2];
                  b[4]=ar[0]*ar[1]*(1-ar[2]);
                  b[5]=(1-ar[0])*ar[1]*(1-ar[2]);
                  b[6]=ar[0]*(1-ar[1])*(1-ar[2]);
                  b[7]=(1-ar[0])*(1-ar[1])*(1-ar[2]);       
                      
                  //for(i=0;i<=7;i++)
                 // fout<<b[i]<<endl;
                  c[0]=b[0]*(d-a+1)+(b[1]+b[2]+b[3]+b[4]+b[5]+b[6]+b[7])*(2*d+2-a);
                  c[1]=(b[0]+b[4])*(d-a+3)+(b[2]+b[3]+b[1]+b[5]+b[6]+b[7])*(2*d+2-a+2);
                  c[2]=(b[0]+b[4]+b[2]+b[6])*(d-a+5)+(b[3]+b[5]+b[1]+b[7])*(2*d+2-a+4);
                  c[3]=(b[0]+b[1]+b[2]+b[3]+b[4]+b[5]+b[6]+b[7])*(d+1+a);
                  c[4]=(b[0]+b[1]+b[2]+b[3]+b[4]+b[5]+b[6]+b[7])*(d+2);
                  for(i=0;i<=4;i++)
                  {
                     //             fout<<c[i]<<endl;
                                   if(c[i]<min)
                                   min=c[i];
                                   }
                  fout<<min<<setprecision(6)<<fixed<<endl;
                  //fout<<"------"<<endl;
                  }
                 else if(a==2)
                 {
                  b[0]=ar[0]*ar[1];
                  b[1]=(1-ar[0])*ar[1];
                  b[2]=ar[0]*(1-ar[1]);
                  b[3]=(1-ar[0])*(1-ar[1]);    
                  c[0]=b[0]*(d-a+1)+(b[1]+b[2]+b[3])*(2*d+2-a);
                  c[1]=(b[0]+b[2])*(d-a+3)+(b[1]+b[3])*(2*d+2-a+2);
                  c[2]=(b[0]+b[1]+b[2]+b[3])*(d+1+a);
                  c[3]=(b[0]+b[1]+b[2]+b[3])*(d+2);
                  for(i=0;i<=3;i++)
                  {
                   //                fout<<c[i]<<endl;
                                   if(c[i]<min)
                                   min=c[i];
                                   }
                  fout<<setprecision(6)<<fixed<<min<<endl;
                 // fout<<"------"<<endl;
                  }
                  else if(a==1)
                  {
                      b[0]=ar[0];
                      b[1]=(1-ar[0]);
                      c[0]=b[0]*(d-a+1)+b[1]*(2*d+2-a);
                      c[1]=(b[0]+b[1])*(d+1+a);
                      c[2]=(b[0]+b[1])*(d+2);
                      
                       for(i=0;i<=2;i++)
                     {
                       //                 fout<<c[i]<<endl;
                                   if(c[i]<min)
                                   min=c[i];
                                   }
                  fout<<setprecision(6)<<fixed<<min<<endl;
                 // fout<<"------"<<endl;
                  }                     
                   }             
                      
              return 0;
              }
              
              
              

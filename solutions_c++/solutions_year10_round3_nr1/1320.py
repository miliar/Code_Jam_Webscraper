#include<iostream>
#include<fstream>
#include<string.h>


using namespace std;

int main()
{         
         long num;
         long lines;
         long inter;
         
         fstream fin,fout;
         fin.open("input.txt",ios::in);         
         fout.open("output.txt",ios::out);         
         
         fin>>num;         
         
         for(long i=1;i<=num;i++)
         {
                    inter=0;
                    fin>>lines;
                    long y1[lines],y2[lines],m[lines],c[lines];
                    for(long j=0;j<lines;j++)                                                   
                    {
                            fin>>y1[j];fin>>y2[j];     
                            m[j]=y2[j]-y1[j];
                            c[j]=y1[j];   
                    }                    
                    for(long j=0;j<lines;j++)
                    {
                            for(long k=j+1;k<lines;k++)
                            {
                                    if((m[j]-m[k])!=0)
                                    {
                                        double x=-((c[j]-c[k])/double(m[j]-m[k]));
                                        if((x>=0)&&(x<=1))
                                            inter++;                                            
                                    }
                            }
                    }
                    fout<<"Case #"<<i<<": "<<inter<<endl;
         }

         fin.close();
         fout.close();            
         return 0;
}         

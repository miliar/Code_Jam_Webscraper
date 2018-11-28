#include <cstdlib>
#include <iostream>
#include<fstream.h>

using namespace std;

int main()
{
    int test;
    int googlers,surp,p,con_p,con_s,point,max,min,res;
    ifstream infile("C:\\Users\\Flirt-PC\\Desktop\\dance_input.txt");
    ofstream outf("C:\\Users\\Flirt-PC\\Desktop\\dance_out.txt");
    infile>>test;
    for(int i=0;i<test;i++)
    {
           infile>>googlers;
           infile>>surp;
           infile>>p;
           if(p==0)
           {
                   outf<<"Case #"<<i+1<<": "<<googlers<<"\n";
                   for(int j=0;j<googlers;j++)
                   {
                      infile>>point;
                   }
                   
           }
           else
           {
               con_p=0;
               con_s=0;
               max=p+2*(p-1);
               min=p+2*(p-2);
               if(min<2)
               {min=2;}
               for(int j=0;j<googlers;j++)
               {
                      infile>>point;
                      if(point>=max)
                      {con_p++;}
                      else if(point>=min)
                      {con_s++;}
               }
               if(con_s>surp)
               {res=surp;}
               else
               {res=con_s;}
               res=res+con_p;
               outf<<"Case #"<<i+1<<": "<<res<<"\n";
           }
    }
    system("PAUSE");
    return EXIT_SUCCESS;
}

#include<iostream>
#include<fstream>
using namespace std;
int main()
{
    int T,n,s,p,t;
    ifstream fin;fin.open("input.txt");
    ofstream fout;fout.open("output.txt");
    fin>>T;
    int count;
    for(int i=1;i<=T;i++)
    {
            count=0;
            fout<<"Case #"<<i<<": ";
            fin>>n>>s>>p;
            while(n--)
            {
                      fin>>t;
                      if(t>=p)
                      {
                             t-=p;
                             
                             if(t>=2*(p-2))
                             {
                                          if(t==2*(p-2) && s>0){s--;count++;}
                                          else if(t==((2*p)-3) && s>0){s--;count++;}
                                          else if(t==2*(p-1)){count++;}
                                          else if(t==(p+p-1)){count++;}
                                          else if(t==2*p){count++;}
                                          else if(t>2*p){count++;}
                             }
                      }
            }
            fout<<count<<endl;                             
           
    }
    
} 

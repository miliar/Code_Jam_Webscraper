#include<iostream>
#include<fstream>
using namespace std;
ifstream fin;
ofstream fout;
int main()
{
    fin.open("input.txt");
    fout.open("q1output.txt");
    int T,N,S,P;
    fin>>T;
    int df=T;
    while(T--)
    {
       int t[100]={0};
       int count,num=0;
       fin>>N>>S>>P;
       count=S;
       for(int i=0;i<N;i++)
       {
               fin>>t[i];
               
       }
       for(int i=0;i<N;i++)
       {
               if(t[i]>=(3*P)&&t[i]<=30)
               num++;
               else if((t[i]-P)>=0)
               {
               if(P-((t[i]-P)/2)==2)
               {
                    if(count>0)
                    {num++;count--;}
               }
               else if(P-((t[i]-P)/2)==1)
               {
                    
               num++;
              }
              }
       }
      fout<<"Case #"<<(df-T)<<": "<<num<<endl;
    } 

    return 0;
}       

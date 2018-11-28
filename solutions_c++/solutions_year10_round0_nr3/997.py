#include<string>
#include<vector>
#include<iostream>
#include<fstream>
using namespace std;
class node
{
      public:
      long long next;
      long long value;
      long long n;
      node(){next=-1;value=-1;}
};

int main()
{
    ifstream cin("f1.in");
    ofstream cout("f2.out");
    long long i,j,t,k,r,n;
    cin>>t;          
    for(j=1;j<=t;j++)
    {
           cin>>r>>k>>n; 
           vector<long long> g(n);
           for(i=0;i<n;i++)
           {

               cin>>g[i];
           }
           vector<node> mark(n);
           long long times=0;
           long long sum=0;
           mark[0].value=0;
           mark[0].n=1;
           long long begin=0;
           long long num=0;
           long long deltasum=0;
           long long loopbegin=-1;
           long long loopend=-1;
           long long looplength=0;
           while(1)
           {
               long long u1;
               long long temsum=0;long long tembegin;
               num++;
               if(num>r){break;}
               for(u1=begin;u1!=(begin-1+g.size())%(g.size());u1=(u1+1)%(g.size()))
               {
                   if(temsum+g[u1]>k){
                      tembegin=u1;sum+=temsum;break;}
                   temsum+=g[u1];
               }
               if(u1==(begin-1+g.size())%(g.size()))
               {
                   if(temsum+g[u1]>k){tembegin=u1;sum+=temsum;}
                   else{tembegin=begin;sum+=temsum+g[u1];}
               }
               if(mark[tembegin].value==-1)
               {                          
                   mark[begin].next=tembegin;
                   mark[tembegin].value=sum;
                   mark[tembegin].n=mark[begin].n+1;
                   begin=tembegin;
                   continue;
               }
               else
               {
                   loopbegin=tembegin;loopend=begin;
                   deltasum=sum-mark[tembegin].value;
                   mark[begin].next=tembegin;
                   looplength=mark[begin].n+1-mark[tembegin].n;
                   break;
               }
           }
           if(looplength!=0)
           {
              long long u2=loopbegin;
              vector<long long> loop(looplength);
              for(long long tem1=0;tem1<looplength;tem1++)
              {
                  loop[tem1]=mark[u2].value-mark[loopbegin].value;
                  u2=mark[u2].next;
              }
              sum+=(long long)(((r-num)/looplength)*deltasum)+loop[(r-num)%looplength];
           }                        
           cout<<"Case #"<<j<<":"<<" "<<sum<<endl;
    }
}

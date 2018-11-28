#include<iostream>
#include<cstdio>
#include<fstream>
using namespace std;

unsigned long g[1000];
short gp_limit[1000];
long limit_sum[1000];
unsigned long long earning=0;

int main()
{
    unsigned long T;
    unsigned long i,j;
    unsigned long R,k,N;  
    unsigned long x;
    unsigned long sum,t_sum,t;
    
    ifstream fin;
    ofstream fout;
    fin.open("A-small.in");
    fout.open("A.out");
    
    fin>>T;
    for(i=0;i<T;i++)
    {
                    fin>>R>>k>>N;
                    for(j=0;j<N;j++)
                    {
                                    fin>>g[j];
                                    
                    }

                    x=0;
                    t_sum=g[x];
                    while(t_sum<=k )
                    {
                            sum=t_sum;
                            x=(++x)%N;
                            t_sum+=g[x];                
                            
                            if(x==0)
                                    break;
                    }
                    if(x==0)
                    {
                    fout<<"Case #"<<i+1<<": "<<(long)R*(long)sum<<endl;
                    
                    }               
                    else
                    {
                    gp_limit[0]=x-1;
                    limit_sum[0]=sum;
                    //fout<<"0"<<" "<<gp_limit[0]<<" "<<limit_sum[0]<<endl;
                    
                    for(j=1;j<N;j++)
                    {
                                    t=j-1;
                                    x=gp_limit[t];
                                    t_sum=limit_sum[t]-g[t];
                                    
                                    while(t_sum<=k )
                                    {
                                            sum=t_sum;
                                            x=(++x)%N;
                                            t_sum+=g[x];                
                                    }
                                    
                                    if(x!=0)
                                    gp_limit[j]=x-1;
                                    else
                                    gp_limit[j]=N-1;
                                    
                                    limit_sum[j]=sum;        
                                    //fout<<j<<" "<<gp_limit[j]<<" "<<limit_sum[j]<<endl;
                                    
                    }
                   
short                     pos=0;
bool                    break_flag=false;
                    earning=0;
                    for(j=0;j<R;j++)
                    {
                                    //cout<<j<<" "<<pos<<" "<<gp_limit[pos]<<earning<<endl;
                                    if((pos==0) && (j!=0))
                                    {
                                                     break_flag=true;
                                                     break;
                                    }
                                    else
                                    {
                                        earning+=limit_sum[pos];
                                        pos=gp_limit[pos];
                                        pos=(pos+1)%N;
                                    }
                    }
                    if(break_flag==true)
                    {
                                        int rj=R/j;
                                        earning=earning*rj;
                                        R%=j;
                                        for(j=0;j<R;j++)
                                        {
                                             earning+=limit_sum[pos];
                                             pos=gp_limit[pos];
                                             pos=(pos+1)%N;
                                        }
                    }
                    fout<<"Case #"<<i+1<<": "<<earning<<endl;
                    }

    }

    fin.close();
    fout.close();
   cout<<"See A.out";
   cin>>i; 
   return 0;
   
}

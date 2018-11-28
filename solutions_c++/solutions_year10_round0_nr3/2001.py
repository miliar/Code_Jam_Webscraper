#include<iostream>

using namespace std;

int main()
{
    
    long long T,R,K,N;
    long long cindex=0;
    long long currk=0;
    long *arr;
    long *mon;
    short * loc;
    
    cin>>T;
    
    long long init;
    long long ans=0;
    for(int t=1;t<=T;t++)
    {
           cin>>R>>K>>N;
           
            ans=0;
            mon=(long*)malloc(sizeof(long)*N);
            arr=(long*)malloc(sizeof(long)*N);
            loc=(short*)malloc(sizeof(short)*N);
            for(int i=0;i<N;i++)
            cin>>arr[i];
            
            cindex=0;
            init=0;
            for(int i=0;i<N;i++)
            {
                    init=cindex=i;
                    currk=0;
                    while(true)
                    {
                               
                               currk+=arr[cindex];
                               
                               if(currk>K)
                                 { currk-=arr[cindex];break;}
                               else
                               cindex=(++cindex)%N;
                               if(cindex==init)break;
                    }
                    mon[i]=currk;
                    loc[i]=cindex;
                    currk=0;
            }
            
            cindex=0;
            for(int i=0;i<R;i++)
            {
                    ans+=mon[cindex];
                    cindex=loc[cindex];
            }
            
            cout<<"Case #"<<t<<": "<<ans<<endl;
    }
    
   
    return 0;
}
            
                               
                        

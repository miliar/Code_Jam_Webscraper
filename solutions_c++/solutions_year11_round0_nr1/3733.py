#include<iostream>
#include<cstdlib>
using namespace std;

int main()
{
    int t,n,p[101],j,i,time=0,po,pb,to,tb,k1,k2;
    char bot[101];
    cin>>t;
    for(i=1;i<=t;i++)
    {
        cin>>n;
        time=0;
        to=tb=0;
        po=pb=1;
        for(j=1;j<=n;j++) cin>>bot[j]>>p[j];
        for(j=1;j<=n;j++)
        {
            if(bot[j]=='O')
            {
                if (time==0)
                {
                    time=p[j];
                }
                else 
                {   
                k1=abs(p[j]-po);
                k2=time-to;
                if(k1<=k2)
                                {time++;}
                else
                {
                                      time=time+(k1-k2+1);
                }    
                }    
                to=time;
                po=p[j];
                    
            }    
            if(bot[j]=='B')
            {
                if (time==0)
                {
                    time=p[j];
                }
                else 
                {  
                k1=abs(p[j]-pb);
                k2=(time-tb);
                if(k1<=k2)
                                {time++;}
                else
                                time=time+(k1-k2+1);
                }    
                tb=time;
                pb=p[j];
                    
            }    
        }
        cout<<"Case #"<<i<<": "<<time<<endl;    
    }
    return 0;
}    
    

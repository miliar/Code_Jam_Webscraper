#include<iostream>
#include<string>
#include<math.h>

using namespace std;
int main()
{
    int i , j , n , r , t , m , rq , temp ,ii;
    long k;
    int a[1002];
    freopen("F:\\google2010\\C-small-attempt1.in" ,"r" ,stdin);
    freopen("F:\\google2010\\outc.txt","w" ,stdout);  
    
    cin>>t;
    i=0;
    while(t--)
    {   
        i++;
        cin>>r>>k>>n; 
        for(j=0;j<n;j++)cin>>a[j];
        m=0;temp=0;
        for(j=0;j<r;j++)
        {
            rq=k;
            ii=1;
            while(rq-a[temp]>=0&&ii<=n){rq=rq-a[temp];temp=(temp+1)%n;ii++;}
            m=m+k-rq;
        }      

       cout<<"Case #"<<i<<": "<<m<<endl;
       
    }    
        
}     

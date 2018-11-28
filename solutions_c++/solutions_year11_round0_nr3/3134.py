#include<iostream.h>
#include<stdio.h>
#include<fcntl.h>
int main()
{
    long int i,j,k,l,m,n,t,cnt,sum,min,val,tem;
    cin>>t;
    freopen( "candy.txt", "w", stdout );
    for(i=0;i<t;i++)
    {
    cin>>cnt;         
    cin>>val;
    sum=val;
    min=val;   
    cout<<"Case #"<<i+1<<": ";
    for(j=1;j<cnt;j++)    
     {
     cin>>tem;
     val^=tem;
     sum+=tem;
     if(min>tem)
     min=tem;     
     }       
     if(val==0)
     cout<<sum-min;
     else
     cout<<"NO";
     cout<<"\n";              
    }                    
    return(0);
}

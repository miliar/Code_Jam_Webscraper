#include<iostream>

using namespace std;


long long int a,b,temp,t,n,pd,pg,temp1,gcd1;

long long int gcd(long long int x,long long int y)
{
    
    if(y>x)
    {
        temp=x;
        x=y;
        y=temp;
    }
    
    if(((x%y)==0))
        return y;
    
    return (gcd(y,(x%y)));
}



int main()
{
    cin>>t;
    
    for(int q=1;q<=t;q++)
    {
        cin>>n>>pd>>pg;
        
        if((pd==0)&&(pg!=0))
        {
            cout<<"Case #"<<q<<": Broken\n";
            continue;
        }
        
        if((pd!=0)&&(pg==0))
        {
            cout<<"Case #"<<q<<": Broken\n";
            continue;
        }
        
        if((pd==0)&&(pg==0))
        {
            cout<<"Case #"<<q<<": Possible\n";
            continue;
        }
        
        if((pg==100)&&(pd!=100))
        {
            cout<<"Case #"<<q<<": Broken\n";
            continue;
        }  
        
        
        gcd1=gcd(pd,100);
        
        temp1=100/gcd1;
        
        if(temp1>n)
        {
            cout<<"Case #"<<q<<": Broken\n";
            continue;
        }
        
        cout<<"Case #"<<q<<": Possible\n";
        continue;
    }
}
        
        
        
        
        
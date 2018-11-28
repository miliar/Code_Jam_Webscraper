#include <iostream>
#include <vector>
using namespace std;

inline void swap(int &a,int &b)
{
    int t=a;
    a=b;
    b=t;
}
bool f(int x,int y)
{
    bool r=false;
    int a,b;
    a=max(x,y);
    b=min(x,y);
    if(a>=2*b)
        r=true;
    else if(a==b)
        r=false;
    else
    {
        do
        {
            a=a-b;
            swap(a,b);
            if(a>=2*b)
               break;           
            else
                r=!r;     
        }while(1);
    }
    return r;
}
int main(void)
{
    int i,j,k;
    int A1,A2,B1,B2;
    int T;
    int sum;    
            
    cin>>T;
    for(i=1;i<=T;i++)
    {
        cin>>A1>>A2>>B1>>B2;
        sum=0;
        for(j=A1;j<=A2;j++)
           for(k=B1;k<=B2;k++)
              if(f(j,k))
                 sum++;   
                
        
        cout<<"Case #"<<i<<": "<<sum<<endl;            
        
    }
//    system("PAUSE");
    return 0;
}

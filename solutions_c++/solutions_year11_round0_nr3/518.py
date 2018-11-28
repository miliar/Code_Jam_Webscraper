#include<iostream>
#include<algorithm>

using namespace std;

int A[10000],t,n,B[30],p,curr,temp1,sum,flag1;

int main()
{
    cin>>t;
    
    for(int q=1;q<=t;q++)
    {
        cin>>n;
        flag1=1;
        sum=0;
        for(int i=1;i<=n;i++)
        {
            cin>>A[i];
        }
        
        
        for(int i=1;i<=n;i++)
            sum+=A[i];
        
        
        sort(A+1,A+n+1);
        sum-=A[1];
        
        for(int i=1;i<25;i++)
            B[i]=0;
        
        
        for(int i=1;i<=n;i++)
        {
            p=2;
            curr=1;
            
            while(A[i]>0)
            {
                temp1=A[i]%2;
                B[curr]+=temp1;
                A[i]/=p;
               
                curr++;
            }
        }
        
        for(int i=1;i<25;i++)
        {
            if(B[i]%2!=0)
            {
                flag1=0;
                break;
            }
        }
        
        if(flag1==0)
        {
            cout<<"Case #"<<q<<": NO\n";
            continue;;
        }
        
        cout<<"Case #"<<q<<": "<<sum<<"\n";
        
    }
}
        
            
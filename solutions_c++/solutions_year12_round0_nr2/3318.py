#include <iostream>
#include <vector>
using namespace std;
#define rep(i,n) for(i=0;i<n;i++)
int main()
{
    int cases,count,k=0,i,q,r,x;
    cin>>cases;
    while(k<cases)
    {
        int n,s,p;
        count=0;
        cin>>n>>s>>p;
        rep(i,n)
        {
            cin>>x;
            q=x/3;
            r=x%3;

            if(q>=p)count++;
            else if(r>=1&&(q+1)==p)count++;
            else if(r==2&&(q+2)==p&&s>0){s--;count++;}
            else if(r==0&&(q+1)==p&&s>0&&q>0){s--;count++;}
            //cout<<count<<"  "<<s<<endl;
        }
        cout<<"Case #"<<k+1<<": "<<count<<endl;
        k++;
    }
}

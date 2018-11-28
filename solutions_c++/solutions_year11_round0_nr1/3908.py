#include<iostream>
using namespace std;

int main()
{
    long long t,i,n,val[200],cu,o,b,count,cg,k=0;
    char c[200];
    cin>>t;
    while(t--)
    {
              cin>>n;
              for(i=0;i<n;i++){cin>>c[i];cin>>val[i];}
              cu=0;o=1;b=1;count=0;
              while(cu<n)
              {
                         if(c[cu]=='O')
                         {
                         cg=abs(o-val[cu])+1;o=val[cu];
                         count+=cg;
                         for(i=cu+1;i<n;i++)if(c[i]=='B')break;
                         if(i<n)b=val[i]+max(0,int(abs(b-val[i])-cg));
                         }
                         if(c[cu]=='B')
                         {
                         cg=abs(b-val[cu])+1;b=val[cu];
                         count+=cg;
                         for(i=cu+1;i<n;i++)if(c[i]=='O')break;
                         if(i<n)o=val[i]+max(0,int(abs(o-val[i])-cg));
                         }
                         cu++;
                         //cout<<count<<"\n";
                         }
                         k=k+1;
                         cout<<"Case #"<<k<<": "<<count<<"\n";
              }
    return 0;
}

#include<iostream>
#include<queue>
using namespace std;
int main()
{
    int t;
    cin>>t;
    for(int i=0;i<t;++i)
    {
            int r=0,k=0,n=0;
            int euro=0;
            queue<int>g;                         
            cin>>r>>k>>n;                     
            for(int j=0;j<n;++j)  
            {
                    int f=0;
                    cin>>f;
                    g.push(f);              
            }
            for(int m=0;m<r;++m)
            {
                    int s=0,x=0;
                    s=s+g.front();
                    for(int d=0;((s<=k) && (d<g.size()));++d) 
                    {
                                           x=g.front();
                                           g.pop();
                                           g.push(x);
                                           s=s+g.front();
                    }
                    euro+=(s-g.front());
            }
            cout<<"Case #"<<i+1<<": "<<euro<<endl;
    }
}

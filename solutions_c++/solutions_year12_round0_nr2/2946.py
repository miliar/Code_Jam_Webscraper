#include<iostream>
#include<cstdio>
#include<memory.h>
#include<iostream>
using namespace std;
int main()
{
	freopen("B-large.in","r",stdin);
	freopen("out.out","w",stdout);
    int T,S,N,p,t;
    cin>>T;
    for(int i=0;i<T;i++)
    {
        cin>>N>>S>>p;
        int ans=0;
        if(p>=2)
        {
            for(int j=0;j<N;j++)
            {
            cin>>t;
            int max=t/3;
            if(t%3!=0) max++;
            if(max>=p){ans++;continue;}
            else
            if((S>0)&&(max==p-1)&&(t%3==0||t%3==2)) {ans++;S--;}
            }
        }
        else
        {
            for(int j=0;j<N;j++)
            {
            cin>>t;
            int max=t/3;
            if(t%3!=0) max++;
            if(max>=p){ans++;continue;}
            }
        }
        cout<<"Case #"<<i+1<<": "<<ans<<endl;
    }
	return 0;
}



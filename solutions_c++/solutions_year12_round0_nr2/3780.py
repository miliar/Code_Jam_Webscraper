#include<cstdio>
#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;
int T,N,S,p,score,res;
int main()
{
    freopen("B-large.in","r",stdin);
    freopen("B.out","w",stdout);
    cin>>T;
    for(int i=1;i<=T;i++)
    {
        res=0;
        cin>>N>>S>>p;
        for(int j=0;j<N;j++)
        {
            cin>>score;
            if(score>3*(p-1)) res++;
            if((score==3*p-3 || score==3*p-4) && S>0 && score>=p)
            {
                S--;
                res++;
            }
        }
        cout<<"Case #"<<i<<": "<<res<<endl;
    }
}

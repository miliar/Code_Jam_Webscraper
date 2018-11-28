#include<map>
#include<set>
#include<cmath>
#include<vector>
#include<cstdio>
#include<string>
#include<cstring>
#include<iostream>
#include<algorithm>
using namespace std;

int T,N,S,P,t[110];

int main()
{
    //freopen("B-large.in","r",stdin);
    //freopen("B-large.out","w",stdout);
    cin>>T;
    for(int ca=1;ca<=T;ca++)
    {
        cin>>N>>S>>P;
        int ans=0;
        for(int i=1;i<=N;i++) cin>>t[i];
        for(int i=1;i<=N;i++)
        {
            if(t[i]>=28) ans++;
            else
            {
                if(t[i]==0)
                {
                    if(P==0) ans++;
                    continue;
                }
                if(t[i]==1)
                {
                    if(P<=1) ans++;
                    continue;
                }
                int tmp=t[i]/3;
                if((t[i]%3)!=0) tmp++;
                if(tmp>=P) ans++;
                else
                {
                    if(S>0)
                    {
                        if((t[i]%3)!=1)
                        {
                            if((tmp+1)>=P)
                            {
                                S--;
                                ans++;
                            }
                        }
                    }
                }
            }
        }
        cout<<"Case #"<<ca<<": "<<ans<<endl;
    }
    return 0;
}











#include <iostream>
#include <stdio.h>
#include <algorithm>

using namespace std;



#define MAXM 10001


short node[MAXM][2];
bool v;
    int M,V;


bool done(int x,int idx)
{
    if(node[x+idx][1]==2)
        return node[x+idx][0]==1?true:false;
    else
    {
        bool a,b;
        a=done(x*2,idx*2);
        b=done(x*2,idx*2+1);
        if(node[x+idx][0]==0)
            return a||b;
        else
            return a&&b;
    }
}

int fun(int cnt)
{
    int tp;
    int idx=1;
    int ans = cnt;

    if(cnt==0)
        return 99999;
    if(v==done(1,0))
        return 0;


        for(;idx<=(M-1)/2;idx++)
        {
            if(node[idx][1]==1)
            {
                node[idx][1] = 0;
                node[idx][0] = 1-node[idx][0];
                tp = fun(cnt-1) + 1;   
                if(tp<ans)
                    ans = tp;
                node[idx][1] = 1;
                node[idx][0] = 1-node[idx][0];
            }
        }

    return ans;
}

int main()
{
    int N;

    
    cin>>N;
    
    int idx;
    int ans;
    for(int i=1;i<=N;i++)
    {   
        cin>>M>>V;
        v= V==1?true:false;
        memset(node,0,sizeof(node));
        
        for(idx=1;idx<=(M-1)/2;idx++)
        {
            cin>>node[idx][0]>>node[idx][1];
        }
        for(;idx<=M;idx++)
        {
            cin>>node[idx][0];
            node[idx][1] = 2;
        }
        ans = fun(99999);
        if(ans>=0 && ans<= 10001)
            cout<<"Case #"<<i<<": "<<ans<<endl;
        else
            cout<<"Case #"<<i<<": IMPOSSIBLE"<<endl;


    }
    return 0;
}

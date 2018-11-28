//prob1
#include<iostream>
#include<string>
#include<vector>
#include<set>
#include<map>
#include<stack>
#include<queue>
#include<cmath>
#include<algorithm>
#include<sstream>
#define vi vector<int>
#define vvi vector<vector<int> >
#define pii pair<int,int> 
#define vs vector<string> 
#define MAXN 1000000000000000LL
using namespace std;
long long dp[10110][3];
int isleaf[10110];
int type[10110];
int ischange[10110];
int vals[10110];
int m;
int v;
long long solve(int node,int value)
{
    //cout<<"tes "<<node<<" "<<value<<endl;
    if(isleaf[node])
    {
        if(value==vals[node])return 0;
        else
        return MAXN;
    }
    long long &ret=dp[node][value];
    if(ret!=-1)return ret;
    ret=MAXN;
    if(isleaf[node])
    {
        if(value==vals[node])return 0;
        else
        return MAXN;
    }
    if(!ischange[node])
    {
        if(type[node]==1)
        {
            if(value==1)
            {
                ret=min(ret,solve(node*2+1,1)+solve(node*2+2,1));
            }
            else
            {
                ret=min(ret,solve(node*2+1,1)+solve(node*2+2,0));
                ret=min(ret,solve(node*2+1,0)+solve(node*2+2,1));
                ret=min(ret,solve(node*2+1,0)+solve(node*2+2,0));
            }
        }
        else
        {
            if(value==1)
            {
                ret=min(ret,solve(node*2+1,1)+solve(node*2+2,0));
                ret=min(ret,solve(node*2+1,0)+solve(node*2+2,1));
                ret=min(ret,solve(node*2+1,1)+solve(node*2+2,1));
            }
            else
            {
                ret=min(ret,solve(node*2+1,0)+solve(node*2+2,0));
            }
        }
    }
    else
    {
        if(type[node]==1)
        {
            if(value==1)
            {
                ret=min(ret,solve(node*2+1,1)+solve(node*2+2,1));
                ret=min(ret,solve(node*2+1,1)+solve(node*2+2,0)+1);
                ret=min(ret,solve(node*2+1,0)+solve(node*2+2,1)+1);
                ret=min(ret,solve(node*2+1,1)+solve(node*2+2,1)+1);
            }
            else
            {
                ret=min(ret,solve(node*2+1,0)+solve(node*2+2,0)+1);
                ret=min(ret,solve(node*2+1,1)+solve(node*2+2,0));
                ret=min(ret,solve(node*2+1,0)+solve(node*2+2,1));
                ret=min(ret,solve(node*2+1,0)+solve(node*2+2,0));
            }
        }
        else
        {
            if(value==1)
            {
                ret=min(ret,solve(node*2+1,1)+solve(node*2+2,1)+1);
                ret=min(ret,solve(node*2+1,1)+solve(node*2+2,0));
                ret=min(ret,solve(node*2+1,0)+solve(node*2+2,1));
                ret=min(ret,solve(node*2+1,1)+solve(node*2+2,1));
            }
            else
            {
                ret=min(ret,solve(node*2+1,0)+solve(node*2+2,0));
                ret=min(ret,solve(node*2+1,1)+solve(node*2+2,0)+1);
                ret=min(ret,solve(node*2+1,0)+solve(node*2+2,1)+1);
                ret=min(ret,solve(node*2+1,0)+solve(node*2+2,0)+1);
            }
        }
    }
    return ret;
}
    
int main()
{
    int tes;
    cin>>tes;
    int count=1;
    while(tes--)
    {
        memset(dp,-1,sizeof(dp));
        memset(isleaf,0,sizeof(isleaf));
        memset(type,0,sizeof(type));
        memset(ischange,0,sizeof(ischange));
        memset(vals,0,sizeof(vals));
        cin>>m>>v;
        int i,j,k;
        for(i=0;i<(m-1)/2;i++)
        {
            cin>>type[i]>>ischange[i];
            isleaf[i]=0;
        }
        for(i=(m-1)/2;i<m;i++)
        {
            cin>>vals[i];
            isleaf[i]=1;
        }
        /*for(i=0;i<m;i++)
        {
            cout<<isleaf[i]<<" "<<ischange[i]<<" "<<type[i]<<" "<<vals[i]<<endl;
        }*/
        long long val=solve(0,v);
        if(val>=MAXN)
        cout<<"Case #"<<count<<": IMPOSSIBLE"<<endl;
        else
        cout<<"Case #"<<count<<": "<<val<<endl;
        count++;
    }
    return 0;
}
        

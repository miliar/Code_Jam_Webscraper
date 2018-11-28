//Prob3
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
#define pb push_back
using namespace std;
int r,c;
int d[101][101];
long long dp[11][1<<10];
long long solve(int row,int prevmask)
{
    if(row==r)return 0;
    long long &ret=dp[row][prevmask];
    if(ret!=-1)return ret;
    
    ret=0;
    int i,j,k;
    
    for(i=0;i<(1<<c);i++)
    {
        int t=0x3;
        int flag=0;
        for(j=0;j<c;j++)
        {
            if((i&(t<<j))==(t<<j))
            {
                flag=1;
                break;
            }
        }
        int p=prevmask<<1;
        int q=prevmask>>1;
        if(p&i || q&i)flag=1;
        for(j=0;j<c;j++)
        {
            if(!(i&(1<<j)))continue;
            if(d[row][j])
            {
                flag=1;
                break;
            }
        }
        if(flag==1)continue;
        ret=max(ret,solve(row+1,i)+__builtin_popcount(i));
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
        cin>>r>>c;
        memset(dp,-1,sizeof(dp));
        memset(d,0,sizeof(d));
        int i,j,k;
        for(i=0;i<r;i++)
        {
            string s;
            cin>>s;
            for(j=0;j<s.size();j++)
            {
                if(s[j]=='.')d[i][j]=0;
                else d[i][j]=1;
            }
        }
        long long val=solve(0,0);
        cout<<"Case #"<<count<<": "<<val<<endl;
        count++;
    }
    return 0;
}

//Prob4
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
#define MOD 10007
using namespace std;

long long dp[201][201];
int rocks[201][201];
int h,w,r;
int x[]={2,1};
int y[]={1,2};
long long solve(int row,int col)
{
    if(row>h || col>w)return 0;
    if(row==h && col==w)return 1;
    long long &ret=dp[row][col];
    if(ret!=-1)return ret;
    
    if(rocks[row][col]==1)return 0;
    
    ret=0;
    ret+=solve(row+2,col+1)%MOD;
    ret+=solve(row+1,col+2)%MOD;
    
    return ret;
}
int main()
{
    int tes;
    cin>>tes;
    int count=1;
    while(tes--)
    {
        cin>>h>>w>>r;
        memset(dp,-1,sizeof(dp));
        memset(rocks,0,sizeof(rocks));
        int i,j,k;
        for(i=0;i<r;i++)
        {
            cin>>j>>k;
            rocks[j][k]=1;
        }
        long long val=solve(1,1)%MOD;
        cout<<"Case #"<<count<<": "<<val<<endl;
        count++;
    }
    return 0;
}

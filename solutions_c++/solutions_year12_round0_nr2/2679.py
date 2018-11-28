//Bismillahir Rahmanir Rahim
#include <iostream>
#include <cstdio>
#include <algorithm>
#include <string>
#include <cstring>
#include <vector>
#include <stack>
#include <queue>
#include <deque>
#include <bitset>
#include <utility>
#include <set>
#include <map>
#include <cmath>

using namespace std;

#define pi 2.0*acos(0.0)
#define pb push_back
#define MAX 2147483647
#define MIN -2147483647
#define rep(i,n) for(int i(0),_n(n);i<_n;i++)
#define reps(i,s,n) for(int i(s),_n(n);i<_n;i++)
#define mp make_pair


typedef long long ll;
typedef vector<int> VI;
typedef set<int>SI;
typedef pair<int,int>PAR;
typedef vector<PAR>VP;
typedef map<string,int>MSI;

int N,S,P,p[109],memo[109][109];

void ini()
{
    rep(i,109)
    {
        rep(j,109)
        memo[i][j]=-1;
    }
}

int dp(int cur,int s,int bar)
{
    if(cur==N){
        if(s==S){
            return bar;
        }
        return MIN;
    }

    if(memo[cur][s]!=-1){
        //cout<<memo[cur][s]<<endl;
        return memo[cur][s];
    }

    int ret=0;

    for(int i=0;i<=p[cur];i++){
        for(int j=0;j<=p[cur];j++)
            for(int k=0;k<=p[cur];k++){

                if(i+j+k==p[cur]&&i<11&&j<11&&k<11&&i>=0&&j>=0&&k>=0){
                if(max(i,max(j,k))-min(i,min(j,k))<=2){
                if(fabs(i-j)==2||fabs(i-k)==2||fabs(j-k)==2){
                    {
                        int x = dp(cur+1,s+1,bar+(max(i,max(j,k))>=P));
                        ret=max(ret,x);
                    }
                }
                else{
                    int x = dp(cur+1,s,bar+(max(i,max(j,k))>=P));
                    ret=max(ret,x);
                }
                }
                }
            }
    }

    return memo[cur][s]=ret;
}



int main()
{
#ifndef ONLINE_JUDGE
   freopen("B_small.txt", "rt", stdin);
   freopen("output.txt", "wt", stdout);
#endif
    int kas;
    scanf("%d",&kas);
    rep(cas,kas){
        scanf("%d%d%d",&N,&S,&P);
        rep(i,N)cin>>p[i];
        ini();
        int ret = dp(0,0,0);
        printf("Case #%d: %d\n",cas+1,ret);
    }

return 0;
}

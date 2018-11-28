#include <map>
#include <deque>
#include <queue>
#include <stack>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <algorithm>
#include <vector>
#include <set>
#include <complex>
using namespace std;
const int MX=1000;
long long res=0;
long long dp[MX];
long long n;
long long v[MX];
int md=1000000007;
long long calc(int ind)
{
    dp[ind]=1;
    for(int i=ind+1;i<n;i++)
    {
        if(v[i]>v[ind])
        {
            if(dp[i]!=-1)
            {
                dp[ind]+=dp[i];
                dp[ind]%=md;
            }
            else
            {
                dp[ind]+=calc(i);
                dp[ind]%=md;
            }
        }
    }
    return dp[ind];
}
int main()
{
    freopen("a.txt","rt",stdin);
    freopen("b.txt","wt",stdout);
    int N;
    cin>>N;
    long long m,X,Y,Z;
    long long A[MX];
    for(int nn=0;nn<N;nn++)
    {
        cin>>n>>m>>X>>Y>>Z;
        for(int i=0;i<m;i++)
            cin>>A[i];
        int cur=0;
        for(int i=0;i<n;i++)
        {
            v[cur++]=A[i%m];
            A[i%m] = (X * A[i%m] + Y * (i + 1))%Z;
        }
        long long res=0;
        memset(dp,-1,sizeof(dp));
        for(int i=0;i<n;i++)
        {
            res+=calc(i);
            res%=md;
        }
        cout<<"Case #"<<nn+1<<": "<<res<<endl;
    }
    return 0;
}

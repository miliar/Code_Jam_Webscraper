#include<iostream>
using namespace std;

int p , n;
long long dp[2049][12];
long long most[2049];
long long cost[2049];
long long INF = 1000000000000LL;

long long dodp(int cur , int minu)
{
    if(cur >= n)
    {
        if(minu > most[cur])
        {
            //cout<<cur<<" "<<minu<<" : "<<INF<<"(cost = "<<cost[cur]<<")"<<endl;
            return INF;
        }
        {
            //cout<<cur<<" "<<minu<<" : "<<0<<"(cost = "<<cost[cur]<<")"<<endl;
        return 0;
        }
    }
    else
    {
        if(dp[cur][minu] >= 0)
            return dp[cur][minu];
        dp[cur][minu] = INF;
        dp[cur][minu] = min(dp[cur][minu] , cost[cur] + dodp(2 * cur , minu) + dodp(2 * cur + 1 , minu));
        dp[cur][minu] = min(dp[cur][minu] , dodp(2 * cur , minu + 1) + dodp(2 * cur + 1 , minu + 1));
        //cout<<cur<<" "<<minu<<" : "<<dp[cur][minu]<<endl;
        return dp[cur][minu];
    }
}

int main()
{
    int T;
    cin>>T;
    for(int caseID = 1 ; caseID <= T ; caseID ++)
    {
        cin>>p;
        memset(dp , 0xff , sizeof(dp));
        n = (1<<p);
        for(int i = 0 ; i < n ; i ++)
            cin>>most[n+i];
        for(int i = p - 1 ; i >= 0 ; i --)
        {
            int L = (1<<i);
            int R = 2 * L - 1;
            for(int j = L ; j <= R ; j ++)
                cin>>cost[j];
        }
        cout<<"Case #"<<caseID<<": "<<dodp(1 , 0)<<endl;
    }
    return 0;
}

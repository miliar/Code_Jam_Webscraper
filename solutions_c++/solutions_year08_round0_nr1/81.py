#include<iostream>
#include<map>
#include<algorithm>
#define oo 1013741823
using namespace std;
map<string,int> Map;
int n,m,Min;
int a[1000],dp[1000][100];
int main()
{
    int _,t,i,j;
    string s;
    cin>>t;
    for(_=1; _<=t; _++)
    {
        cin>>n;getline(cin,s);
        Map.clear();
        for(i=0; i<n; i++)
        {
            getline(cin,s);
            Map[s]=i;
        }
        cin>>m;getline(cin,s);
        for(j=0; j<m; j++)
        {
            getline(cin,s);
            a[j]=Map[s];
        }
        for(i=0; i<n; i++)
        dp[0][i]=(i==a[0]?oo:0);
        Min=0;
        for(j=1; j<m; j++)
        {
            for(i=0; i<n; i++)
            if(i!=a[j])
            dp[j][i]=min(Min+1,dp[j-1][i]);
            else
            dp[j][i]=oo;
            Min=oo;
            for(i=0; i<n; i++)
            Min=min(Min,dp[j][i]);
        }
        printf("Case #%d: %d\n",_,Min);
    }
    return 0;
}

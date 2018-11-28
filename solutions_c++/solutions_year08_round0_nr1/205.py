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
#define pb push_back
#define all(v) v.begin(),v.end()
#define sz size()
#define rep(i,m) for(int i=0;i<m;i++)
#define mem(a,b) memset(a,b,sizeof(a))
#define mp make_pair
typedef pair<int,int> pii;
typedef vector<pii> vpii;
typedef vector<string> vs;
typedef vector<int> vi;
typedef vector<vector<int> > vii;
typedef long long ll;
int oo=0x7FFFFFFF;
int s,q;
string qs[1000],ss[100];
int dp[1000][100];
int calc(int ind,int cur)
{
    if(ind==q)
        return 0;
    if(cur!=-1 && dp[ind][cur]!=-1)
        return dp[ind][cur];
    int mn=int(0xFFFFFF);
    if(cur==-1 || qs[ind]==ss[cur])
    {
        for(int i=0;i<s;i++)
            if(ss[i]!=qs[ind])
            {
                int temp;
                temp=calc(ind+1,i);
                if(cur!=-1)
                    temp++;
                mn=min(mn,temp);
            }
    }
    else
        mn=min(mn,calc(ind+1,cur));
    return dp[ind][cur]=mn;
}
int main()
{
    freopen("A-large.in","rt",stdin);
    freopen("b.txt","wt",stdout);
    int N;
    cin>>N;
    rep(i,N)
    {
        cin>>s;
        getline(cin,ss[0]);
        rep(j,s)
            getline(cin,ss[j]);
        cin>>q;
        getline(cin,qs[0]);
        rep(j,q)
            getline(cin,qs[j]);
        memset(dp,-1,sizeof(dp));
        cout<<"Case #"<<i+1<<": "<<calc(0,-1)<<endl;
    }
    return 0;
}

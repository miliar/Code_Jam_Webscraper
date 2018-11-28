#include<iostream>
#include<vector>
#include<string>
#include<map>
#include<algorithm>
using namespace std;

vector<string> eng;
vector<string> q;
int dp[1020][200];
int minSwitches(int ind, int cur)
{
    if(ind == q.size())return 0;
    if(dp[ind][cur]!=-1) return dp[ind][cur];
    int r = 5000;
    if(eng[cur] == q[ind])
    {
        for(int i = 0 ; i < eng.size() ; i ++)
        {
            if(i!=cur)
            r = min(r,minSwitches(ind+1,i)+1);
        }
    }
    else
    r = min(r,minSwitches(ind+1,cur));
    return dp[ind][cur] = r;     
}
int main()
{
    freopen("A-large.in","rt",stdin);
    freopen("A-large.out","wt",stdout);
    int t;
    cin>>t;
    string temp;
    int ng,nq;
    for(int i = 0 ; i < t; i ++)
    {
        memset(dp,-1,sizeof(dp));
        cin>>ng;
        getline(cin,temp);
        eng.resize(ng);
        for(int j = 0 ; j < ng ; j++)
        {
            getline(cin,eng[j]);
        }
        
        cin>>nq;
        getline(cin,temp);
        q.resize(nq);
        for(int j = 0 ; j < nq ; j++)
        {
            getline(cin,q[j]);
        }
        int sol = 5000;
        for(int j = 0 ; j < ng; j ++)
        {
            sol = min(sol,minSwitches(0,j));
        }
        cout<<"Case #"<<i+1<<": "<<sol<<endl;
    }
    
    //system("pause");
    return 0;
}

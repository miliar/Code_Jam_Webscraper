#include<iostream>
#include<string>
#include<vector>
#include<sstream>
#include<cmath>
#include<algorithm>
#include<numeric>
#include<map>
#include<set>
#include<queue>
using namespace std ;
string busca="welcome to code jam";
string s;
int memo[502][22];
int dp(int pos,int i)
{
    if(i==busca.size())return 1;
    if(pos>=s.size() || i>=busca.size())return 0;
    if(memo[pos][i]!=-1)return memo[pos][i];
    int dev=0;
    if(s[pos]==busca[i])dev=(dp(pos+1,i+1)+dp(pos+1,i))%10000;
        else dev=dp(pos+1,i)%10000;
    
    memo[pos][i]=dev;
    return dev;
}
int main()
{
    //freopen("in.txt","r",stdin);
    //freopen("out.txt","w",stdout);
    int t;
    cin>>t;
    getline(cin,s);
    for(int ana=0;ana<t;ana++)
    {
        getline(cin,s);
        memset(memo,-1,sizeof(memo));
        int k=dp(0,0)%10000;
        stringstream st;
        st<<k;
        string aux=st.str();
        aux=string(4-aux.size(),'0')+aux;
        cout<<"Case #"<<ana+1<<": "<<aux<<endl;
    }
    //system("pause");
    return 0;
}



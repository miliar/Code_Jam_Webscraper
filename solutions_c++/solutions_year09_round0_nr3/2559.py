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
int dp[509][509];
string wel="welcome to code jam";
string str="";
int go(int i,int j)
{
    if(i>=wel.size())return 1;
    if(j>=str.size())return 0;
    if(dp[i][j])return dp[i][j];
    int b=go(i,j+1);
    int a=0;
    if(wel[i]==str[j]) a+=go(i+1,j);
    
    return dp[i][j]=a+b;
}

int main()
{
    #ifndef ONLINE_JUDGE
	freopen("a.txt", "rt", stdin);
    freopen("b.txt", "wt", stdout);
    #endif

    string tmp;
    int n;cin>>n;
    getline(cin,tmp);
    int cnt=1;
    while (n--)
    {
          memset(dp,0,sizeof(dp));
          getline(cin,str);
          long long res=go(0,0)%10000;
          stringstream ss;
          ss<<res;string ret="";ss>>ret;
          string rett="";
          for(int i=0;i<4-ret.size();i++)
          rett+="0";
          rett+=ret;
          cout<<"Case #"<<cnt++<<": "<<rett<<endl;
    }
    return 0;
}

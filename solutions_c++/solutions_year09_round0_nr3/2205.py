#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <queue>
#include <fstream>
using namespace std;
int dp[550][550],l1,l2,i,j;
const string s1="welcome to code jam";
string s2;
int count(int i,int j)
{
    
    if(j==s1.size())return 1;
    if(i==s2.size())return 0;
    if(dp[i][j]!=-1)return dp[i][j];
    int cnt=0;
    cnt+=count(i+1,j);
    if(s1[j]==s2[i])
    cnt+=count(i+1,j+1);

  	return dp[i][j]=cnt%10000;
}

int main()
{
    
    int cp=0,jj=0,ans;
    cin>>cp;
    getline(cin,s2);
    while(cp--)
    {jj++;
               cout<<"Case #"<<(jj)<<": ";
    getline(cin,s2);
    for(i=0;i<550;i++)
    for(j=0;j<550;j++)dp[i][j]=-1;
    ans=count(0,0);    
    
    cout<<ans/1000<<(ans/100)%10<<(ans/10)%10<<ans%10<<endl;

    
    }
   
   return 0;
    
}

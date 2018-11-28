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
using namespace std;
long long s2i(string s){stringstream ss;long long n;ss<<s;ss>>n;return n;}
string i2s(long long n){stringstream ss;ss<<n;return ss.str();}
//int dp[45][5][7][11][15][5][7][11][15];
int test;
string s;
vector<int> v;
char a[30];
long long res;
void calc()
{
       //cout<<a<<endl;
       int x=0;
       long long sum=0,k=0;
       bool add=1;
       while(a[x]!='.')
       {
               while(a[x]!='.' && a[x]!='+' && a[x]!='-')
               {
                       k=k*10+(a[x]-'0');
                       x++;
               }
               if(add) sum+=k; else sum-=k;
               if(a[x]=='-') add=0; else add=1;
               if(a[x]=='.') break;
               x++;
               k=0;                
       }
       //cout<<sum<<endl;
       if(sum%2==0 || sum%3==0 || sum%5==0 || sum%7==0) res++;
}
void solve(int pos,int x)
{
       //cout<<pos<<" "<<x<<endl;
       if(pos==v.size()){
               a[x]='.';
               calc();
               return;
       }
       if(a[x-1]!='-' && a[x-1]!='+')
       {
               a[x]='+';
               solve(pos,x+1);
               a[x]='-';
               solve(pos,x+1);
       }
       a[x]=s[pos];
       solve(pos+1,x+1);
}        

int main()
{
       cin>>test;
       for(int i1=1;i1<=test;++i1)
       {
               v.clear();
               //memset(dp,-1,sizeof(dp));
               cin>>s;
               for(int i=0;i<s.size();i++) v.push_back(s[i]-'0');
               printf("Case #%i: ",i1);
               //cout<<solve(1,a%2,a%3,a%5,a%7,0,0,0,0,0)<<"\n";
               a[0]=s[0];
               res=0;
               solve(1,1);
               cout<<res<<endl;
       }
}
 

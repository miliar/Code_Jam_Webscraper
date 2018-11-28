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
long long cnt;
string s;
int n;
/*void calc(int ind,long long sum,long long ti)
{
    if(ind==n)
    {
        cout<<sum<<" "<<ti<<endl;
        if(sum%2==0 || sum%3==0 || sum%5==0 || sum%7==0)
            cnt++;
        return;
    }
    int nsum=sum+ti;
    calc(ind+1,nsum,s[ind]-'0');
    nsum=sum-ti;
    calc(ind+1,nsum,s[ind]-'0');
    int nti=ti;
    nti*=10;
    nti+=int(s[ind]-'0');
    calc(ind+1,sum,nti);
}*/
long long val(const string &s)
{
    long long res=0;
    long long sum=0;
    for(int i=0;i<s.size();i++)
        if(s[i]=='-')
        {
            res-=sum;
            sum=0;
        }
        else if(s[i]=='+')
        {
            res+=sum;
            sum=0;
        }
        else
        {
            sum*=10;
            sum+=s[i]-'0';
        }
    return res+sum;
}
void calc(int ind,string st)
{
    if(ind==n)
    {
        long long sum=val(st);
        if(sum%2==0 || sum%3==0 || sum%5==0 || sum%7==0)
            cnt++;
        return;
    }
    calc(ind+1,st+"+"+s[ind]);
    calc(ind+1,st+"-"+s[ind]);
    calc(ind+1,st+s[ind]);
}
int main()
{
    freopen("a.txt","rt",stdin);
    freopen("b.txt","wt",stdout);
    int N;
    cin>>N;
    for(int nn=0;nn<N;nn++)
    {
        cin>>s;
        n=s.size();
        cnt=0;
        calc(1,s.substr(0,1));
        cout<<"Case #"<<nn+1<<": "<<cnt<<endl;
    }
    return 0;
}

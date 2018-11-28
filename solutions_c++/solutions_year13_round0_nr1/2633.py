//Author: master_pk
#include<cstdio>
#include<vector>
#include<cmath>
#include<string>
#include<cstring>
#include<algorithm>
#include<queue>
#include<set>
#include<stack>
#include<map>
#include<sstream>
#include<bitset>
#include<deque>
#include<utility>
#include<cstdlib>
#include<iomanip>
#include<cctype>
#include<climits>
#include<iostream>
using namespace std;
#define ll             long long
#define ull            unsigned long long
string tostr(long long x) { stringstream ss; ss << x; return ss.str(); }
long long toint(const string &s) { stringstream ss; ss << s; long long x; ss >> x; return x; }

int main()
{
freopen("A-large.in","r",stdin);
freopen("output.txt","w",stdout);
int test;
cin>>test;
int i,j,k;
for(i=1;i<=test;i++)
{
    vector<string> s;
    s.clear();
    for(j=0;j<4;j++)
    {
        string s1;
        cin>>s1;
        s.push_back(s1);
    }
    int f1=0,f2=0,d=0;
    for(j=0;j<4;j++)
    for(k=0;k<4;k++)
    if(s[j][k]!='.')
    d++;
    for(j=0;j<4;j++)
    {
        int cnt1=0,cnt2=0;
        for(k=0;k<4;k++)
        {
            if(s[j][k]=='T'||s[j][k]=='O')
            cnt1++;
            if(s[j][k]=='T'||s[j][k]=='X')
            cnt2++;
        }
        if(cnt1==4)
        {
            f1=1;
            break;
        }
        if(cnt2==4)
        {
            f2=1;
            break;
        }
    }
    for(k=0;k<4;k++)
    {
        int cnt1=0,cnt2=0;
        for(j=0;j<4;j++)
        {
            if(s[j][k]=='T'||s[j][k]=='O')
            cnt1++;
            if(s[j][k]=='T'||s[j][k]=='X')
            cnt2++;
        }
        if(cnt1==4)
        {
            f1=1;
            break;
        }
        if(cnt2==4)
        {
            f2=1;
            break;
        }
    }
    int cnt1=0,cnt2=0;
    for(j=0;j<4;j++)
    {

        if(s[j][j]=='T'||s[j][j]=='O')
        cnt1++;
        if(s[j][j]=='T'||s[j][j]=='X')
        cnt2++;
        if(cnt1==4)
        {
            f1=1;
            break;
        }
        if(cnt2==4)
        {
            f2=1;
            break;
        }
        //cout<<cnt1<<"  "<<cnt2<<endl;
    }
    cnt1=0;cnt2=0;
    for(j=0;j<4;j++)
    {

        if(s[j][3-j]=='T'||s[j][3-j]=='O')
        cnt1++;
        if(s[j][3-j]=='T'||s[j][3-j]=='X')
        cnt2++;
        if(cnt1==4)
        {
            f1=1;
            break;
        }
        if(cnt2==4)
        {
            f2=1;
            break;
        }
        //cout<<cnt1<<"  "<<cnt2<<endl;
    }
    if(f1==1)
    cout<<"Case #"<<i<<": O won"<<endl;
    else if(f2==1)
    cout<<"Case #"<<i<<": X won"<<endl;
    else if(f1==0&&f2==0&&d==16)
    cout<<"Case #"<<i<<": Draw"<<endl;
    else
    cout<<"Case #"<<i<<": Game has not completed"<<endl;

}
return 0;
}

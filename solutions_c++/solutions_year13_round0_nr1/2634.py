//Author: prakash.mishra005
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
    int O=0,X=0,d=0;
    for(j=0;j<4;j++)
    for(k=0;k<4;k++)
    if(s[j][k]!='.')
    d++;
    for(j=0;j<4;j++)
    {
        int cntO=0,cntX=0;
        for(k=0;k<4;k++)
        {
            if(s[j][k]=='T'||s[j][k]=='O')
            cntO++;
            if(s[j][k]=='T'||s[j][k]=='X')
            cntX++;
        }
        if(cntO==4)
        {
            O=1;
            break;
        }
        if(cntX==4)
        {
            X=1;
            break;
        }
    }
    for(k=0;k<4;k++)
    {
        int cntO=0,cntX=0;
        for(j=0;j<4;j++)
        {
            if(s[j][k]=='T'||s[j][k]=='O')
            cntO++;
            if(s[j][k]=='T'||s[j][k]=='X')
            cntX++;
        }
        if(cntO==4)
        {
            O=1;
            break;
        }
        if(cntX==4)
        {
            X=1;
            break;
        }
    }
    int cntO=0,cntX=0;
    for(j=0;j<4;j++)
    {

        if(s[j][j]=='T'||s[j][j]=='O')
        cntO++;
        if(s[j][j]=='T'||s[j][j]=='X')
        cntX++;
        if(cntO==4)
        {
            O=1;
            break;
        }
        if(cntX==4)
        {
            X=1;
            break;
        }
        //cout<<cntO<<"  "<<cntX<<endl;
    }
    cntO=0;cntX=0;
    for(j=0;j<4;j++)
    {

        if(s[j][3-j]=='T'||s[j][3-j]=='O')
        cntO++;
        if(s[j][3-j]=='T'||s[j][3-j]=='X')
        cntX++;
        if(cntO==4)
        {
            O=1;
            break;
        }
        if(cntX==4)
        {
            X=1;
            break;
        }
        //cout<<cntO<<"  "<<cntX<<endl;
    }
    if(O==1)
    cout<<"Case #"<<i<<": O won"<<endl;
    else if(X==1)
    cout<<"Case #"<<i<<": X won"<<endl;
    else if(O==0&&X==0&&d==16)
    cout<<"Case #"<<i<<": Draw"<<endl;
    else
    cout<<"Case #"<<i<<": Game has not completed"<<endl;

}
return 0;
}

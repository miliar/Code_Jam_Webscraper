#include <iostream>
#include <sstream>
#include <utility>
#include <cstdlib>
#include <cstdio>
#include <cctype>
#include <cmath>
#include <functional>
#include <algorithm>
#include <numeric>
#include <string>
#include <vector>
#include <queue>
#include <stack>
#include <list>
#include <map>
#include <set>
using namespace std;

#define FOR(i,a,b)  for(int i=(a);i<(b);++i)
#define F(i,a)      FOR(i,0,a)
#define ALL(x)      x.begin(),x.end()
#define PB          push_back
#define S           size()

int main()
{

freopen("A-large.in","r",stdin);
long long t,to=0;
cin>>t;
while(t--)
{
    to++;
    long long n,k,re;
    cin>>n>>k;
    if(n==1)re=2;
    if(n==2)re=4;
    if(n==3)re=8;
    if(n==4)re=16;
    if(n==5)re=32;
    if(n==6)re=64;
    if(n==7)re=128;
    if(n==8)re=256;
    if(n==9)re=512;
    if(n==10)re=1024;
    if(n==11)re=2048;
    if(n==12)re=4096;
    if(n==13)re=8192;
    if(n==14)re=16384;
    if(n==15)re=32768;
    if(n==16)re=65536;
    if(n==17)re=131072;
    if(n==18)re=262144;
    if(n==19)re=524288;
    if(n==20)re=1048576;
    if(n==21)re=2097152;
    if(n==22)re=4194304;
    if(n==23)re=8388608;
    if(n==24)re=16777216;
    if(n==25)re=33554432;
    if(n==26)re=67108864;
    if(n==27)re=134217728;
    if(n==28)re=268435456;
    if(n==29)re=536870912;
    if(n==30)re=1073741824;
    
    k++;
    if(k%re==0)cout<<"Case #"<<to<<": "<<"ON"<<endl;
    else cout<<"Case #"<<to<<": "<<"OFF"<<endl;
}
return 0;
}

#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
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
#define FOR( i,a,b ) for(int i=a;i<b;i++)
#define VI vector<int>
#define VS vector<string>
#define mp make_pair
#define NS string::npos
using namespace std;
int call()
{
    int n;
    cin>>n;
    int s;
    cin>>s;
    int p;
    cin>>p;
    int s1,s2;
    s1=3*p-4;
    s2=3*p-3;
    vector<int> v;
    v.resize(n);
    int tmp=0,m=0;
    for(int i=0;i<n;i++)
    cin>>v[i];
    for(int i=0;i<n;i++)
    {
        if(v[i]>s2  && v[i]>=p)tmp++;
        if((v[i]==s1 || v[i]==s2)&&(v[i]>=p))m++;
    }
  //  cout<<tmp<<" "<<m<<" "<<s<<endl;
tmp=tmp+min(s,m);
return tmp;
}
int main()
{
    int t;
    freopen("b2.in","r",stdin);
    freopen("b2out.txt","w",stdout);

    cin>>t;
    int i=1;
    while(i<=t)
    {
        cout<<"Case #"<<i<<": "<<call()<<endl;
        i++;
    }
return 0;
}

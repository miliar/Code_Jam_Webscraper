/*ID: jbsu321
PROG: test
LANG: C++
*/

#include <cstdio>
#include <iostream>
#include <cstdlib>
#include <cmath>
#include <cstring>
#include <map>
#include <set>
#include <vector>
#include <stack>
#include <queue>
#include <algorithm>
#include <string>
#include <sstream>
#include <list>

#define ms(a,b) memset(a, b, sizeof(a))
#define pb(a) push_back(a)
#define pi (2*acos(0))
#define oo 1<<29
#define dd double
#define ll long long
#define ff float
#define EPS 10E-10
#define fr first
#define sc second
#define MAXX 100
#define SZ(a) (int)a.size()
#define all(a) a.begin(),a.end()
#define intlim 2147483648
#define rtintlim 46340
#define llim 9223372036854775808
#define rtllim 3037000499
#define ull unsigned long long

using namespace std;

map<char , char>mp;

void process()
{
    mp['q']='z';
    mp['z']='q';
    string str1="ejp mysljylc kd kxveddknmc re jsicpdrysi";
    string str2="our language is impossible to understand";
    for(int i=0;i<SZ(str1);i++)
        mp[str1[i]]=str2[i];

    str1="rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd";
    str2="there are twenty six factorial possibilities";
    for(int i=0;i<SZ(str1);i++)
        mp[str1[i]]=str2[i];

    str1="de kr kd eoya kw aej tysr re ujdr lkgc jv";
    str2="so it is okay if you want to just give up";
    for(int i=0;i<SZ(str1);i++)
        mp[str1[i]]=str2[i];

    string s1, s2;
    ll t, cas=1;
    cin>>t;getchar();
    while(t--)
    {
        getline(cin,s1);
        cout<<"Case #"<<cas++<<": ";
        for(int i=0;i<SZ(s1);i++)
            cout<<mp[s1[i]];
        cout<<endl;
    }
return;
}

int main()
{
    freopen("A.in","r",stdin);
    freopen("A.out","w",stdout);
    process();
    return 0;
}




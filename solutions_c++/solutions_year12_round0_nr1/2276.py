#include <map>
#include <set>
#include <list>
#include <cmath>
#include <queue>
#include <stack>
#include <bitset>
#include <vector>
#include <cstdio>
#include <string>
#include <sstream>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <algorithm>
using namespace std;
#define PB push_back
#define MP make_pair
#define SZ(v) ((int)(v).size())
#define abs(x) ((x) > 0 ? (x) : -(x))
#define pp pair<char,char>
#define f find
#define in insert
typedef long long LL;
map<char,char> base;

void do_base()
{
    base.in(pp('y','a'));
    base.in(pp('n','b'));
    base.in(pp('f','c'));
    base.in(pp('i','d'));
    base.in(pp('c','e'));
    base.in(pp('w','f'));
    base.in(pp('l','g'));
    base.in(pp('b','h'));
    base.in(pp('k','i'));
    base.in(pp('u','j'));
    base.in(pp('o','k'));
    base.in(pp('m','l'));
    base.in(pp('x','m'));
    base.in(pp('s','n'));
    base.in(pp('e','o'));
    base.in(pp('v','p'));
    base.in(pp('q','z'));
    base.in(pp('p','r'));
    base.in(pp('d','s'));
    base.in(pp('r','t'));
    base.in(pp('j','u'));
    base.in(pp('g','v'));
    base.in(pp('t','w'));
    base.in(pp('h','x'));
    base.in(pp('a','y'));
    base.in(pp('z','q'));
    base.in(pp(' ',' '));
}

int main()
{
    freopen("A.in","r",stdin);
    freopen("A.out","w",stdout);
    do_base();
    int t;
    cin>>t;
    string temp;
    cin.ignore(1,'\n');
    for (int k=1; k<=t; k++)
    {
        getline(cin,temp);
        cout<<"Case #"<<k<<": ";
        for (int i=0; i<SZ(temp); i++) cout<<base[temp[i]];
        cout<<endl;
    }
    return 0;
}

#include <iostream>
#include <cmath>
#include <algorithm>
#include <string>
#include <vector>
#include <sstream>
using namespace std;

#define two(x)  (1<<x)
#define twol(x) ((long long)1<<x)
#define sqr(x)  ((x)*(x))

string dic[5000];

bool check(string s,string t)
{
    if (s==""&&t=="")   return 1;
    if (s==""||t=="")   return 0;
    if (s[0]=='(')
    {
        int p=0;
        while (s[p]!=')')   p++;
        bool c=0;
        for (int i=1;i<p;i++)
            if (s[i]==t[0])
            {
                c=1;
                break;
            }
        if (!c) return 0;
        s=s.substr(p+1);
        t=t.substr(1);
    }
    else
    {
        if (s[0]!=t[0]) return 0;
        s=s.substr(1);
        t=t.substr(1);
    }   
    return check(s,t);
}

main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int l,d,n;
    cin>>l>>d>>n;
    for (int i=0;i<d;i++)
        cin>>dic[i];
    for (int i=0;i<n;i++)
    {
        string cur;
        cin>>cur;
        int ret=0;
        for (int j=0;j<d;j++)
            ret+=check(cur,dic[j]);
        printf("Case #%d: %d\n",i+1,ret);   
    }
}

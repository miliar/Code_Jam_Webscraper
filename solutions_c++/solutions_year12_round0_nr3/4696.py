#include <iostream>
#include <stdio.h>
#include <string>
#include <algorithm>
using namespace std;
bool f(int a,int b)
{
    string s1,s2;
    s1=s2="";
    while (a!=0)
        s1+=a%10,
        a/=10;
    while (b!=0)
        s2+=b%10,
        b/=10;
    reverse(s1.begin(),s1.end());
    reverse(s2.begin(),s2.end());
    if (s1.length() != s2.length()) return 0;
    int len = s1.length();
    s1 = s1+s1;
    for (int i=0;i<=s1.length()-len;i++)
    {
        string temp="";
        for (int j=i;j<=i+len-1;j++)
            temp+=s1[j];
        if (temp == s2) return 1;
    }

    return 0;
}
int main()
{
    freopen("C-small-attempt0.in","r",stdin);
    freopen("C-small-attempt0.out","w",stdout);
    int a,b,t;
    cin>>t;
    for (int T=0;T<t;T++)
    {
        int s=0;
        cin>>a>>b;
        for (int i=a;i<b;i++)
            for (int j=i+1;j<=b;j++)
                if (f(i,j))
                    s++;
        cout<<"Case #"<<T+1<<": "<<s<<endl;
    }
    return 0;
}

#include <iostream>
#include <stdio.h>
#include <map>
#include <cstring>
#include <string>
using namespace std;

int main()
{
    freopen("A-small-attempt1.in","r",stdin);
   freopen("xxx.out","w",stdout);
    int n;
    int ii=1;
    char t[30]={'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};
    string s;
    map<char,char> m;

    cin>>n;
    getchar();
    while(n--)
    {

        m[' ']=' ';
        for(int i=0;i<26;i++)
            m['a'+i]=t[i];
        getline(cin,s);
        printf("Case #%d: ",ii++);
        for(int i=0;i<s.length();i++)
        cout<<m[s[i]];
        cout<<endl;
    }

    return 0;
}

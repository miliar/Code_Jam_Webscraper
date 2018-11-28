#include <iostream>
#include <cstdio>
#include <cstring>
#include <cctype>
using namespace std;
string s, dg = "yhesocvxduiglbkrztnwjpfmaq";
int tests;
int main()
{
    freopen("A-small-attempt0.in","r",stdin);
    freopen("tmp.txt","w",stdout);
    cin>>tests;
    getline(cin,s);

    for(int j=1;j<=tests;j++)
    {
        getline(cin,s);

        for(int tmp=0; tmp<s.size();tmp++)
            if (isalpha(s[tmp])) s[tmp]=dg[s[tmp]-'a'];

        cout<<"Case #"<<j<<": "<<s<<endl;
    }
    return 0;
}

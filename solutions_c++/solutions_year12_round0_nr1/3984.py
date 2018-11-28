#include <iostream>
#include <string>
#include <fstream>
using namespace std;
int main()
{
    const string a="abcdefghijklmnopqrstuvwxyz";
    const string b="yhesocvxduiglbkrztnwjpfmaq";
    freopen("A-small-attempt0.in","r",stdin);
    freopen("p1.out","w",stdout);
    int T;
    cin>>T;
    string s;
    getline(cin,s);
    for (int asd=0; asd<T; asd++)
    {
        getline(cin,s);
        string ans="";
        for (int i =0; i<s.length(); i++)
        {
            if (s[i]!=' ')
                ans+=b[a.find(s[i])];
            else
                ans+=" ";
        }
        cout<<"Case #"<<asd+1<<": "<<ans<<endl;
    }
}

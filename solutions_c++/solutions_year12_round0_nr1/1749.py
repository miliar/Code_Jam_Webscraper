#include <iostream>
#include <cstdio>
#include <cstring>
#include <cctype>
using namespace std;
typedef long long ll;
const string r="yhesocvxduiglbkrztnwjpfmaq";
int main()
{
    freopen("A-small-attempt0.in","r",stdin);
    freopen("Answer.txt","w",stdout);
    int t;
    cin>>t;
    string s;
    getline(cin,s);
    for(int q=1;q<=t;q++)
    {
        getline(cin,s);
        for(int i=0;i<s.size();i++)
            if (isalpha(s[i]))
                s[i]=r[s[i]-'a'];
        cout<<"Case #"<<q<<": "<<s<<endl;
    }
    return 0;
}

#include <fstream>
#include <iostream>
#include <string>

using namespace std;

string s;
int i,n;

//ifstream cin("Speaking.in");
//ofstream cout("Speaking.out");

int main()
{
    char next[26]={'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};
    cin>>n;
    getline(cin,s);
    for (int j = 1;j<=n;j++)
    {
        getline(cin,s);
        for (i = 0;i<s.length();i++)
        if (s[i]!=' ')
        {
            s[i]=next[s[i]-'a'];
        }
        cout<<"Case #"<<j<<": "<<s<<endl;
    }
}

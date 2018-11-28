#include <cstring>
#include <iostream>
#include <map>
#include <cstdio>
using namespace std;

string str = "abcdefghijklmnopqrstuvwxyz";
string str1 = "yhesocvxduiglbkrztnwjpfmaq";

int main()
{
    freopen("A-small-attempt0.in","r", stdin);
    freopen("A-small-attempt0.out","w", stdout);
    int ca;
    cin >> ca;
    getchar();
    string s;
    int t=0;
    while(ca--)
    {
        getline(cin, s);
        int n= s.size();
        for( int i = 0; i < n; ++i )
        {
            if(s[i] == ' ')
               continue;
            s[i] = str1[s[i]-'a'];
        }
        printf("Case #%d: ", ++t);
        cout<<s<<endl;
    }
    return 0;
}


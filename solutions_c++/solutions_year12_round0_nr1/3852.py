#include <vector>
#include <list>
#include <iostream>
#include <fstream>
#include <string>
#include <map>
#include <set>
#include <algorithm>
#include <memory.h>
#include <cmath>

using namespace std;

char table[26] = {'y','n','f','i','c','w','l','b','k','u','o','m','x','s','e','v','z','p','d','r','j','g','t','h','a','q'};
char table2[26];

string solve(string str)
{
    for( int i=0; i!=str.size(); i++)
    {
        if( islower(str[i]) )
        {
            str[i] = table2[str[i]-'a'];
        }
    }
    return str;
}

int main()
{
    freopen("A-small-attempt0.in","r",stdin);
    freopen("out.txt","w",stdout);
    int T;
    cin>>T;
    string str;
    for( int i=0; i!=26; i++)
    {
        table2[table[i]-'a'] = i+'a';
    }
    getchar();
    for( int i=1; i<=T; i++)
    {
        getline(cin,str);
        cout<<"Case #"<<i<<": "<<solve(str)<<endl;
    }
    return 0;
}

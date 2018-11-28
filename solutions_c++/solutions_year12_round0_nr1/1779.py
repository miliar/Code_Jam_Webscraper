#include <algorithm>
#include <iostream>
#include <cstring>
#include <cstdlib>
#include <cstdio>
#include <string>
#include <map>
using namespace std;

map <char, char> D;
string CT = "ejp mysljylc kd kxveddknmc re jsicpdrysirbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcdde kr kd eoya kw aej tysr re ujdr lkgc jvqz";
string PT = "our language is impossible to understandthere are twenty six factorial possibilitiesso it is okay if you want to just give upzq";
string decode(string s)
{
    for(int i = 0; i < s.length(); i++)
    {
        s[i] = D[s[i]];
    }
    return s;
}

int main()
{
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    for(int i = 0; i < PT.length(); i++)
        D[CT[i]] = PT[i];
    int TestCase;
    cin >> TestCase;
    char c;
    cin.get(c);
    for(int CaseID = 1; CaseID <= TestCase; CaseID ++)
    {

        string s;
        while(cin.get(c))
        {
            if(c == '\n')
                break;
            s += c;
        }
        cout << "Case #" << CaseID << ": " << decode(s) << endl;
    }
    return 0;
}

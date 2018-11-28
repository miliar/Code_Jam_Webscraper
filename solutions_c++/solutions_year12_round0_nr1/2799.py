#include <iostream>
#include <map>
#include <string>
using namespace std;

map<char,char> dict;
string s;
int tn;

int main()
{
    freopen("A-small-attempt0.in","r",stdin);
    freopen("A-small.out","w",stdout);
    
    int i;
    string sin,sout;
    sin = "ejp mysljylc kd kxveddknmc re jsicpdrysi";
    sout = "our language is impossible to understand";
    for (i=0;i<sin.length();i++)
        dict[sin[i]] = sout[i];
    sin = "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd";
    sout = "there are twenty six factorial possibilities";
    for (i=0;i<sin.length();i++)
        dict[sin[i]] = sout[i];
    sin = "de kr kd eoya kw aej tysr re ujdr lkgc jv";
    sout = "so it is okay if you want to just give up";
    for (i=0;i<sin.length();i++)
        dict[sin[i]] = sout[i];   
    dict['q'] = 'z';
    dict['z'] = 'q';
    dict[' '] = ' ';
 
    cin >> tn;
    cin.get();
    for (int t=1;t<=tn;t++)
    {
        getline(cin,s);
        cout << "Case #" << t << ": ";
        for (i=0;i<s.length();i++)
            cout << dict[s[i]];
        cout << endl;
    }          
}

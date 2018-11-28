#include <stdio.h>
#include <stdlib.h>
#include <conio.h>
#include <iostream>
#include <set>
#define repl(str,a,b) if (str==a) str = b; else
using namespace std;
int main()
{
    int nr;
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    cin >> nr;
    string ss;
    getline(cin,ss);
    int nrtot = 0;
    int nrc=0;


    for (int k=0;k<nr;k++)
    {
        string s;
        getline(cin,s);
        for (int i=0;i<s.size();i++)
        {
            repl(s[i],'a','y')//
            repl(s[i],'b','h')//
            repl(s[i],'c','e')//
            repl(s[i],'d','s')//
            repl(s[i],'e','o')//
            repl(s[i],'f','c')//
            repl(s[i],'g','v')//
            repl(s[i],'h','x')//
            repl(s[i],'i','d')//
            repl(s[i],'j','u')//
            repl(s[i],'k','i')//
            repl(s[i],'l','g')//
            repl(s[i],'m','l')//
            repl(s[i],'n','b')//
            repl(s[i],'o','k')//
            repl(s[i],'p','r')//
            repl(s[i],'q','z')
            repl(s[i],'r','t')//
            repl(s[i],'s','n')//
            repl(s[i],'t','w')//
            repl(s[i],'u','j')//
            repl(s[i],'v','p')//
            repl(s[i],'w','f')//
            repl(s[i],'x','m')//
            repl(s[i],'y','a')//
            repl(s[i],'z','q')//
            s[i]=s[i];

        }
        cout <<"Case #"<<k+1<<": "<< s<<endl;
    }

    return 0;
}

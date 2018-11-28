#include <iostream>
#include <cstdio>
#include <map>
#include <string>
#include <vector>
#include <algorithm>
#include <fstream>
#include <cmath>
#include <string>
using namespace std;

#define forsn(i,s,n) for(int i=(s);i<(int)(n);i++)
#define forn(i,n) forsn(i,0,n)
#define esta(x,c) (c.find(x)!=c.end())
#define all(v) v.begin(),v.end()
map <char,char> m; //entra en base google y sale en la canonica
string translation(string s)
{
    string t;
    forn(i,s.size())
    {
        t+=m[s[i]];
    }
    return t;
}

int main ()
{
    freopen("Acodejam.in","r",stdin);
    freopen("Acodejam.out","w",stdout);
    int n;
    string str00, str10, str20, str01, str11, str21, s, t;
    m['y']='a';
    m['e']='o';
    m['q']='z';
    m[' ']=' ';

    str00="ejp mysljylc kd kxveddknmc re jsicpdrysi";
    str10="rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd";
    str20="de kr kd eoya kw aej tysr re ujdr lkgc jv";
    str01="our language is impossible to understand";
    str11="there are twenty six factorial possibilities";
    str21="so it is okay if you want to just give up";

    s=str00;
    t=str01;
    forn(i,s.size())
    {
        if(esta(s[i],m)==false)
        {
            m[s[i]]=t[i];
        }
    }

    s=str10;
    t=str11;
    forn(i,s.size())
    {
        if(esta(s[i],m)==false)
        {
            m[s[i]]=t[i];
        }
    }

    s=str20;
    t=str21;
    forn(i,s.size())
    {
        if(esta(s[i],m)==false)
        {
            m[s[i]]=t[i];
        }
    }
    //Lo corro una vez y veo que la única letra que falta es la z
    //y como es una funcion biyectiva, busco la letra que falta en la imagen, que es q
    m['z']='q';
    cin >> n;
    string str;
    getline(cin,str);
    forn(i,n)
    {
        getline(cin,str);
        cout << "Case #"<< i+1 <<": "<<translation(str)<<endl;
    }

}

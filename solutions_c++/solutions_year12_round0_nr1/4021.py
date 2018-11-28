#include <iostream>
#include <fstream>
#include <sstream>
#include <iterator>
#include <vector>
#include <string>
#include <map>
#include <algorithm>

#include <cstdio>

using namespace std;


void parse(map<char, char> & dic, const string & g, const string & e)
{
    for(int i = 0; i < g.length(); i++)
    {
        if(dic.find(g[i]) == dic.end())
            dic[g[i]] = e[i];
    }
}


int main()
{
    string g1("ejp mysljylc kd kxveddknmc re jsicpdrysi");
    string g2("rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd");
    string g3("de kr kd eoya kw aej tysr re ujdr lkgc jv");

    string e1("our language is impossible to understand");
    string e2("there are twenty six factorial possibilities");
    string e3("so it is okay if you want to just give up");

    map<char, char> dic;
    parse(dic, g1, e1);
    parse(dic, g2, e2);
    parse(dic, g3, e3);

    dic['q'] = 'z';
    dic['z'] = 'q';

    string buf;
    getline(cin, buf);
    int T;
    sscanf(buf.c_str(), "%d", &T);

    for(int k = 1; k <= T; k++)
    {
        getline(cin, buf);
        cout << "Case #" << k << ": ";
        for(int i = 0; i < buf.length(); i++)
        {
            cout << dic[buf[i]];
        }
        cout << endl;
    }


//    for(map<char, char>::const_iterator it = dic.begin(); it != dic.end(); it++)
//        cout << it->first << it->second << endl;

    return 0;
}

#include <iostream>
#include <string>
#include <map>
#include <vector>
#include <set>

using namespace std;

#define IN(x,y) ((x).find((y)) != (x).end())
#define FOREACH(_it,_l) for(__typeof((_l).begin()) _it=((_l).begin());(_it)!=(_l).end();++(_it))

int main( int argc, char ** argv)
{
    map<char,char> dict;
    set<char> letters;
    
    for( size_t i = 97; i <=122; ++i )
        letters.insert(char(i));
    dict['q']='z';
    dict['z']='q';
    vector<string> s,d;
    s.push_back("ejp mysljylc kd kxveddknmc re jsicpdrysi");
    s.push_back("rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd");
    s.push_back("de kr kd eoya kw aej tysr re ujdr lkgc jv");
    d.push_back("our language is impossible to understand");
    d.push_back("there are twenty six factorial possibilities");
    d.push_back("so it is okay if you want to just give up");

    for( size_t i = 0; i < 3; ++i )
    {
        for( size_t j = 0; j < s[i].size(); ++j )
        {
            dict[s[i][j]]= d[i][j];
            letters.erase(d[i][j]);
        }
    }

    int X;
    string t;
    getline(cin,t);
    X = atoi(t.c_str());

    for( int CASE = 1; CASE <= X; ++CASE )
    {
        getline(cin,t);
        cout<<"Case #"<<CASE<<": ";
        for( int i = 0; i < t.size(); ++i )
        {
            if( IN(dict,t[i]))cout<<dict[t[i]];
                    else cout<<"X";
        }
        cout<<endl;
    }

}

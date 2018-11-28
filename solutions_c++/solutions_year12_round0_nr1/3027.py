#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <map>
#include <list>
#include <utility>
#include <string>

class Found{};

using namespace std;

int main()
{
    ifstream in("C:\\Users\\Olexandr\\Desktop\\A-small-attempt0.in");
    ofstream out("C:\\Users\\Olexandr\\Desktop\\output.txt");
    int T;
    in>>T;

    vector<pair<string, string> > known;
    known.push_back(make_pair(  "ejp mysljylc kd kxveddknmc re jsicpdrysi",      "our language is impossible to understand"     ));
    known.push_back(make_pair(  "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd",  "there are twenty six factorial possibilities" ));
    known.push_back(make_pair(  "de kr kd eoya kw aej tysr re ujdr lkgc jv",     "so it is okay if you want to just give up"    ));

    vector<char> table(256);

    for(int i=0; i<known.size(); i++)
        for(int s=0; s<known[i].first.size(); s++)
            table[known[i].first[s]]=known[i].second[s];
    table['z']='q';
    table['q']='z';

    in.ignore(100, '\n');
    for(int t=0; t<T; t++)
    {
        out<<"Case #"<<(t+1)<<": ";
        string line;
        getline(in, line);
        for(int s=0; s<line.size(); s++)
            out<<char(table[line[s]]);
        out<<endl;
    }
    //system("pause>nul");
    return 0;
}
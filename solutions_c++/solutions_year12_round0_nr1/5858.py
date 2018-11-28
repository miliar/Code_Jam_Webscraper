#include <iostream>
#include <string>
#include <map>
using namespace std;

int main(int argc, const char *argv[])
{
    map<char,char> tr;

    string inputs[4][2] = {
        {"ejp mysljylc kd kxveddknmc re jsicpdrysiz", "our language is impossible to understandq"},
        {"rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd", "there are twenty six factorial possibilities"},
        {"de kr kd eoya kw aej tysr re ujdr lkgc jv", "so it is okay if you want to just give up"},
        {"y qee", "a zoo"},
    };

    for(int i=0; i<4; i++)
        for(int j=0; j<inputs[i][0].size(); j++)
        {
            tr[inputs[i][0][j]] = inputs[i][1][j];
        }

    int T;
    cin >> T;

    cin.ignore();

    string G;
    for(int i=0; i<T; i++)
    {
        getline(cin, G);
        for(int j=0; j<G.size(); j++)
            G[j] = tr[G[j]];
        cout << "Case #" << (i+1) << ": " << G << "\n";
    }

    return 0;
}

#include <iostream>
#include <map>
#include <cstdio>
#include <cctype>
using namespace std;

int main()
{
    string in = "ejpmysljylckdkxveddknmcrejsicpdrysirbcpcypcrtcsradkhwyfrepkymveddknkmkrkcddekrkdeoyakwaejtysrreujdrlkgcjv";
    string out = "ourlanguageisimpossibletounderstandtherearetwentysixfactorialpossibilitiessoitisokayifyouwanttojustgiveup";

    char mapping[256];
    for ( int i=0 ; i<in.length() ; ++i )
    {
        mapping[in[i]] = out[i];
    }
    mapping['z'] = 'q';
    mapping['q'] = 'z';
    mapping[' '] = ' ';

    int T;
    cin >> T;
    cin.ignore();
    for ( int t=1 ; t<=T ; ++t )
    {
        string line;
        getline(cin, line);
        cout << "Case #" << t << ": ";
        for ( int i=0 ; i<line.length() ; ++i )
        {
            cout << mapping[line[i]];
        }
        cout << endl;
    }

    return 0;
}

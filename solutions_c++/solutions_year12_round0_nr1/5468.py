#include <iostream>
#include <fstream>
#include <string>
#include <map>
using namespace std;

string mp = "yhesocvxduiglbkrztnwjpfmaq";

int main(void)
{
    ios::sync_with_stdio(false);
#ifdef DEBUG
    ifstream fin("A-small-attempt0.in");
    streambuf *backup = cin.rdbuf(fin.rdbuf());
#endif
    string line;
    int ncases;
    cin >> ncases;
    getline(cin, line);
    for (int t = 1; t <= ncases; ++t)
    {
        getline(cin, line);
        int len = line.length();
        cout << "Case #" << t << ": ";
        for (int i = 0; i < len; ++i)
        {
            if (line[i] == ' ')
                cout << ' ';
            else
                cout << mp[line[i] - 'a'];
        }
        cout << endl;
    }
    
#ifdef DEBUG
    cin.rdbuf(backup);
    fin.close();
#endif
    return 0;
}

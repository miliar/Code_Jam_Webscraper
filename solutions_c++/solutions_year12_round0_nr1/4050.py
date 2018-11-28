#include <cmath>
#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <algorithm>

using namespace std;
int main()
{
    string s1("abcdefghijklmnopqrstuvwxyz");
    string s2("yhesocvxduiglbkrztnwjpfmaq");
    map<char,char> mp;
    for(int i = 0;i < s1.size();++i)
        mp[s1[i]] = s2[i];

    ifstream fin("A_in.txt");
    ofstream fout("A_out.txt");

    string s;
    int T;
    fin >> T;
    fin.get();
    for(int cnt = 1;cnt <= T;++cnt)
    {
        getline(fin,s);
        for(int i = 0;i < s.size();++i)
        {
            if(mp.count(s[i]))
                s[i] = mp[s[i]];
        }

        fout << "Case #" << cnt << ": " << s << endl;
    }
    return 0;
}

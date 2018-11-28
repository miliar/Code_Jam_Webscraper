#include <iostream>
#include <map>
#include <string>
#include <fstream>
#include <cstdlib>
#include <sstream>

using namespace std;

int main()
{
    map<char, char> mapping;
    int T;
    string s;
    string buffer;
    
    mapping.insert(pair<char, char>('a', 'y'));
    mapping.insert(pair<char, char>('b', 'h'));
    mapping.insert(pair<char, char>('c', 'e'));
    mapping.insert(pair<char, char>('d', 's'));
    mapping.insert(pair<char, char>('e', 'o'));
    mapping.insert(pair<char, char>('f', 'c'));
    mapping.insert(pair<char, char>('g', 'v'));
    mapping.insert(pair<char, char>('h', 'x'));
    mapping.insert(pair<char, char>('i', 'd'));
    mapping.insert(pair<char, char>('j', 'u'));
    mapping.insert(pair<char, char>('k', 'i'));
    mapping.insert(pair<char, char>('l', 'g'));
    mapping.insert(pair<char, char>('m', 'l'));
    mapping.insert(pair<char, char>('n', 'b'));
    mapping.insert(pair<char, char>('o', 'k'));
    mapping.insert(pair<char, char>('p', 'r'));
    mapping.insert(pair<char, char>('q', 'z'));
    mapping.insert(pair<char, char>('r', 't'));
    mapping.insert(pair<char, char>('s', 'n'));
    mapping.insert(pair<char, char>('t', 'w'));
    mapping.insert(pair<char, char>('u', 'j'));
    mapping.insert(pair<char, char>('v', 'p'));
    mapping.insert(pair<char, char>('w', 'f'));
    mapping.insert(pair<char, char>('x', 'm'));
    mapping.insert(pair<char, char>('y', 'a'));
    mapping.insert(pair<char, char>('z', 'q'));
    
    ifstream fin("A-small-attempt2.in");
    getline(fin, buffer);
    ofstream os;
    os.open("out.txt");
    
    T = atoi(buffer.c_str());
    
    for (int i = 0; i < T; i++)
    {
        getline(fin, buffer);
        
        os<<"Case #"<<i+1<<": ";
        istringstream iss(buffer);
        iss>>s;
        for (int j = 0; j < s.size(); j++)
            os<<mapping[s[j]];
        
        while (iss >> s)
        {
            os<<" ";
            for (int j = 0; j < s.size(); j++)
            {
                if (s[j] == ' ') os<<s[j];
                else
                    os<<mapping[s[j]];
            }
        }
        if (i < T - 1)
           os<<endl;
    }
    os.close();
    
    return 0;
}

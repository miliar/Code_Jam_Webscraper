#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <map>
#include <sstream>

using namespace std;

int main()
{
    map<char, char> dict;
    dict.insert(std::pair<char,char>('a', 'y'));
    dict.insert(std::pair<char,char>('b', 'h'));
    dict.insert(std::pair<char,char>('c', 'e'));
    dict.insert(std::pair<char,char>('d', 's'));
    dict.insert(std::pair<char,char>('e', 'o'));
    dict.insert(std::pair<char,char>('f', 'c'));
    dict.insert(std::pair<char,char>('g', 'v'));
    dict.insert(std::pair<char,char>('h', 'x'));
    dict.insert(std::pair<char,char>('i', 'd'));
    dict.insert(std::pair<char,char>('j', 'u'));
    dict.insert(std::pair<char,char>('k', 'i'));
    dict.insert(std::pair<char,char>('l', 'g'));
    dict.insert(std::pair<char,char>('m', 'l'));
    dict.insert(std::pair<char,char>('n', 'b'));
    dict.insert(std::pair<char,char>('o', 'k'));
    dict.insert(std::pair<char,char>('p', 'r'));
    dict.insert(std::pair<char,char>('q', 'z'));
    dict.insert(std::pair<char,char>('r', 't'));
    dict.insert(std::pair<char,char>('s', 'n'));
    dict.insert(std::pair<char,char>('t', 'w'));
    dict.insert(std::pair<char,char>('u', 'j'));
    dict.insert(std::pair<char,char>('v', 'p'));
    dict.insert(std::pair<char,char>('w', 'f'));
    dict.insert(std::pair<char,char>('x', 'm'));
    dict.insert(std::pair<char,char>('y', 'a'));
    dict.insert(std::pair<char,char>('z', 'q'));

    string line;
    getline(cin, line);
    
    stringstream ss("");
    ss<<line;
    int howmany;
    ss>>howmany;
    
    int p = 1;
    for(int n = 0; n < howmany; n++)
    {
        getline(cin, line);
        printf("Case #%d: ", p++);
        
        for(int i = 0; i < line.size(); i++)
        {
            if(dict.find(line[i]) == dict.end())
                printf("%c", line[i]);
            else
                printf("%c", (char)( dict[ (char)(line[i]) ] ));
        }
        printf("\n");
        
    }


}

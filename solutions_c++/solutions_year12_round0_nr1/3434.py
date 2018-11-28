#include <iostream>
#include <map>
#include <string>
#include <cctype>
using namespace std;
map<char, char> my_map;

int main()
{
    my_map.insert(pair<char,char>('a','y'));
    my_map.insert(pair<char,char>('b','h'));
    my_map.insert(pair<char,char>('c','e'));
    my_map.insert(pair<char,char>('d','s'));
    my_map.insert(pair<char,char>('e','o'));
    my_map.insert(pair<char,char>('f','c'));
    my_map.insert(pair<char,char>('g','v'));
    my_map.insert(pair<char,char>('h','x'));
    my_map.insert(pair<char,char>('i','d'));
    my_map.insert(pair<char,char>('j','u'));
    my_map.insert(pair<char,char>('k','i'));
    my_map.insert(pair<char,char>('l','g'));
    my_map.insert(pair<char,char>('m','l'));
    my_map.insert(pair<char,char>('n','b'));
    my_map.insert(pair<char,char>('o','k'));
    my_map.insert(pair<char,char>('p','r'));
    my_map.insert(pair<char,char>('q','z'));
    my_map.insert(pair<char,char>('r','t'));
    my_map.insert(pair<char,char>('s','n'));
    my_map.insert(pair<char,char>('t','w'));
    my_map.insert(pair<char,char>('u','j'));
    my_map.insert(pair<char,char>('v','p'));
    my_map.insert(pair<char,char>('w','f'));
    my_map.insert(pair<char,char>('x','m'));
    my_map.insert(pair<char,char>('y','a'));
    my_map.insert(pair<char,char>('z','q'));

    int caseNum;
    string caseStr;
    cin >> caseNum;
    getline(cin, caseStr);
    for(int i = 1; i <= caseNum; i++)
    {
        cout<<"Case #" << i <<": "; 
        getline(cin, caseStr);
        int len = caseStr.length();
        for (int j = 0;j < len; j++ )
        {
            if(!isspace(caseStr[j]))
                cout <<my_map.find(caseStr[j])->second;
            else
                cout << caseStr[j];
        }
        cout << endl;
    }
    return 0;
}
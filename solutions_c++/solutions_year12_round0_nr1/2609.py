
#include <iostream>
#include <vector>
#include <sstream>
#include <map>
#include <sstream>
using namespace std;

map<char,char> dict;
vector<char> keys;
vector<char> objs;

int main(int argc,char *argv[])
{
    dict['a'] = 'y';
    dict['b'] = 'h';
    dict['c'] = 'e';
    dict['d'] = 's';
    dict['e'] = 'o';
    dict['f'] = 'c';
    dict['g'] = 'v';
    dict['h'] = 'x';
    dict['i'] = 'd';
    dict['j'] = 'u';
    dict['k'] = 'i';
    dict['l'] = 'g';
    dict['m'] = 'l';
    dict['n'] = 'b';
    dict['o'] = 'k';
    dict['p'] = 'r';
    dict['q'] = 'z';
    dict['r'] = 't';
    dict['s'] = 'n';
    dict['t'] = 'w';
    dict['u'] = 'j';
    dict['v'] = 'p';
    dict['w'] = 'f';
    dict['x'] = 'm';
    dict['y'] = 'a';
    dict['z'] = 'q';
    dict[' '] = ' ';

    int testCaseCount;
    cin >> testCaseCount;
    string t;
    getline(cin,t);
    for(int testCase=1;testCase<=testCaseCount;testCase++)
    {
        vector<char> li;
       string str;
       getline(cin,str);

       for(int i=0;i<str.size();i++) {
           li.push_back(dict[str[i]]);
       }
       cout << "Case #" << testCase << ": " ;
       for(int i=0;i<li.size();i++) {
           cout << li[i];
       }
       cout << endl;
    }

    return 0;
}

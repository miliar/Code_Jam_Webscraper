#include <map>
#include <string>
#include <iostream>
#include <fstream>
using namespace std;
int main()
{
    map<char,char> m_map;
    m_map['a'] = 'y';
    m_map['b'] = 'h';
    m_map['c'] = 'e';
    m_map['d'] = 's';
    m_map['e'] = 'o';
    m_map['f'] = 'c';
    m_map['g'] = 'v';
    m_map['h'] = 'x';
    char c= 'i';
    m_map[c++] = 'd';
    m_map[c++] = 'u';
    m_map[c++] = 'i';
    m_map[c++] = 'g';
    m_map[c++] = 'l';
    m_map[c++] = 'b';
    m_map[c++] = 'k';
    m_map[c++] = 'r';
    m_map[c++] = 'z';
    m_map[c++] = 't';
    m_map[c++] = 'n';
    m_map[c++] = 'w';
    m_map[c++] = 'j';
    m_map[c++] = 'p';
    m_map[c++] = 'f';
    m_map[c++] = 'm';
    m_map[c++] = 'a';
    m_map[c++] = 'q';
    m_map[' ']=' ';
    int T;
    ifstream cin("A-small-attempt2.in");
    ofstream cout("out.out");
    cin>>T;
    //cin>>c;
    int kcase = 1;
    string str;
    while(T--)
    {
        getline(cin,str);
        if(str.size() == 0)
        {
            T++;
            continue;
        }
        //cout<<str<<endl;
        cout<<"Case #"<<kcase++<<": ";
        for(int i= 0;i< str.size();++i)
        {
            cout<<m_map[str.at(i)];
        }
        cout<<endl;
    }
}

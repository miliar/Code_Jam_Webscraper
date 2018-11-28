#include <iostream>
#include <fstream>
#include <string>
#include <cstdlib>
#include <cstdio>

using namespace std;

string replaceLine(string line)
{
    string res;
    for (auto i:line)
        switch (i)
        {
            case 'a': res+='y'; break;
            case 'b': res+='h'; break;
            case 'c': res+='e'; break;
            case 'd': res+='s'; break;
            case 'e': res+='o'; break;
            case 'f': res+='c'; break;
            case 'g': res+='v'; break;
            case 'h': res+='x'; break;
            case 'i': res+='d'; break;
            case 'j': res+='u'; break;
            case 'k': res+='i'; break;
            case 'l': res+='g'; break;
            case 'm': res+='l'; break;
            case 'n': res+='b'; break;
            case 'o': res+='k'; break;
            case 'p': res+='r'; break;
            case 'q': res+='z'; break;
            case 'r': res+='t'; break;
            case 's': res+='n'; break;
            case 't': res+='w'; break;
            case 'u': res+='j'; break;
            case 'v': res+='p'; break;
            case 'w': res+='f'; break;
            case 'x': res+='m'; break;
            case 'y': res+='a'; break;
            case 'z': res+='q'; break;
            case ' ': res+=' '; break;
            //default: res+=i;
            default: res+='?';
        }
    return res;
}

int main()
{
    ifstream in("A-small-attempt0.in");
    ofstream out("res.txt");
    string tmp;
    getline(in,tmp);
    auto lines=atoi(tmp.c_str());
    for (int i=0;i<lines;i++)
    {
        getline(in,tmp);
        cout << "Case #" << (i+1) << ": " << replaceLine(tmp) << endl;
        out << "Case #" << (i+1) << ": " << replaceLine(tmp) << endl;
    }
    in.close();
    out.close();
    return 0;
}

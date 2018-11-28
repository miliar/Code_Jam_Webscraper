#include <iostream>
#include <fstream>
#include <string>
using namespace std;
ofstream out("out.in");
void func(string str,int c)
{
    int pos=str.length();
    out<<"Case #"<<c<<": ";
    for(int i=0;i<pos;i++)
    {
        switch(str[i])
        {
            case 'a':out<<'y'; break;
            case 'b':out<<'h'; break;
            case 'c':out<<'e'; break;
            case 'd':out<<'s'; break;
            case 'e':out<<'o'; break;
            case 'f':out<<'c'; break;
            case 'g':out<<'v'; break;
            case 'h':out<<'x'; break;
            case 'i':out<<'d'; break;
            case 'j':out<<'u'; break;
            case 'k':out<<'i'; break;
            case 'l':out<<'g'; break;
            case 'm':out<<'l'; break;
            case 'n':out<<'b'; break;
            case 'o':out<<'k'; break;
            case 'p':out<<'r'; break;
            case 'q':out<<'z'; break;
            case 'r':out<<'t'; break;
            case 's':out<<'n'; break;
            case 't':out<<'w'; break;
            case 'u':out<<'j'; break;
            case 'v':out<<'p'; break;
            case 'w':out<<'f'; break;
            case 'x':out<<'m'; break;
            case 'y':out<<'a'; break;
            case 'z':out<<'q'; break;
            case ' ':out<<' '; break;
        }
    }
}
int main()
{
    int t,i,j;
    ifstream in("a.in");
    string str;
    if(in.is_open())
    {
        in>>t;
        for(int j=0;j<=t;j++)
        {
            getline(in,str);
            if(j!=0)
            {
                cout<<str<<endl;
                func(str,j);
                out<<endl;
            }
        }
    }
    return 0;
}

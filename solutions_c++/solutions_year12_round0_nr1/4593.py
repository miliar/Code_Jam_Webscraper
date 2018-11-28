#include <iostream>
#include<stdio.h>
#include<string>
using namespace std;

int main()
{
string str[100],curr;
int T;
cin>>T;
getline(cin,curr);



for(int i=0;i<T;++i)
{

    getline(cin,str[0]);

}


for(int i=0;i<T;++i)
{
    cout<<"Case #"<<i+1<<": ";

    for(int j=0;j<str[i].size();++j)
    {
        switch(str[i][j])
        {
            case 'a':   cout<<'y';
                        break;
            case 'b': cout<<'h';
                        break;
            case 'c':  cout<<'e';
                        break;
            case 'd':   cout<<'s';
                        break;
            case 'e':   cout<<'o';
                        break;
            case 'f':   cout<<'c';
                        break;
            case 'g':   cout<<'v';
                        break;
            case 'h':   cout<<'x';
                        break;
            case 'i':   cout<<'d';
                        break;
            case 'j':   cout<<'u';
                        break;
            case 'k':   cout<<'i';
                        break;
            case 'l':   cout<<'g';
                        break;
            case 'm':   cout<<'l';
                        break;
            case 'n':   cout<<'b';
                        break;
            case 'o':   cout<<'k';
                        break;
            case 'p':   cout<<'r';
                        break;
            case 'q':   cout<<'z';
                        break;
            case 'r':   cout<<'t';
                        break;
            case 's':   cout<<'n';
                        break;
            case 't':   cout<<'w';
                        break;
            case 'u':   cout<<'j';
                        break;
            case 'v':   cout<<'p';
                        break;
            case 'w':   cout<<'f';
                        break;
            case 'x':   cout<<'m';
                        break;
            case 'y':   cout<<'a';
                        break;
            case 'z':   cout<<'q';
                        break;
            case ' ':   cout<<' ';
                        break;

        }

    }

}








}

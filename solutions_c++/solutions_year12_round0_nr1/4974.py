#include <cstdlib>
#include <fstream>
#include <iostream>
#include <string>
using namespace std;

void translate( string &text);

int main()
{
    int caseNumber, buff=1;
    string line;
    char charLine[100];
    ifstream myInput("A-small-attempt2.in.txt");
    ofstream myOutput ("output.txt");

    myInput>>caseNumber;
    getline(myInput, line);

    while(myInput.good() && buff<=caseNumber)
    {
        getline(myInput, line);
        translate(line);

        myOutput<<"Case #"<<buff<<": "<<line<<"\n";
        buff++;

    }
}


void translate(string &text)
{
    for(int i=0; i<text.length(); i++)
    {
        if(text[i]>='a' && text[i]<='z')
            switch( text[i] ){
                case 'a':
                    text[i]='y';
                    break;
                case 'b':
                    text[i]='h';
                    break;
                case 'c':
                    text[i]='e';
                    break;
                case 'd':
                    text[i]='s';
                    break;
                case 'e':
                    text[i]='o';
                    break;
                case 'f':
                    text[i]='c';
                    break;
                case 'g':
                    text[i]='v';
                    break;
                case 'h':
                    text[i]='x';
                    break;
                case 'i':
                    text[i]='d';
                    break;
                case 'j':
                    text[i]='u';
                    break;
                case 'k':
                    text[i]='i';
                    break;
                case 'l':
                    text[i]='g';
                    break;
                case 'm':
                    text[i]='l';
                    break;
                case 'n':
                    text[i]='b';
                    break;
                case 'o':
                    text[i]='k';
                    break;
                case 'p':
                    text[i]='r';
                    break;
                case 'q':
                    text[i]='z';
                    break;
                case 'r':
                    text[i]='t';
                    break;
                case 's':
                    text[i]='n';
                    break;
                case 't':
                    text[i]='w';
                    break;
                case 'u':
                    text[i]='j';
                    break;
                case 'v':
                    text[i]='p';
                    break;
                case 'w':
                    text[i]='f';
                    break;
                case 'x':
                    text[i]='m';
                    break;
                case 'y':
                    text[i]='a';
                    break;
                case 'z':
                    text[i]='q';
                    break;
            }
    }
}

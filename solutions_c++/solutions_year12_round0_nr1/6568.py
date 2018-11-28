#include <iostream>
#include <string>
#include <fstream>

using namespace std;

char encodeLetter(char a)
{
    char letter;
    switch(a)
    {
        case ' ':
            letter=' ';
            break;
        case 'a':
            letter='y';
            break;
        case 'b':
            letter='h';
            break;
        case 'c':
            letter='e';
            break;
        case 'd':
            letter='s';
            break;
        case 'e':
            letter='o';
            break;
        case 'f':
            letter='c';
            break;
        case 'g':
            letter='v';
            break;
        case 'h':
            letter='x';
            break;
        case 'i':
            letter='d';
            break;
        case 'j':
            letter='u';
            break;
        case 'k':
            letter='i';
            break;
        case 'l':
            letter='g';
            break;
        case 'm':
            letter='l';
            break;
        case 'n':
            letter='b';
            break;
        case 'o':
            letter='k';
            break;
        case 'p':
            letter='r';
            break;
        case 'q':
            letter='z';
            break;
        case 'r':
            letter='t';
            break;
        case 's':
            letter='n';
            break;
        case 't':
            letter='w';
            break;
        case 'u':
            letter='j';
            break;
        case 'v':
            letter='p';
            break;
        case 'w':
            letter='f';
            break;
        case 'x':
            letter='m';
            break;
        case 'y':
            letter='a';
            break;
        case 'z':
            letter='q';
            break;
    }
    return letter;
}

int main()
{
    string cases;
    string googlerese;
    string text;

    ifstream input;
    ofstream out;

    input.open("A-small-attempt4.in");
    out.open("solution.txt");

    int Tcases=0;
    int j=1;

    getline(input, cases);
    sscanf(cases.c_str(), "%d", &Tcases);

    while(Tcases>0)
    {
        getline(input, googlerese);
        for(unsigned int i=0; i<googlerese.size(); ++i)
        {
            text+= encodeLetter(googlerese[i]);
        }
        out << "Case #" << j << ": " << text << endl;
        text.clear();
        googlerese.clear();
        ++j;
        --Tcases;
    }

    input.close();
    out.close();

    return 0;
}

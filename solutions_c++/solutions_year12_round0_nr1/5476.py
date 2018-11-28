#include <iostream>
#include <fstream>
#include <stdio.h>

using namespace std;

int main()
{
    ofstream f;
    ifstream file;
    string line;
    file.open("input.in");
    f.open("output.in");
    int cases;
    file>>cases;
    getline(file,line);
    for(int temp=1;temp<=cases;temp++)
    {
    f<<"Case #"<<temp<<": ";
    getline(file,line);
    int len = line.length();
    for(int t=0;t<len;t++)
    {
        char c = line[t];
    if(c=='y')
    c = 'a';
    else if(c=='n')
    c= 'b';
    else if(c=='f')
    c= 'c';
    else if(c=='i')
    c= 'd';
    else if(c=='c')
    c= 'e';
    else if(c=='w')
    c= 'f';
    else if(c=='l')
    c= 'g';
    else if(c=='b')
    c= 'h';
    else if(c=='k')
    c= 'i';
    else if(c=='u')
    c= 'j';
    else if(c=='o')
    c= 'k';
    else if(c=='m')
    c= 'l';
    else if(c=='x')
    c= 'm';
    else if(c=='s')
    c= 'n';
    else if(c=='e')
    c= 'o';
    else if(c=='v')
    c= 'p';
    else if(c=='z')
    c= 'q';
    else if(c=='p')
    c= 'r';
    else if(c=='d')
    c= 's';
    else if(c=='r')
    c= 't';
    else if(c=='j')
    c= 'u';
    else if(c=='g')
    c= 'v';
    else if(c=='t')
    c= 'w';
    else if(c=='h')
    c= 'x';
    else if(c=='a')
    c= 'y';
    else if(c=='q')
    c= 'z';
    f<<c;
    }
    f<<"\n";
    }
f.close();
file.close();
return 0;
}

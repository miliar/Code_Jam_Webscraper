#include <stdio.h>
#include <fstream>
#include <iostream>

using namespace std;

int main(int argc, char** argv)
{
    ofstream fileout;
    ifstream filein;
    filein.open("A-small-attempt0.in" , ios::in);
    fileout.open("output.txt" , ios::out);

    int Cases, Counter=1, i=0;
    char Words[101];
    filein>>Cases;
    filein.getline(Words,1);
    while (filein.getline(Words,101))
    {
        while (Words[i]!='\0')
        {
            if (Words[i]==' ')
            Words[i]=' ';
            else if (Words[i]=='b')
            Words[i]='h';
            else if (Words[i]=='c')
            Words[i]='e';
            else if (Words[i]=='d')
            Words[i]='s';
            else if (Words[i]=='e')
            Words[i]='o';
            else if (Words[i]=='f')
            Words[i]='c';
            else if (Words[i]=='g')
            Words[i]='v';
            else if (Words[i]=='h')
            Words[i]='x';
            else if (Words[i]=='i')
            Words[i]='d';
            else if (Words[i]=='j')
            Words[i]='u';
            else if (Words[i]=='k')
            Words[i]='i';
            else if (Words[i]=='l')
            Words[i]='g';
            else if (Words[i]=='m')
            Words[i]='l';
            else if (Words[i]=='n')
            Words[i]='b';
            else if (Words[i]=='o')
            Words[i]='k';
            else if (Words[i]=='p')
            Words[i]='r';
            else if (Words[i]=='q')
            Words[i]='z';
            else if (Words[i]=='r')
            Words[i]='t';
            else if (Words[i]=='s')
            Words[i]='n';
            else if (Words[i]=='t')
            Words[i]='w';
            else if (Words[i]=='u')
            Words[i]='j';
            else if (Words[i]=='v')
            Words[i]='p';
            else if (Words[i]=='w')
            Words[i]='f';
            else if (Words[i]=='x')
            Words[i]='m';
            else if (Words[i]=='y')
            Words[i]='a';
            else if (Words[i]=='z')
            Words[i]='q';
            else if (Words[i]=='a')
            Words[i]='y';

            i++;
        }
        i=0;


        fileout<<"Case #"<<Counter<<": ";
        while (Words[i]!='\0')
        {
            fileout<<Words[i];
            i++;
        }
        i=0;
        if (Counter!=Cases)
        fileout<<endl;
        Counter++;
    }

    filein.close();
    fileout.close();

    return 0;
}


#include <iostream>
#include <stdio.h>
#include <cstring>
#include <fstream>
using namespace std;

char a[26] = {'y','h','e','s','o',
              'c','v','x','d','u',
              'i','g','l','b','k',
              'r','z','t','n','w',
              'j','p','f','m','a',
              'q'};

int n;
char str[110];
fstream fin,fout;

int main()
{
    fin.open("A-small-attempt2.in",ios::in);
    fout.open("ans2.out",ios::out);
    fin >> n;
    fin.get();
    for (int i = 0; i < n; i++)
    {
        fin.getline(str,101,'\n');
        fout << "Case #" << i+1 << ": ";
        for (int j = 0; j < strlen(str); j++)
            if (str[j] == ' ') fout << ' ';
            else fout << a[str[j]-'a'];
        fout << endl;
    }
    fout.close();
}

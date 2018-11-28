#include <cstdio>
#include <iostream>
#include <vector>
#include <algorithm>
#include <string>

using namespace std;

int main()
{
    int n;
    cin >> n;
    cin.ignore();
    string T;
    for(int i = 0; i < n; i++)
    {
        string G;
        getline(cin, T);

        cout << "Case #" << i+1 << ": ";

        for(int j = 0; j < T.size(); j++)
        {
            if (T[j]=='a') putchar('y');
            else if (T[j]=='b') putchar('h');
            else if (T[j]=='c') putchar('e');
            else if (T[j]=='d') putchar('s');
            else if (T[j]=='e') putchar('o');
            else if (T[j]=='f') putchar('c');
            else if (T[j]=='g') putchar('v');
            else if (T[j]=='h') putchar('x');
            else if (T[j]=='i') putchar('d');
            else if (T[j]=='j') putchar('u');
            else if (T[j]=='k') putchar('i');
            else if (T[j]=='l') putchar('g');
            else if (T[j]=='m') putchar('l');
            else if (T[j]=='n') putchar('b');
            else if (T[j]=='o') putchar('k');
            else if (T[j]=='p') putchar('r');
            else if (T[j]=='q') putchar('z');
            else if (T[j]=='r') putchar('t');
            else if (T[j]=='s') putchar('n');
            else if (T[j]=='t') putchar('w');
            else if (T[j]=='u') putchar('j');
            else if (T[j]=='v') putchar('p');
            else if (T[j]=='w') putchar('f');
            else if (T[j]=='x') putchar('m');
            else if (T[j]=='y') putchar('a');
            else if (T[j]=='z') putchar('q');
            else putchar(T[j]);
        }
        putchar('\n');
    }
}

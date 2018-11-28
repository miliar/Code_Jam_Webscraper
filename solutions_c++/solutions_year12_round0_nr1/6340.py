// Wojciech Orzechowski
// 14.04.2012r.
// Google Coder Jam 2012 - Problem A

#include <iostream>
#include <string>
using namespace std;

char zamiana(char litera)
{
    if (litera==' ') return ' ';
    if (litera=='a') return 'y';
    if (litera=='b') return 'h';
    if (litera=='c') return 'e';
    if (litera=='d') return 's';
    if (litera=='e') return 'o';
    if (litera=='f') return 'c';
    if (litera=='g') return 'v';
    if (litera=='h') return 'x';
    if (litera=='i') return 'd';
    if (litera=='j') return 'u';
    if (litera=='k') return 'i';
    if (litera=='l') return 'g';
    if (litera=='m') return 'l';
    if (litera=='n') return 'b';
    if (litera=='o') return 'k';
    if (litera=='p') return 'r';
    if (litera=='r') return 't';
    if (litera=='s') return 'n';
    if (litera=='t') return 'w';
    if (litera=='u') return 'j';
    if (litera=='v') return 'p';
    if (litera=='w') return 'f';
    if (litera=='x') return 'm';
    if (litera=='y') return 'a';
    if (litera=='q') return 'z';
    if (litera=='z') return 'q';
}

string dekoduj(string s)
{
    int lg=s.length();
    for (int i=0; i<lg; i++) s[i]=zamiana(s[i]);
    return s;
}

int main()
{
    ios_base::sync_with_stdio(0);
    int n,i=1;
    string s;
    cin >> n;
    cin.ignore();
    while (n>0)
    {
        getline(cin,s);
        cout << "Case #" << i++ << ": " << dekoduj(s) << "\n";
        n--;
    }
    return 0;
}

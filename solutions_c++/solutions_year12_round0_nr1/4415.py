#include <iostream>
#include <stdio.h>
#include <string.h>

using namespace std;
char jomle[200];
char encode(char a);
void print(char j[200],int e);
void restart();
int main()
{
    int T,i;
    cin >> T;
    for(i = 0 ; i <= T ; i++)
    {
        gets(jomle);
        print(jomle,i);
        restart();
    }
    return 0;
}
void restart()
{
    int i;
    for(i = 0 ; i < 200 ;i++)jomle[i] =NULL;
}
void print(char j[200],int e)
{
    int tol,i;
    tol = strlen(j);
    if(e != 0)
    cout <<"Case #"<<e<<": ";
    for(i = 0 ; i < tol; i++)
    {
         cout << encode(j[i]);
    }
    if(e != 0)
    cout <<"\n";
}
char encode(char a)
{
switch(a)
{
    case(' '):
    return ' ';
    break;
    case('a'):
    return'y';
    break;
    case('b'):
    return'h';
    break;
    case('c'):
    return'e';
    break;
    case('d'):
    return's';
    break;
    case('e'):
    return'o';
    break;
    case('f'):
    return'c';
    break;
    case('g'):
    return'v';
    break;
    case('h'):
    return'x';
    break;
    case('i'):
    return'd';
    break;
    case('j'):
    return'u';
    break;
    case('k'):
    return'i';
    break;
    case('l'):
    return'g';
    break;
    case('m'):
    return'l';
    break;
    case('n'):
    return'b';
    break;
    case('o'):
    return'k';
    break;
    case('p'):
    return'r';
    break;
    case('q'):
    return'z';
    break;
    case('r'):
    return't';
    break;
    case('s'):
    return'n';
    break;
    case('t'):
    return'w';
    break;
    case('u'):
    return'j';
    break;
    case('v'):
    return'p';
    break;
    case('w'):
    return'f';
    break;
    case('x'):
    return'm';
    break;
    case('y'):
    return'a';
    break;
    case('z'):
    return'q';
    break;
    return a;
}
}

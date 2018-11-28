#include <cmath>
#include <cstdio>
#include <iostream>

using namespace std;

const int SIZE = 200;


static char decode(char e);


void calculation(char input[SIZE])
{
    int i = 0;
    while(input[i] != '\0')
    {
        char d = decode(input[i]);
        if(d == 'X')
        {
            cout << "Failure while decoding: " << d;
            throw 10;
        }
        else
        {
            cout << d;
        }

        i++;
    }
}

char decode(char e)
{
    switch(e)
    {
        case 'a':
            return 'y';
        case 'b':
            return 'h';
        case 'c':
            return 'e';
        case 'd':
            return 's';
        case 'e':
            return 'o';
        case 'f':
            return 'c';
        case 'g':
            return 'v';
        case 'h':
            return 'x';
        case 'i':
            return 'd';
        case 'j':
            return 'u';
        case 'k':
            return 'i';
        case 'l':
            return 'g';
        case 'm':
            return 'l';
        case 'n':
            return 'b';
        case 'o':
            return 'k';
        case 'p':
            return 'r';
        case 'q':
            return 'z';
        case 'r':
            return 't';
        case 's':
            return 'n';
        case 't':
            return 'w';
        case 'u':
            return 'j';
        case 'v':
            return 'p';
        case 'w':
            return 'f';
        case 'x':
            return 'm';
        case 'y':
            return 'a';
        case 'z':
            return 'q';
        case ' ':
            return ' ';
        
        default:
            return 'X';
    }
}


int main()
{
    int cases;

    cin >> cases;
    
    char line[SIZE];
    cin.getline(line, SIZE);
    
    for(int i=0; i<cases; i++)
    {
        printf("Case #%d: ", i+1);
        
        cin.getline(line, SIZE);
        
        calculation(line);
        
        cout << endl;
    }

    return 0;
}


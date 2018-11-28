#include <iostream>
#include <fstream>
#include <string>

#include <stdio.h>
#include <stdlib.h>
#define LINE_SIZE 120
#define LINE_NUM 40

using namespace std;

char translate(char g)
{
    char engChar;
    switch (g) {
        case 'a':
            engChar = 'y';
            break;
        case 'b':
            engChar = 'h';
            break;
        case 'c':
            engChar = 'e';
            break;
        case 'd':
            engChar = 's';
            break;
        case 'e':
            engChar = 'o';
            break;
        case 'f':
            engChar = 'c';
            break;
        case 'g':
            engChar = 'v';
            break;
        case 'h':
            engChar = 'x';
            break;
        case 'i':
            engChar = 'd';
            break;
        case 'j':
            engChar = 'u';
            break;
        case 'k':
            engChar = 'i';
            break;
        case 'l':
            engChar = 'g';
            break;
        case 'm':
            engChar = 'l';
            break;
        case 'n':
            engChar = 'b';
            break;
        case 'o':
            engChar = 'k';
            break;
        case 'p':
            engChar = 'r';
            break;
        case 'q':
            engChar = 'z';
            break;
        case 'r':
            engChar = 't';
            break;
        case 's':
            engChar = 'n';
            break;
        case 't':
            engChar = 'w';
            break;
        case 'u':
            engChar = 'j';
            break;
        case 'v':
            engChar = 'p';
            break;
        case 'w':
            engChar = 'f';
            break;
        case 'x':
            engChar = 'm';
            break;
        case 'y':
            engChar = 'a';
            break;
        case 'z':
            engChar = 'q';
            break;
        default:
            engChar = g;
            break;
    }
    return engChar;
}

int main () {
    char line[LINE_NUM][LINE_SIZE];
    char engline[LINE_NUM][LINE_SIZE];
    int lineNum;
    char buffer [50];
    int i = 0;
    ifstream inFile ("in.txt");
    ofstream outFile ("out.txt");
    
    if (inFile.is_open())
    {
        while (inFile.good())
        {
            inFile.getline (line[i],LINE_SIZE);
            cout << line[i] << endl;
            i++;
        }
        lineNum =  atoi(line[0]);
        inFile.close();
    }
    else cout << "Unable to open file"; 
    
    
    for (int j=1; j<=lineNum; j++) {
        int len = snprintf(engline[j], LINE_SIZE, "Case #%d: ", j);
        printf("this string has length %d\n", len);
        for (int k=0; k<LINE_SIZE; k++) {
            engline[j][k+len] = translate(line[j][k]);
        }
        outFile << engline[j] << endl;
    }    
    outFile.close();
    cout << "Done!\n";
    
    return 0;
}

#include<iostream>
#include<fstream>
#include<string>
using namespace std;
int main()
{
    fstream in("A-small-attempt0.in");
    fstream out("output.txt");
    string input,output;
    int cases;
    in>>cases;in.ignore();
    for(int b=1; b<=cases; b++)
    {
        getline(in,input);
        for(int a=0; a<input.length(); a++)
        {
            switch(input[a])
            {
            case ' ':
                output.push_back(' ');
                break;
            case 'a':
                output.push_back('y');
                break;
            case 'b':
                output.push_back('h');
                break;
            case 'c':
                output.push_back('e');
                break;
            case 'd':
                output.push_back('s');
                break;
            case 'e':
                output.push_back('o');
                break;
            case 'f':
                output.push_back('c');
                break;
            case 'g':
                output.push_back('v');
                break;
            case 'h':
                output.push_back('x');
                break;
            case 'i':
                output.push_back('d');
                break;
            case 'j':
                output.push_back('u');
                break;
            case 'k':
                output.push_back('i');
                break;
            case 'l':
                output.push_back('g');
                break;
            case 'm':
                output.push_back('l');
                break;
            case 'n':
                output.push_back('b');
                break;
            case 'o':
                output.push_back('k');
                break;
            case 'p':
                output.push_back('r');
                break;
            case 'q':
                output.push_back('z');
                break;
            case 'r':
                output.push_back('t');
                break;
            case 's':
                output.push_back('n');
                break;
            case 't':
                output.push_back('w');
                break;
            case 'u':
                output.push_back('j');
                break;
            case 'v':
                output.push_back('p');
                break;
            case 'w':
                output.push_back('f');
                break;
            case 'x':
                output.push_back('m');
                break;
            case 'y':
                output.push_back('a');
                break;
            case 'z':
                output.push_back('q');
                break;
            }
        }
        out<<"Case #"<<b<<": "<<output<<endl;
        output.resize(0);
        input.resize(0);
    }
}

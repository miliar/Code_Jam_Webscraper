#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <string>
#include <sstream>
#include <fstream>

using namespace std;

int T;

int main(int argc, char **argv)
{
    string fname;
    if(argc > 1)
        fname = string(argv[1]);
    else {
        cout << "File Name: ";
        cin >> fname;
    }

    ifstream in;
    in.open(fname.c_str(), ifstream::in);

    if(in.fail()) {
        cout << "Error";
        cin.get();
        exit(-1);
    }

    string input;
    getline(in, input);
    stringstream(input) >> T;
    ofstream fout("output.out");

    for(int i = 0; i < T; i++) {
        string line;
        getline(in, line);
        for(int j = 0; j < line.size(); j++) {
            char c = line[j];
            switch(c) {
            case 'a':
                line[j] = 'y';
                break;
            case 'b':
                line[j] = 'h';
                break;
            case 'c':
                line[j] = 'e';
                break;
            case 'd':
                line[j] = 's';
                break;
            case 'e':
                line[j] = 'o';
                break;
            case 'f':
                line[j] = 'c';
                break;
            case 'g':
                line[j] = 'v';
                break;
            case 'h':
                line[j] = 'x';
                break;
            case 'i':
                line[j] = 'd';
                break;
            case 'j':
                line[j] = 'u';
                break;
            case 'k':
                line[j] = 'i';
                break;
            case 'l':
                line[j] = 'g';
                break;
            case 'm':
                line[j] = 'l';
                break;
            case 'n':
                line[j] = 'b';
                break;
            case 'o':
                line[j] = 'k';
                break;
            case 'p':
                line[j] = 'r';
                break;
            case 'q':
                line[j] = 'z';
                break;
            case 'r':
                line[j] = 't';
                break;
            case 's':
                line[j] = 'n';
                break;
            case 't':
                line[j] = 'w';
                break;
            case 'u':
                line[j] = 'j';
                break;
            case 'v':
                line[j] = 'p';
                break;
            case 'w':
                line[j] = 'f';
                break;
            case 'x':
                line[j] = 'm';
                break;
            case 'y':
                line[j] = 'a';
                break;
            case 'z':
                line[j] = 'q';
                break;
            default:
                break;
            }
        }
        
        string output;
		stringstream ss;
		ss << "Case #" << i+1 << ": " << line;
		output = ss.str();
		cout << output;
		fout << output;
		if(i != T-1) {
			cout << endl;
			fout << endl;
		}
    }

    cin.ignore(100, '\n');
    cin.get();
    
    return 0;
}

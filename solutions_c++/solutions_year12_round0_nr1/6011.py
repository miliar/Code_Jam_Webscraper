#include <stdlib.h>
#include <iostream>
#include <fstream>
#include <string>
using namespace std;

string convert(string str_in) {
    for (int i = 0; i < str_in.length(); i++) {
        switch (str_in[i]) {
            case 'a':
                str_in[i] = 'y';
                break;
            case 'b':
                str_in[i] = 'h';
                break;
            case 'c':
                str_in[i] = 'e';
                break;
            case 'd':
                str_in[i] = 's';
                break;
            case 'e':
                str_in[i] = 'o';
                break;
            case 'f':
                str_in[i] = 'c';
                break;
            case 'g':
                str_in[i] = 'v';
                break;
            case 'h':
                str_in[i] = 'x';
                break;
            case 'i':
                str_in[i] = 'd';
                break;
            case 'j':
                str_in[i] = 'u';
                break;
            case 'k':
                str_in[i] = 'i';
                break;
            case 'l':
                str_in[i] = 'g';
                break;
            case 'm':
                str_in[i] = 'l';
                break;
            case 'n':
                str_in[i] = 'b';
                break;
            case 'o':
                str_in[i] = 'k';
                break;
            case 'p':
                str_in[i] = 'r';
                break;
            case 'q':
                str_in[i] = 'z';
                break;
            case 'r':
                str_in[i] = 't';
                break;
            case 's':
                str_in[i] = 'n';
                break;
            case 't':
                str_in[i] = 'w';
                break;
            case 'u':
                str_in[i] = 'j';
                break;
            case 'v':
                str_in[i] = 'p';
                break;
            case 'w':
                str_in[i] = 'f';
                break;
            case 'x':
                str_in[i] = 'm';
                break;
            case 'y':
                str_in[i] = 'a';
                break;
            case 'z':
                str_in[i] = 'q';
                break;
        }
    }

    return str_in;
}

int main(int argc, char** argv) {

    ifstream infile("A-small-attempt2.in");
    ofstream outfile("Output.in");
    string line;
    int count = 0, lines = 0;

    if (infile.is_open()) {
        while (infile.good()) {
            getline(infile, line);
            if (count == 0) {
                lines = atoi(line.c_str());
            } else if (lines >= count) {
                line = convert(line);
                outfile << "Case #" << count << ": " << line << endl;
            }
            count++;
        }
        outfile.close();
        infile.close();
    } else cout << "Unable to open file";

    return (EXIT_SUCCESS);
}
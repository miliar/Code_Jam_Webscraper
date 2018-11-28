#include <iostream>
#include <fstream>
#include <string>
#include <stdio.h>
#include <stdlib.h>
#include <sstream>

using namespace std;

int main(){
    ifstream problemFile;
    ofstream resultFile;
    string line;
    int cases;

    problemFile.open("A-small-attempt0.in");
    getline(problemFile, line);
    cases = atoi(line.c_str());

    resultFile.open ("result.txt");

    for(int i = 1; i < cases+1; i++){
        getline(problemFile, line);
        cout << line << endl;
        stringstream sstream;

        sstream << "Case #" << i << ": ";

        for (int i = 0; i < line.length(); ++i) {
            //cout << line.at(i) << endl;
            if (line.at(i) == ' ') sstream << ' ';
            else if(line.at(i) == 'a') sstream << 'y';
            else if(line.at(i) == 'b') sstream << 'h';
            else if(line.at(i) == 'c') sstream << 'e';
            else if(line.at(i) == 'd') sstream << 's';
            else if(line.at(i) == 'e') sstream << 'o';
            else if(line.at(i) == 'f') sstream << 'c';
            else if(line.at(i) == 'g') sstream << 'v';
            else if(line.at(i) == 'h') sstream << 'x';
            else if(line.at(i) == 'i') sstream << 'd';
            else if(line.at(i) == 'j') sstream << 'u';
            else if(line.at(i) == 'k') sstream << 'i';
            else if(line.at(i) == 'l') sstream << 'g';
            else if(line.at(i) == 'm') sstream << 'l';
            else if(line.at(i) == 'n') sstream << 'b';
            else if(line.at(i) == 'o') sstream << 'k';
            else if(line.at(i) == 'p') sstream << 'r';
            else if(line.at(i) == 'q') sstream << 'z';
            else if(line.at(i) == 'r') sstream << 't';
            else if(line.at(i) == 's') sstream << 'n';
            else if(line.at(i) == 't') sstream << 'w';
            else if(line.at(i) == 'u') sstream << 'j';
            else if(line.at(i) == 'v') sstream << 'p';
            else if(line.at(i) == 'w') sstream << 'f';
            else if(line.at(i) == 'x') sstream << 'm';
            else if(line.at(i) == 'y') sstream << 'a';
            else if(line.at(i) == 'z') sstream << 'q';
        }

        resultFile << sstream.str() << endl;
    }

    resultFile.close();
    problemFile.close();

    return 0;
}


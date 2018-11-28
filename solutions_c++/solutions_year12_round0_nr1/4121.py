#include <iostream>
#include <fstream>
#include <cstring>
using namespace std;
char decode(char i) {
    switch(i) {
        case 'y': return 'a';
        case 'n': return 'b';
        case 'i': return 'd';
        case 'c': return 'e';
        case 'w': return 'f';
        case 'l': return 'g';
        case 'k': return 'i';
        case 'o': return 'k';
        case 'm': return 'l';
        case 'x': return 'm';
        case 's': return 'n';
        case 'e': return 'o';
        case 'v': return 'p';
        case 'p': return 'r';
        case 'd': return 's';
        case 'r': return 't';
        case 'j': return 'u';
        case 'g': return 'v';
        case 't': return 'w';
        case 'h': return 'x';
        case 'a': return 'y';
        case 'q': return 'z';
        case 'b': return 'h';
        case 'f': return 'c';
        case 'u': return 'j';
        case 'z': return 'q';
        default: return ' ';
        
    }
}
int main() {
    
    ifstream infile("A-small-attempt0.in",ios::in);
    ofstream outfile("result.txt",ios::out);
    
    if(!infile.is_open()) {
        return -1;
    }
    else {
        int numcase;
        string casetext = "";
        string numcasrString = "";
        getline(infile,numcasrString);
        const char* Ptr = numcasrString.c_str();
        numcase = atoi(Ptr);
        for(int i=0; i<numcase; i++) {
            getline(infile,casetext);
            for(int j=0; casetext[j]!='\0'; j++) {
                casetext[j] = decode(casetext[j]);
            }
            outfile << "Case #" << i+1 << ": " << casetext + "\n";
        }
    }

    return 0;
}



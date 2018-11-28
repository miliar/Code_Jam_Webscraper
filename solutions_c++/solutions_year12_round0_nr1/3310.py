#include <iostream>
#include <fstream>
#include <stdlib.h>

using namespace std;

int main(int argc, char** argv){
    ifstream inFile(argv[1]);
    ofstream outFile(argv[2]);
    
    const char m[27] = {"yhesocvxduiglbkrztnwjpfmaq"};
    
    int line;
    inFile >> line;
    cout << line;
    
    char temp[3];
    inFile.getline(temp,3);
    
    for(int i = 0 ; i < line ; i++){
        char text[200];
        inFile.getline(text,200);
        cout << text << endl;
        for(int j = 0 ; j < 100 ; j++){
            if(text[j] <= 'z' && text[j] >= 'a')
                text[j] = m[text[j] - 'a'];
            else if(text[j] <= 'Z' && text[j] >= 'A')
                text[j] = m[text[j] - 'a' + ('A' - 'a')];
        }
        outFile << "Case #" << i+1 << ": "<< text << endl;
    }
}

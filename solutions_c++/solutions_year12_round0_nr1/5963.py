#include <iostream>
#include <fstream>
#include <string>

using namespace std;

char changeLetter(char sub){
    if(sub == 'a'){
        return 'y';
    }
    if(sub == 'b'){
        return 'h';
    }
    if(sub == 'c'){
        return 'e';
    }
    if(sub == 'd'){
        return 's';
    }
    if(sub == 'e'){
        return 'o';
    }
    if(sub == 'f'){
        return 'c';
    }
    if(sub == 'g'){
        return 'v';
    }
    if(sub == 'h'){
        return 'x';
    }
    if(sub == 'i'){
        return 'd';
    }
    if(sub == 'j'){
        return 'u';
    }
    if(sub == 'k'){
        return 'i';
    }
    if(sub == 'l'){
        return 'g';
    }
    if(sub == 'm'){
        return 'l';
    }
    if(sub == 'n'){
        return 'b';
    }
    if(sub == 'o'){
        return 'k';
    }
    if(sub == 'p'){
        return 'r';
    }
    if(sub == 'q'){
        return 'z';
    }
    if(sub == 'r'){
        return 't';
    }
    if(sub == 's'){
        return 'n';
    }
    if(sub == 't'){
        return 'w';
    }
    if(sub == 'u'){
        return 'j';
    }
    if(sub == 'v'){
        return 'p';
    }
    if(sub == 'w'){
        return 'f';
    }
    if(sub == 'x'){
        return 'm';
    }
    if(sub == 'y'){
        return 'a';
    }
    if(sub == 'z'){
        return 'q';
    }
    if(sub == ' '){
        return ' ';
    }
}

int main()
{
    ifstream file;
    file.open ("A-small-attempt2.in");
    int caseNumber = 0;
    file>>caseNumber;
    string output[caseNumber+1];
    string temp;
    string output2[caseNumber+1];

    for(int i = 0; i < caseNumber+1; i++){
        getline(file,output[i]);
    }
    file.close();

    for(int i = 0; i < caseNumber+1; i++){
            string tempString = output[i];
            int k = 0;
            for(int k = 0; k < tempString.size(); k++){
                output2[i]+=changeLetter(tempString[k]);
            }
    }

    ofstream file2;
    file2.open("output.in");
    for(int i = 1; i < caseNumber+1; i++){
    file2 << "Case #" << i << ": " << output2[i] << endl;
    }

    return 0;
}


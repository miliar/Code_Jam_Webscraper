#include<iostream>
#include<string>
using namespace std;
int main() {
    int t;
    string line;
    cin >> t;
    for(int j=1; j<=t+1; j++) {

        getline (cin,line);
        if(j>1) cout << "Case #" << j-1 << ": ";
        for(int i=0; i<line.size(); i++) {
            if(int(line[i])==32) cout << " ";
            if(line[i]=='a') cout << "y";
            else if(line[i]=='b') cout << "h";
            else if(line[i]=='c') cout << "e";
            else if(line[i]=='d') cout << "s";
            else if(line[i]=='e') cout << "o";
            else if(line[i]=='f') cout << "c";
            else if(line[i]=='g') cout << "v";
            else if(line[i]=='h') cout << "x";
            else if(line[i]=='i') cout << "d";
            else if(line[i]=='j') cout << "u";
            else if(line[i]=='k') cout << "i";
            else if(line[i]=='l') cout << "g";
            else if(line[i]=='m') cout << "l";
            else if(line[i]=='n') cout << "b";
            else if(line[i]=='o') cout << "k";
            else if(line[i]=='p') cout << "r";
            else if(line[i]=='q') cout << "z";
            else if(line[i]=='r') cout << "t";
            else if(line[i]=='s') cout << "n";
            else if(line[i]=='t') cout << "w";
            else if(line[i]=='u') cout << "j";
            else if(line[i]=='v') cout << "p";
            else if(line[i]=='w') cout << "f";
            else if(line[i]=='x') cout << "m";
            else if(line[i]=='y') cout << "a";
            else if(line[i]=='z') cout << "q";
        }
        if(j>1) cout << endl;
    }
    return 0;
}

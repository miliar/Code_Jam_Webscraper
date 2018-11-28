#include <iostream>
#include <string>

using namespace std;

int main()
{
    int a;
    cin >> a;
    string syf;
    getline(cin,syf);
    for (int i=1;i<=a;i++){
        string input;
        getline(cin,input);
        string output=input;
        for (int j=0;j<input.length();j++){
            if (input[j]=='a') output[j]='y';
            else if (input[j]=='b') output[j]='h';
            else if (input[j]=='c') output[j]='e';
            else if (input[j]=='d') output[j]='s';
            else if (input[j]=='e') output[j]='o';
            else if (input[j]=='f') output[j]='c';
            else if (input[j]=='g') output[j]='v';
            else if (input[j]=='h') output[j]='x';
            else if (input[j]=='i') output[j]='d';
            else if (input[j]=='j') output[j]='u';
            else if (input[j]=='k') output[j]='i';
            else if (input[j]=='l') output[j]='g';
            else if (input[j]=='m') output[j]='l';
            else if (input[j]=='n') output[j]='b';
            else if (input[j]=='o') output[j]='k';
            else if (input[j]=='p') output[j]='r';
            else if (input[j]=='q') output[j]='z';
            else if (input[j]=='r') output[j]='t';
            else if (input[j]=='s') output[j]='n';
            else if (input[j]=='t') output[j]='w';
            else if (input[j]=='u') output[j]='j';
            else if (input[j]=='v') output[j]='p';
            else if (input[j]=='w') output[j]='f';
            else if (input[j]=='x') output[j]='m';
            else if (input[j]=='y') output[j]='a';
            else if (input[j]=='z') output[j]='q';


        }
        cout << "Case #" << i << ": " << output << "\n";

    }

    return 0;
}

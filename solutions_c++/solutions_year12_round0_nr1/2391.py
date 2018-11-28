#include <iostream>

using namespace std;

char convert(char c){
    switch(c){
        case ' ':
            return ' ';
        case 'a':
            return 'y';
        case 'b':
            return 'h';
        case 'c':
            return 'e';
        case 'd':
            return 's';
        case 'e':
            return 'o';
        case 'f':
            return 'c';
        case 'g':
            return 'v';
        case 'h':
            return 'x';
        case 'i':
            return 'd';
        case 'j':
            return 'u';
        case 'k':
            return 'i';
        case 'l':
            return 'g';
        case 'm':
            return 'l';
        case 'n':
            return 'b';
        case 'o':
            return 'k';
        case 'p':
            return 'r';
        case 'q':
            return 'z';
        case 'r':
            return 't';
        case 's':
            return 'n';
        case 't':
            return 'w';
        case 'u':
            return 'j';
        case 'v':
            return 'p';
        case 'w':
            return 'f';
        case 'x':
            return 'm';
        case 'y':
            return 'a';
        case 'z':
            return 'q';
        default:
            return '$';
    }
}

int main(){
    int T;
    string input;
    cin >> T;
    for(int i=0; i<T;i++){
        //cout << "Case #" << i+1 << ":";
        int a = 0;
        while (std::getline(cin, input)) {
            if(input != ""){
                cout << "Case #" << a << ": ";
                //std::cout << "> " << input << std::endl;
                int len = input.length();
                for(int j=0; j<len;j++){
                    cout << convert(input[j]);
                }
                cout << endl;
            }
            a++;
        }
    }
}

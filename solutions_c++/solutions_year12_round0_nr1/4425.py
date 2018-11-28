#include<iostream>
#include<string>
using namespace std;

string translate(string s){
    string output;
    char c;
    int i=0;
    while(s[i]){
        switch(s[i]){
            case 'a':
                c='y';
                break;
            case 'b':
                c='h';
                break;
            case 'c':
                c='e';
                break;
            case 'd':
                c='s';
                break;
            case 'e':
                c='o';
                break;
            case 'f':
                c='c';
                break;
            case 'g':
                c='v';
                break;
            case 'h':
                c='x';
                break;
            case 'i':
                c='d';
                break;
             case 'j':
                c='u';
                break;
             case 'k':
                c='i';
                break;
             case 'l':
                c='g';
                break;
             case 'm':
                c='l';
                break;
             case 'n':
                c='b';
                break;
             case 'o':
                c='k';
                break;
             case 'p':
                c='r';
                break;
             case 'q':
                c='z';
                break;
             case 'r':
                c='t';
                break;
             case 's':
                c='n';
                break;
             case 't':
                c='w';
                break;
            case 'u':
                c='j';
                break;
            case 'v':
                c='p';
                break;
            case 'w':
                c='f';
                break;
            case 'x':
                c='m';
                break;
            case 'y':
                c='a';
                break;
            case 'z':
                c='q';
                break;
            default:
                c=s[i];
        }
        output+=c;
        ++i;
    }

    return output;
}


int main(){
    int n;
    string str;
    cin >> n;
    cin.ignore();
    for(int i=1; i<=n; i++){
        getline(cin, str);
        cout << "Case #" << i << ": " << translate(str) << endl;
    }


}

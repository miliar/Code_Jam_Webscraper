#include <iostream>
#include <string>

using namespace std;

string translate(string cases);

int main(int argc, char * argv) {
    int T;
    string cases;
    
    cin >> T;
    
    getline(cin, cases);
    
    for(int i = 0; i < T; i++) {
        getline(cin, cases);
        
        cout << "Case #" << i+1 << ": " << translate(cases) << endl;
    }
    
    return 0;
}

string translate(string cases) {
    string str;
    
    for(int i = 0; i < cases.length(); i++) {
        switch(cases[i]) {
            case 'y': str += "a"; break;
            case 'n': str += "b"; break;
            case 'f': str += "c"; break;
            case 'i': str += "d"; break;
            case 'c': str += "e"; break;
            case 'w': str += "f"; break;
            case 'l': str += "g"; break;
            case 'b': str += "h"; break;
            case 'k': str += "i"; break;
            case 'u': str += "j"; break;
            case 'o': str += "k"; break;
            case 'm': str += "l"; break;
            case 'x': str += "m"; break;
            case 's': str += "n"; break;
            case 'e': str += "o"; break;
            case 'v': str += "p"; break;
            case 'z': str += "q"; break;
            case 'p': str += "r"; break;
            case 'd': str += "s"; break;
            case 'r': str += "t"; break;
            case 'j': str += "u"; break;
            case 'g': str += "v"; break;
            case 't': str += "w"; break;
            case 'h': str += "x"; break;
            case 'a': str += "y"; break;
            case 'q': str += "z"; break;
            case ' ': str += " "; break;
        }
    }
    
    return str;
}
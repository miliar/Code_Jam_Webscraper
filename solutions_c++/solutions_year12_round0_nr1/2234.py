#include <iostream>

using namespace std;

char replace(char c) {
    switch(c) {
        case 'a': return 'y'; break;
        case 'b': return 'h'; break;
        case 'c': return 'e'; break;
        case 'd': return 's'; break;
        case 'e': return 'o'; break;
        case 'f': return 'c'; break;
        case 'g': return 'v'; break;
        case 'h': return 'x'; break;
        case 'i': return 'd'; break;
        case 'j': return 'u'; break;
        case 'k': return 'i'; break;
        case 'l': return 'g'; break;
        case 'm': return 'l'; break;
        case 'n': return 'b'; break;
        case 'o': return 'k'; break;
        case 'p': return 'r'; break;
        case 'q': return 'z'; break;
        case 'r': return 't'; break;
        case 's': return 'n'; break;
        case 't': return 'w'; break;
        case 'u': return 'j'; break;
        case 'v': return 'p'; break;
        case 'w': return 'f'; break;
        case 'x': return 'm'; break;
        case 'y': return 'a'; break;
        case 'z': return 'q'; break;
        default: return c;
    }
}

string translate(string s) {
    string t;
    for (int i = 0; i < (int)s.length(); i++) {
        t.push_back(replace(s[i]));
    }
    return t;
}

int main() {
    int n;
    cin >> n;
    cin.ignore(10, '\n');
    for (int i = 1; i <= n; i++) {
        string s; getline(cin, s);
        cout << "Case #" << i << ": " << translate(s) << "\n";
    }
}

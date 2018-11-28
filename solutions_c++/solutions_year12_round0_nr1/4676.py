#include <string>
#include <iostream>
using namespace std;


char code[] = { 'y', 'h', 'e', 's', 'o', 'c',
                'v', 'x', 'd', 'u', 'i', 'g',
                'l', 'b', 'k', 'r', 'z', 't', 
                'n', 'w', 'j', 'p', 'f', 'm', 'a', 'q' };

int main () {
    int linesno;
    cin >> linesno; 
    string line;
    getline ( cin, line ) ;
    for (int i = 1; i<=linesno; i++) {
        getline ( cin, line ) ;
        cout << "Case #" << i << ": ";
        for (int j = 0; j<line.size(); j++)
            cout <<  (line[j]==' ' ? ' ' : code [(int) line[j] - (int)'a' ] );
        cout << '\n';
    }
}


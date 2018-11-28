#include <iostream>
#include <fstream>
#include <string>
#include <stdlib.h>
#include <map>

using namespace std;

int main (int argc, char * argv[]) {
    ifstream is(&argv[1][0]);
    string line;
    int cases;
    map<char,char> alphabet;
    map<char,bool> usedLetters;
    //init
    for (char c = 'a'; c <= 'z'; c++) {
        alphabet[c] = '0';
        usedLetters[c] = false;
    }
    alphabet['a'] = 'y';
    usedLetters['y'] = true;
    alphabet['o'] = 'e';
    usedLetters['e'] = true;
    alphabet['z'] = 'q';
    usedLetters['q'] = true;
    string normal = "our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up";
    string coded = "ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv";
    for (int i = 0; i < normal.length(); i++) {
        if (normal[i] == ' ')
            continue;
        if (alphabet[normal[i]] != '0' && alphabet[normal[i]] != coded[i])
            cout << alphabet[normal[i]] << " " << coded[i] << "mismatch in encoding!\n";
        else
            alphabet[normal[i]] = coded[i];
        usedLetters[coded[i]] = true;
    }

    //assume only one unused can left
    char unused = '0';
    for (map<char,bool>::iterator it = usedLetters.begin(); it != usedLetters.end(); ++it) {
        if (it->second == 0) {
            unused = it->first;
            break;
        }
    }
    
    for (map<char,char>::iterator it = alphabet.begin(); it != alphabet.end(); ++it) {
        if (it->second == '0') {
            it->second = unused;
        }        
    }

    map<char,char> alphabetiEncoded;
    for (map<char,char>::iterator it = alphabet.begin(); it != alphabet.end(); ++it) {
        if (it->second == '0')
            cout << it->first << " not decoded\n";
        else
            alphabetiEncoded[it->second] = it->first;
    }

    if (is.is_open()) {
        if (is.good()) { 
            getline(is, line);
            cases = atoi(line.c_str());
        }
        for (int caseCounter = 0; caseCounter < cases; caseCounter++) {
            getline(is, line);
            cout << "Case #" << caseCounter+1 << ": ";
            for (int i = 0; i < line.length(); i++) {
                if (line[i] == ' ')
                    cout << " ";
                else
                    cout << alphabetiEncoded[line[i]];
            }
            cout << endl;
        }
        is.close();
        return 0;
    }
    return -1;    
}

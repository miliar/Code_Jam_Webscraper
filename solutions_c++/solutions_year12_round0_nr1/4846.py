#include <iostream>
#include <stdio.h>
#include <map>

using namespace std;

void transTable();
void output(int i, char *s);
char tTable[26] = {'y', 'n', 'f', 'i', 'c', 'w', 'l', 'b', 'k', 'u', 'o', 'm', 'x', 's', 'e', 'v', 'z', 'p', 'd', 'r', 'j', 'g', 't', 'h', 'a', 'q'};
int main()
{
    freopen("A-small-attempt1.in", "r", stdin);
    freopen("out.txt", "w", stdout);

    int T;  //number of test cases
    cin >> T;
    char s[200];
    cin.getline(s, 200);  //garbage

    //print translated string
    for (int i = 1; i<=T; i++){
        cin.getline(s, 200);
        output(i, s);
    }

    return 0;
}

void output(int caseNum, char *s){
    cout << "Case #" << caseNum << ": ";

    while (*s != '\0'){
        for (int j = 0; j < 26; j++){
            if (*s == ' '){
                cout << ' ';
                break;
            }
            if (tTable[j] == *s){
                cout << char(j+'a');
                break;
            }
        }
        s++;
    }

    cout << endl;
}

void transTable(){


//    m.insert(make_pair("a", "y"));
//    m.insert(make_pair("b", "n"));
//    m.insert(make_pair("c", "f"));
//    m.insert(make_pair("d", "i"));
//    m.insert(make_pair("e", "c"));
//    m.insert(make_pair("f", "w"));
//    m.insert(make_pair("g", "l"));
//    m.insert(make_pair("h", "b"));
//    m.insert(make_pair("i", "k"));
//    m.insert(make_pair("j", "u"));
//    m.insert(make_pair("k", "o"));
//    m.insert(make_pair("l", "m"));
//    m.insert(make_pair("m", "x"));
//    m.insert(make_pair("n", "s"));
//    m.insert(make_pair("o", "e"));
//    m.insert(make_pair("p", "v"));
//    m.insert(make_pair("q", "z"));
//    m.insert(make_pair("r", "p"));
//    m.insert(make_pair("s", "d"));
//    m.insert(make_pair("t", "r"));
//    m.insert(make_pair("u", "j"));
//    m.insert(make_pair("v", "g"));
//    m.insert(make_pair("w", "t"));
//    m.insert(make_pair("x", "h"));
//    m.insert(make_pair("y", "a"));
//    m.insert(make_pair("z", "q"));
}

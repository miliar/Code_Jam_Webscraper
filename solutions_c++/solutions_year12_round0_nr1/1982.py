#include <fstream>
#include <map>
#include <string>

using namespace std;

map <char, char> dictionary;

void fillMap(char sentence[], char meaning[]) {
    for(int i = 0; sentence[i] != '\0'; i++) {
        char l = sentence[i];
        char ll = meaning[i];
        if (dictionary.count(l) == 0) {
            dictionary.insert(pair <char, char> (l, ll));
        }
    }
}

string translate (string sentence) {
    string answ;
    int l = sentence.length();
    for (int i = 0; i < l; i++) {
        answ += dictionary[sentence[i]];
    }
    return answ;
}

int main () {
    fillMap("ejp mysljylc kd kxveddknmc re jsicpdrysi",
            "our language is impossible to understand");

    fillMap("rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd",
            "there are twenty six factorial possibilities");

    fillMap("de kr kd eoya kw aej tysr re ujdr lkgc jv",
            "so it is okay if you want to just give up");

    fillMap("zq",
            "qz");

//    map <char, char>::iterator it;
//    for (it = dictionary.begin(); it != dictionary.end(); it++) {
//        cout << it->first << " " << it->second << endl;
//    }

    int t;

    ifstream fd("input.txt");
    ofstream fr("output.txt");

    fd >> t;
    fd.ignore();
    for (int i = 1; i <= t; i++) {
        string sentence;
        getline(fd, sentence);
        //cout << "Readed: " << sentence << "|" << endl;
        fr << "Case #" << i << ": " << translate (sentence) << endl;
    }

    fd.close();
    fr.close();

    return 0;
}

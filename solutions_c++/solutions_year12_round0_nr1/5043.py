
#include <iostream>
#include <map>
#include <string.h>
#include <fstream>
#include <vector>

using namespace std;

string inputs[] = {"ejp mysljylc kd kxveddknmc re jsicpdrysi",
    "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd",
    "de kr kd eoya kw aej tysr re ujdr lkgc jv"};
string outputs[] = {
    "our language is impossible to understand",
    "there are twenty six factorial possibilities",
    "so it is okay if you want to just give up"};

map<char,char> table;

string translate(string input);

int main (int argc, const char * argv[])
{
    ifstream inputfile;
    inputfile.open("inputs.txt");
    int numinputs;
    inputfile >> numinputs;
    inputfile.ignore();
    vector<string> needstranslation;
    for(int i=0;i<numinputs;i++) {
        string temp;
        getline(inputfile, temp);
        needstranslation.push_back(temp);
    }

    for (int i=0;i<3;i++) {
        for (int j=0;j<inputs[i].length();j++) {
            if (table[inputs[i][j]] == NULL) {
                table[inputs[i][j]] = outputs[i][j];
            }
        }
    }
    table['z'] = 'q';
    table['q'] = 'z';
    //cout << "Determined: " << table.size() << endl;
    for (char i = 97;i<123;i++) {
        table[i-32] = table[i] - 32;
    }
    /*for (char i = 65;i<123;i++) {
        cout << i << "->" << table[i] << endl;
    }*/
    for (int i=0; i<needstranslation.size();i++) {
        cout << "Case #" << i+1 << ": " << translate(needstranslation[i]) << endl;
    }
    return 0;
}

string translate(string input) {
    string str;
    for (int i=0;i<input.length();i++) {
        str.push_back(table[input[i]]);
    }
    return str;
}

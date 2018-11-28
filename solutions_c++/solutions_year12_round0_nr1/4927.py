#include <iostream>
#include <map>
#include <string.h>
#include <fstream>

using namespace std;

int main()
{
    map<char,char> alphabet;

    char s[] =  "ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv";
    char ss[] = "our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up";

    for (int var = 0; var < strlen(s); var++) {
        alphabet[s[var]] = ss[var];
    }
    alphabet['q']='z';
    alphabet['z']='q';
    //    for (map<char,char>::iterator it=alphabet.begin();it!=alphabet.end();it++) {
    //        outFile<<it->first<<" -> " << it->second<<endl;
    //    }

    ifstream inFile;
    ofstream outFile;
    outFile.open("output.txt");
    inFile.open("input.in", ifstream::in);
    int n;
    inFile>> n;
    char text[200];
    inFile.getline(text,200);

    for (int var = 0; var < n; ++var) {
        inFile.getline(text,200);
        outFile<< "Case #"<<var+1<<": ";
        for (int count = 0; count < strlen(text); ++count) {
            outFile<<alphabet[text[count]];
        }
        outFile<<endl;
    }


    return 0;
}


#include <iostream>
#include <string>
#include <fstream>
#include <cstring>

using namespace std;

int main()
{
    // work out the code table from the sample and hint
    string s[4] = {"y qee", "ejp mysljylc kd kxveddknmc re jsicpdrysi",
                "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd", "de kr kd eoya kw aej tysr re ujdr lkgc jv"};
    string g[4] = {"a zoo", "our language is impossible to understand",
                "there are twenty six factorial possibilities", "so it is okay if you want to just give up"};
    const int N = 26;
    char CodeTable[N];
    memset(CodeTable, ' ', N);

    for(int i = 0; i < 4; i++) {
        for(int j = 0; j < s[i].length(); j++) {
            if(s[i].at(j) != ' ') {
                int key = s[i].at(j) - 'a';
                if(CodeTable[key] == ' ')
                    CodeTable[key] = g[i].at(j);
            }
        }
    }
    // fill the rest
    for(int i = 0; i < N; i++) {
        if(CodeTable[i] == ' ') {
            char c = 'a' + i;
            for(int j = 0; j < N; j++) {
                if(c == CodeTable[j])
                    CodeTable[i] = 'a' + j;
            }
        }
    }

    // Decode the input file
    ifstream fin("A-small-attempt1.in");
    ofstream fout("A-small-attempt1.out");
    if(!fin.is_open())
        cerr << "Failed to open input file" << endl;
    if(!fout.is_open())
        cerr << "Failed to open output file" << endl;
    int nSamples;
    fin >> nSamples;
    fin.get();
    string line;
    for(int i = 0; i < nSamples; i++) {
        getline(fin, line);
        for(int j = 0; j < line.length(); j++) {
            if(line.at(j) != ' ') {
                int key = line.at(j) - 'a';
                line.at(j) = CodeTable[key];
            }
        }
        fout << "Case #" << i+1 << ": " << line << endl;
    }

    return 0;
}


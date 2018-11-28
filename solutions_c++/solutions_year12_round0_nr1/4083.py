#include <fstream>
#include <iostream>
#include <cstring>
#include <string>

const char * googlerese = "yeq"
    "ejp mysljylc kd kxveddknmc re jsicpdrysi"
    "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd"
    "de kr kd eoya kw aej tysr re ujdr lkgc jv";

const char * english = "aoz"
    "our language is impossible to understand"
    "there are twenty six factorial possibilities"
    "so it is okay if you want to just give up";

char googlerese_table[26];
char english_table[26];

void BuildTable() {
    std::memset(googlerese_table, 0, 26);
    std::memset(english_table, 0, 26);
    int size = std::strlen(googlerese);
    for(int i=0; i<size; ++i) {
        if (googlerese[i]!=' ') {
            googlerese_table[googlerese[i]-'a'] = english[i];
            english_table[english[i]-'a'] = googlerese[i];
        }
    }

    googlerese_table['z'-'a'] = 'q';  // Only possibility left
    english_table['q'-'a'] = 'z';  // Only possibility left
}

void DisplayTable() {
    std::cout << "Unknown Googlerese:";
    for(int i=0; i<26; ++i) {
        if (googlerese_table[i]==0) {
            std::cout << ' ' << char('a'+i);
        }
    }
    std::cout << std::endl << "Unknown English:";
    for(int i=0; i<26; ++i) {
        if (english_table[i]==0) {
            std::cout << ' ' << char('a'+i);
        }
    }
    std::cout << std::endl << "Known Googlerese:";
    for(int i=0; i<26; ++i) {
        if (googlerese_table[i]!=0) {
            std::cout << ' ' << char('a'+i) << "->" << googlerese_table[i];
        }
    }
    std::cout << std::endl << "Known English:";
    for(int i=0; i<26; ++i) {
        if (english_table[i]!=0) {
            std::cout << ' ' << char('a'+i) << "->" << english_table[i];
        }
    }
    std::cout << std::endl;
}


int main(int argc, char *argv[])
{
    BuildTable();
    if (argc==1) {
        DisplayTable();
        return 0;
    }
    if (argc!=2) {
        std::cout<<"Error"<<std::endl;
        return 1;
    }
    std::ifstream input(argv[1]);
    std::string file_out = argv[1];
    file_out += ".out";
    std::ofstream output(file_out.c_str());
    int nb_case;
    input >> nb_case;
    std::string text;
    getline(input, text);
    if (!text.empty()) {
        std::cout<<"Error input"<<std::endl;
        return 1;
    }
    for(int i=0; i<nb_case; ++i) {
        getline(input, text);
        output<<"Case #"<<(i+1)<<": ";
        for(std::string::const_iterator cit=text.begin(); cit!=text.end(); ++cit) {
            if (*cit>='a' && *cit<='z') {
                output<<googlerese_table[*cit-'a'];
            } else if (*cit>='A' && *cit<='Z') {
                output<<googlerese_table[*cit-'A'];
            } else {
                output << *cit;
            }
        }
        output<<std::endl;
    }
    if (input.fail() || !output.good()) {
        std::cout<<"File error"<<std::endl;
        return 1;
    }
    return 0;
}

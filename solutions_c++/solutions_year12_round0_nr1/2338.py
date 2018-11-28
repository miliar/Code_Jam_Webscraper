#include <sstream>
#include <map>
#include <cstring>
#include <string>
#include <fstream>
#include <iostream>
using namespace std;

string translate(char* token,map<char,char> &dict){
    stringstream ss;
        ss.str("");
        int i = 0;
        while(token[i]){
            ss << dict[token[i]];
            i++;
        }
        return ss.str();
}

void read_file(string inFileName){
    ifstream inFile(inFileName.c_str());
    ofstream fout("a_out.txt");
    map<char,char> dict;
    dict['y'] = 'a';
    dict['n'] = 'b';
    dict['f'] = 'c';
    dict['i'] = 'd';
    dict['c'] = 'e';
    dict['w'] = 'f';
    dict['l'] = 'g';
    dict['b'] = 'h';
    dict['k'] = 'i';
    dict['u'] = 'j';
    dict['o'] = 'k';
    dict['m'] = 'l';
    dict['x'] = 'm';
    dict['s'] = 'n';
    dict['e'] = 'o';
    dict['v'] = 'p';
    dict['z'] = 'q';
    dict['p'] = 'r';
    dict['d'] = 's';
    dict['r'] = 't';
    dict['j'] = 'u';
    dict['g'] = 'v';
    dict['t'] = 'w';
    dict['h'] = 'x';
    dict['a'] = 'y';
    dict['q'] = 'z';



    if(!inFile.good()){
        return;
    }
    string line;
    char* token = NULL;
    int nTest = 0;
    char ch1;
    char ch2;
    /*
    inFile >> nTest;
    inFile >> ch1;
    inFile >> ch2;
    cout << nTest << endl;
    cout << ch1 << endl;
    cout << ch2 << endl;
    fout << nTest << "\n";
    while(1){
        inFile >> ch1;
    }
    */
    int cnt = 0;
    string s;
    int ti = 1;
    while(getline(inFile,line)){
        if (cnt == 0){
            cnt ++ ;            
            continue;
        }
        token = strtok(const_cast<char*>(line.c_str())," ");
        fout << " Case #" << ti << ":";
        ti ++ ;
        while(token!=NULL){
            s = translate(token,dict);
            fout << " " << s;
            token = strtok(NULL," ");
        }
        fout << "\n";
    }
    inFile.close();
    fout.close();
}

int main(){    
    read_file("A-small-attempt1.in");
//    read_file("a.in");
    return 0;
}

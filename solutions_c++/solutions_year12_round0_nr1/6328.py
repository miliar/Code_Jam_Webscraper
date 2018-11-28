#include <cstdlib>
#include <iostream>
#include <fstream>
#include <string>
#include <map>

using namespace std;

int main(int argc, char** argv) {
    ifstream in("a.in");
    ifstream sample_in("sample.in");
    ofstream out("a.out");
    ifstream sample_out("sample.out");
    string str, str_sample;
    typedef map <char,char> dict;
    dict d;
    dict::iterator iter = d.begin();


    getline(sample_in,str);
    int i = 0, num = atoi(str.c_str());
    while(getline(sample_in,str)){
        getline(sample_out,str_sample);
        for (int i = 0; i < str.size(); i++){
            d.insert(pair<char,char>(str[i],str_sample[i]));
        }
        d.insert(pair<char,char>('q','z'));
        d.insert(pair<char,char>('z','q'));
    }
    i = 1;
    getline(in,str);
    while (getline(in,str)){
        out << "Case #" << i++ << ": ";
        for (int i=0; i < str.size(); i++){
            iter = d.find(str[i]);
            out << iter->second;
        }
        out << endl;
    }
    return 0;
}

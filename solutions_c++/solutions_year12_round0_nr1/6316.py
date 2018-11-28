/* 
 * File:   main.cpp
 * Author: andrey
 *
 * Created on April 14, 2012, 7:23 PM
 */

#include <cstdlib>
#include <iostream>
#include <fstream>
#include <string>
#include <map>

using namespace std;

/*
 * 
 */

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
    //cout << "num of lines: " << dec << num << endl;
    while(getline(sample_in,str)){
        getline(sample_out,str_sample);
//        cout << "Case #" << i++ << " " << str << endl;
        for (int i = 0; i < str.size(); i++){
            d.insert(pair<char,char>(str[i],str_sample[i]));
        }
        d.insert(pair<char,char>('q','z'));
        d.insert(pair<char,char>('z','q'));
    }
    /*
   for (dict::const_iterator it = d.begin(); it != d.end(); ++it) {
        std::cout << it->first;
        std::cout << it->second << '\n';
    }
     */
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
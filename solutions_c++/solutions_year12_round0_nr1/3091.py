#include <iostream>
#include "map.h"
#include "simpio.h"
using namespace std;

int stringToInteger(string str);

int main(){
    Map<char, char> map;
    map.put('y','a');
    map.put('n','b');
    map.put('f','c');
    map.put('i','d');
    map.put('c','e');
    map.put('w','f');
    map.put('l','g');
    map.put('b','h');
    map.put('k','i');
    map.put('u','j');
    map.put('o','k');
    map.put('m','l');
    map.put('x','m');
    map.put('s','n');
    map.put('e','o');
    map.put('v','p');
    map.put('z','q');
    map.put('p','r');
    map.put('d','s');
    map.put('r','t');
    map.put('j','u');
    map.put('g','v');
    map.put('t','w');
    map.put('h','x');
    map.put('a','y');
    map.put('q','z');
    map.put(' ', ' ');
    
    ifstream fin;
    ofstream fout;
    int numCases;
    string line2;
    fin.open("/Users/leungtimothy/Desktop/A-small-attempt3.in.txt");
    fout.open("/Users/leungtimothy/Desktop/problem1_result.txt");
    getline(fin,line2);
    line2 = line2.substr(0,2);
    numCases = stringToInteger(line2);
    for (int j = 0; j < numCases; j++) {    
        string line;
        getline(fin,line);
        for (int i = 0;  i < line.length(); i++) {
            line[i] = map.get(line[i]);
        }
        fout << "Case #" << j + 1 << ": "<< line << endl;

    }
    fin.close();
    fout.close();
    return 0;
    
}

int stringToInteger(string str) {
    istringstream stream(str);
    int value;
    stream >> value >> ws;
    if (stream.fail() || !stream.eof()) {
        error("stringToInteger: Illegal integer format");
    }
    return value;
}
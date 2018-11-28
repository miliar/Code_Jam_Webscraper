#include <stdio.h>
#include <string>
#include <iostream>
#include <stdlib.h>
#include <fstream>

using namespace std;

string transform(string a){
    string b;
    for (int i=0;i<a.length();i++){
        switch(a.at(i)){
            case 'a':
                b.push_back('y');
            break;
            case 'b':
                b.push_back('h');
            break;
            case 'c':
                b.push_back('e');
            break;
            case 'd':
                b.push_back('s');
            break;
            case 'e':
                b.push_back('o');
            break;
            case 'f':
                b.push_back('c');
            break;
            case 'g':
                b.push_back('v');
            break;
            case 'h':
                b.push_back('x');
            break;
            case 'i':
                b.push_back('d');
            break;
            case 'j':
                b.push_back('u');
            break;
            case 'k':
                b.push_back('i');
            break;
            case 'l':
                b.push_back('g');
            break;
            case 'm':
                b.push_back('l');
            break;
            case 'n':
                b.push_back('b');
            break;
            case 'o':
                b.push_back('k');
            break;
            case 'p':
                b.push_back('r');
            break;
            case 'q':
                b.push_back('z');
            break;
            case 'r':
                b.push_back('t');
            break;
            case 's':
                b.push_back('n');
            break;
            case 't':
                b.push_back('w');
            break;
            case 'u':
                b.push_back('j');
            break;
            case 'v':
                b.push_back('p');
            break;
            case 'w':
                b.push_back('f');
            break;
            case 'x':
                b.push_back('m');
            break;
            case 'y':
                b.push_back('a');
            break;
            case 'z':
                b.push_back('q');
            break;
            case ' ':
                b.push_back(' ');
            break;
        };
    }
    return b;
}

int main(){
    int a,cont=1;
    string asdd;
    fstream file,output;
    file.open("A-small-attempt1.in", fstream::in);
    output.open("tarea1.out", fstream::out);
    file >> asdd;
    file.ignore();
    a=atoi(asdd.c_str());
    while(a--){
        string b,asd;
        getline(file,asd,'\n');
        b=transform(asd);
        output << "Case #"<<cont<<": "<<b<<endl;
        cont++;
    }
    file.close();
    output.close();
}

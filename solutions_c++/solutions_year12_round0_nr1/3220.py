#include<stdio.h>
#include<iostream>
#include<string>
#include <algorithm>

using namespace std;

int main(){
    freopen("in2.in","r",stdin);
    freopen("out2.txt","w",stdout);

    int t;
    string ts;

    getline(cin,ts);
    t=atoi(ts.c_str());

    for(int ti=0;ti<t;ti++){
        string line;
        getline(cin,line);

        for(int i=0;i<line.size();i++){
            switch(line[i]){
                case 'a': line[i] = 'y'; break;
                case 'b': line[i] = 'h'; break;
                case 'c': line[i] = 'e'; break;
                case 'd': line[i] = 's'; break;
                case 'e': line[i] = 'o'; break;
                case 'f': line[i] = 'c'; break;
                case 'g': line[i] = 'v'; break;
                case 'h': line[i] = 'x'; break;
                case 'i': line[i] = 'd'; break;
                case 'j': line[i] = 'u'; break;
                case 'k': line[i] = 'i'; break;
                case 'l': line[i] = 'g'; break;
                case 'm': line[i] = 'l'; break;
                case 'n': line[i] = 'b'; break;
                case 'o': line[i] = 'k'; break;
                case 'p': line[i] = 'r'; break;
                case 'q': line[i] = 'z'; break;
                case 'r': line[i] = 't'; break;
                case 's': line[i] = 'n'; break;
                case 't': line[i] = 'w'; break;
                case 'u': line[i] = 'j'; break;
                case 'v': line[i] = 'p'; break;
                case 'w': line[i] = 'f'; break;
                case 'x': line[i] = 'm'; break;
                case 'y': line[i] = 'a'; break;
                case 'z': line[i] = 'q'; break;
            }
        }

        cout << "Case #" << (ti+1) << ": " << line << endl;
    }
}

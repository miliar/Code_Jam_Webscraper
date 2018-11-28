#include <iostream>
#include <string>
#include <fstream>
#include <stdlib.h>

using namespace std;

int main(int argc, char *argv[])
{
    string s1;
    int a;
    ifstream f("A-small-attempt2.in");
    getline(f,s1);
    a=atoi(s1.c_str());
    string *s;
    s = new string[a];
    for(int i=0;i<a;i++){
        getline(f,s[i]);
    }
    for(int i=0; i<a; i++){
        for(unsigned int j=0;j<s[i].length();j++){
            switch(s[i][j]){
                case 'a': s1='y';
                          s[i].replace(j,1,s1);
                          break;
                case 'b': s1='h';
                          s[i].replace(j,1,s1);
                          break;
                case 'c': s1='e';
                          s[i].replace(j,1,s1);
                          break;
                case 'd': s1='s';
                          s[i].replace(j,1,s1);
                          break;
                case 'e': s1='o';
                          s[i].replace(j,1,s1);
                          break;
                case 'f': s1='c';
                          s[i].replace(j,1,s1);
                          break;
                case 'g': s1='v';
                          s[i].replace(j,1,s1);
                          break;
                case 'h': s1='x';
                          s[i].replace(j,1,s1);
                          break;
                case 'i': s1='d';
                          s[i].replace(j,1,s1);
                          break;
                case 'j': s1='u';
                          s[i].replace(j,1,s1);
                          break;
                case 'k': s1='i';
                          s[i].replace(j,1,s1);
                          break;
                case 'l': s1='g';
                          s[i].replace(j,1,s1);
                          break;
                case 'm': s1='l';
                          s[i].replace(j,1,s1);
                          break;
                case 'n': s1='b';
                          s[i].replace(j,1,s1);
                          break;
                case 'o': s1='k';
                          s[i].replace(j,1,s1);
                          break;
                case 'p': s1='r';
                          s[i].replace(j,1,s1);
                          break;
                case 'q': s1='z';
                          s[i].replace(j,1,s1);
                          break;
                case 'r': s1='t';
                          s[i].replace(j,1,s1);
                          break;
                case 's': s1='n';
                          s[i].replace(j,1,s1);
                          break;
                case 't': s1='w';
                          s[i].replace(j,1,s1);
                          break;
                case 'u': s1='j';
                          s[i].replace(j,1,s1);
                          break;
                case 'v': s1='p';
                          s[i].replace(j,1,s1);
                          break;
                case 'w': s1='f';
                          s[i].replace(j,1,s1);
                          break;
                case 'x': s1='m';
                          s[i].replace(j,1,s1);
                          break;
                case 'y': s1='a';
                          s[i].replace(j,1,s1);
                          break;
                case 'z': s1='q';
                          s[i].replace(j,1,s1);
                          break;
                case '\040': s1='\040';
                          s[i].replace(j,1,s1);
                          break;
                }
        }
   }
   ofstream op;
   op.open("google.txt");
for(int i=0;i<a; i++)
    op<<"Case #"<<i+1<<": "<<s[i]<<endl;
    op.close();
    delete [] s;
    return 0;
}

#include <stdio.h>
#include <string.h>
#include <string>
#include <map>
#include <iostream>

using namespace std;

int main(){
    map<char,char> alfabeto;
    char charAlfabeto[50]={'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'};
    alfabeto['a']='y';
    alfabeto['b']='h';
    alfabeto['c']='e';
    alfabeto['d']='s';
    alfabeto['e']='o';
    alfabeto['f']='c';
    alfabeto['g']='v';
    alfabeto['h']='x';
    alfabeto['i']='d';
    alfabeto['j']='u';
    alfabeto['k']='i';
    alfabeto['l']='g';
    alfabeto['m']='l';
    alfabeto['n']='b';
    alfabeto['o']='k';
    alfabeto['p']='r';
    alfabeto['q']='z';
    alfabeto['r']='t';
    alfabeto['s']='n';
    alfabeto['t']='w';
    alfabeto['u']='j';
    alfabeto['v']='p';
    alfabeto['w']='f';
    alfabeto['x']='m';
    alfabeto['y']='a';
    alfabeto['z']='q';
    alfabeto[' ']=' ';
    
   // freopen ("A-small-attempt0.in","r",stdin);
    //freopen ("salida.txt","w",stdout);
    int t;
    string p;
    getline (cin,p);
    t = atoi(p.c_str());
    for(int i=0; i<t; i++){
            string s,o="";
            getline (cin,s);
            for(int j=0; j<s.length(); j++){
                  o+=alfabeto[s[j]];
            }
            cout <<"Case #"<< i+1 <<": "<< o << endl;
    }
    //fclose(stdin);
   // fclose(stdout);
return 0;    
}

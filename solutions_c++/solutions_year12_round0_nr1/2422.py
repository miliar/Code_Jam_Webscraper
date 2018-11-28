#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <map>
#include <cstring>

using namespace std;

map<char,char> googlerese;

int main(int argc, char* argv[]){
    int T;
    scanf("%d\n",&T);
    googlerese.insert(pair<char,char>('a','y'));
    googlerese.insert(pair<char,char>('b','h'));
    googlerese.insert(pair<char,char>('c','e'));
    googlerese.insert(pair<char,char>('d','s'));
    googlerese.insert(pair<char,char>('e','o'));
    googlerese.insert(pair<char,char>('f','c'));
    googlerese.insert(pair<char,char>('g','v'));
    googlerese.insert(pair<char,char>('h','x'));
    googlerese.insert(pair<char,char>('i','d'));
    googlerese.insert(pair<char,char>('j','u'));
    googlerese.insert(pair<char,char>('k','i'));
    googlerese.insert(pair<char,char>('l','g'));
    googlerese.insert(pair<char,char>('m','l'));
    googlerese.insert(pair<char,char>('n','b'));
    googlerese.insert(pair<char,char>('o','k'));
    googlerese.insert(pair<char,char>('p','r'));
    googlerese.insert(pair<char,char>('q','z'));
    googlerese.insert(pair<char,char>('r','t'));
    googlerese.insert(pair<char,char>('s','n'));
    googlerese.insert(pair<char,char>('t','w'));
    googlerese.insert(pair<char,char>('u','j'));
    googlerese.insert(pair<char,char>('v','p'));
    googlerese.insert(pair<char,char>('w','f'));
    googlerese.insert(pair<char,char>('x','m'));
    googlerese.insert(pair<char,char>('y','a'));
    googlerese.insert(pair<char,char>('z','q'));
    googlerese.insert(pair<char,char>(' ',' '));
    int i = 1;
    while(T--){
               char *G = (char*)malloc(256*sizeof(char));
               char *A = (char *)malloc(256*sizeof(char));
               cin.getline (G, 101, '\n' );
               int len = strlen(G);
               for(int j=0; j<len; j++){
                       A[j] = googlerese[G[j]];
               }
               cout<<"Case #"<<i<<": "<<A<<endl;
               i++;
               G = "";
               A = "";
    }
    return 0;
}

#include <iostream>
#include <string>
#include <queue>
#include <vector>
#include <map>
#include <cstdio>
#include <cstdlib>
using namespace std;

bool testPattern(string a, string patt) {
    vector<string> v;

    for(int i=0; i<patt.length(); i++) {
       if(patt[i]=='(') {
          string s = "";
          while(patt[++i]!=')') {
             s += patt[i];
          }
          v.push_back(s);
       }
       else {
          string s = "*";
          s[0] = patt[i];
          v.push_back(s);
       }
    }

/*
cout << "###" << endl;
for(int i=0; i<a.length(); i++) cout << v[i] << endl;
cout << "###" << endl;
*/

    for(int i=0; i<a.length(); i++) {
       char c = a[i];
       bool found = false;
       for(int j=0; j<v[i].length(); j++) {
           if( v[i][j] == a[i] ) {
               found = true;
               break;
           }
       }
       if(!found) return false;
    }
    return true;
}

int main() {
    int L, D, N;
    int i;
    string s;
    
    scanf("%d%d%d", &L, &D, &N);
    
    vector<string> v(D);
    char tmp[20000];
    for(i=0; i<D; i++) {
       scanf("%s", tmp);
       v[i] = tmp;
    }
    for(i=1; i<=N; i++) {
       scanf("%s", tmp);
       string s = tmp;
       
       int cont = 0;
       for(int j=0; j<D; j++) {
          if( testPattern(v[j], s) ) cont++;
       }
       printf("Case #%d: %d\n", i, cont);
    }
}

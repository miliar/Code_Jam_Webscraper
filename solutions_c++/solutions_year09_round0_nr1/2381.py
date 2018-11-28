#include<cstdio>
#include<iostream>
#include<string>
#include<sstream>
#include<vector>

#define PB push_back

using namespace std;

typedef vector<string> VS;

int L=0, D=0, N=0;
VS lang;
int pword[15][26];

inline void parseword(string word, int pword[15][26]){
  bool b=false;
  int i=0, j=0;
  for(i=0; i<15; i++) for(j=0; j<26; j++) pword[i][j]=0;
  for(i=0, j=0; i<(int)word.size(); i++){
    switch(word[i]){
      case '(':
        b=true;
        break;
      case ')':
        b=false;
        j++;
        break;
      default:
        pword[j][word[i]-'a']=1;
        if(!b) j++;
    }
  }
}

inline bool matches(int pword[15][26], string w){
  for(int i=0; i<(int)w.size(); i++) if(pword[i][w[i]-'a']==0) return false;
  return true;
}

int main(){
  string pom="";
  int i=0, j=0, w=0;
  cin >> L >> D >> N;
  getline(cin,pom); 
  for(i=0; i<D; i++) {getline(cin,pom); lang.PB(pom);}
  for(i=0; i<N; i++) {
    getline(cin,pom); 
    parseword(pom, pword);
    w=0;
    for(j=0; j<(int)lang.size(); j++) if(matches(pword, lang[j])) w++;
    printf("Case #%d: %d\n", i+1, w);
  }
  return 0;
}

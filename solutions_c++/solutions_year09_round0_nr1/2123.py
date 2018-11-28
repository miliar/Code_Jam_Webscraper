
#include<string>
#include<vector>
#include<cmath>
#include<cstdio>
#include<cstring>
#include<iostream>
#include<utility>
#include <fstream>
#include <map>

using namespace std;


int main(){


  ifstream f("A-large.in");
  ofstream r("result.out");
  vector<string> words;
  string word, reg;
  int L,D,N;
  f>>L>>D>>N;
  words.resize(D);
  for (int z=0; z<D; z++){
    f>>words[z];
  }
  for (int k=0; k<N; k++){
    long ans = 0;
    f>>reg;
    vector<string> letters(L);
    int index = 0;
    bool fixed = true;
    for (int i=0; i<reg.size(); i++){
      if (reg[i] =='('){
        fixed = false;
      }
      else if (reg[i] ==')'){
        fixed = true;
      }
      else{
        letters[index]+=reg[i];
      }
      if (fixed) index++;

    }
    
    for (int i=0; i<D; i++){
      bool ok = true;
      for (int j=0; j<L; j++){
        if (letters[j].find(words[i][j])==-1) {
          ok = false;
          break;
        }
      }
      if (ok) ans++;
    }

    r<<"Case #"<<k+1<<": "<<ans<<endl;
    
  }



  f.close();
  r.close();
  return 0;
}


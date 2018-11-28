#include <stdio.h>
#include <iostream>
#include <stdlib.h>
#include <math.h>
#include <string.h>
#include <vector>
#include <algorithm>
#include <stdlib.h>

using namespace std;

int main(int argc, char** argv) {
	int i;
	int L, D, N;
  vector <string> Lword, Lpattern;
  string STemp;
	char S[1000];
	scanf("%d %d %d", &L, &D, &N);
  for (i = 1; i <=D; i++) {
    scanf("%s", S);
    STemp=S;
    Lword.push_back(STemp);
  }
  
  for (i = 1; i <= N; i++) {
    scanf("%s", S);
    STemp=S;
    Lpattern.push_back(STemp);
  }
  
  for (i = 1; i <= N; i++) {
    vector <string> StrPatterns(L, "");
    string STemp="";
    int curWord=1;
    bool writeFlag=false;
    for (int z=0; z < Lpattern[i-1].length(); z++) {
      if(Lpattern[i-1][z]=='(') {
        writeFlag=true;
      } else if (Lpattern[i-1][z]==')') {
        writeFlag=false;
        curWord++;
      } else {
        STemp = Lpattern[i-1][z];
        StrPatterns[curWord-1]+=STemp;
        if (writeFlag==false) {
          curWord++;
        }
      }
    }
    
    int NumberOfWords=0;
    for (int z = 1; z <= D; z++) {
      int w;
      for (w = 1; w <=L; w++) {
        size_t found;
        found = StrPatterns[w-1].find(Lword[z-1][w-1]);
        if (found==string::npos) {
          break;
        }
      }
      if (w==L+1) {
        NumberOfWords++;
      }
    }
    cout<<"Case #"<<i<<": "<<NumberOfWords<<"\n";
  }
}

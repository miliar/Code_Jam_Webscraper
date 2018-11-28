#include <iostream>
#include <cstring>
#include <string>

using namespace std;

char transTable[26];

int main(){

  for(int i=0; i<26; i++){
    transTable[i] = ' ';
  }

  string ex1 = "ejp mysljylc kd kxveddknmc re jsicpdrysi";
  string sol1 = "our language is impossible to understand";
  string ex2 = "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd";
  string sol2 = "there are twenty six factorial possibilities";
  string ex3 = "de kr kd eoya kw aej tysr re ujdr lkgc jv";
  string sol3 = "so it is okay if you want to just give up";

  for(int i=0; i<ex1.length(); i++){
    if(ex1[i]==' '){
      continue;
    }
    else{
      int index = (int)ex1[i]-(int)'a';
      if(transTable[index]==' '){
	transTable[index] = sol1[i];
      }
      else{
	assert(transTable[index]==sol1[i]);
      }
    }
  }

  for(int i=0; i<ex2.length(); i++){
    if(ex2[i]==' '){
      continue;
    }
    else{
      int index = (int)ex2[i]-(int)'a';
      if(transTable[index]==' '){
	transTable[index] = sol2[i];
      }
      else{
	assert(transTable[index]==sol2[i]);
      }
    }
  }

  for(int i=0; i<ex3.length(); i++){
    if(ex3[i]==' '){
      continue;
    }
    else{
      int index = (int)ex3[i]-(int)'a';
      if(transTable[index]==' '){
	transTable[index] = sol3[i];
      }
      else{
	assert(transTable[index]==sol3[i]);
      }
    }
  }

  transTable[(int)'q'-(int)'a'] = 'z';
  transTable[(int)'z'-(int)'a'] = 'q';

  /*
  for(int i=0; i<26; i++){
    cout<<transTable[i]<<endl;
  }
  */

  int N;
  scanf("%d",&N);
  string s;

  char c = getchar();
  //c = getchar();
  for(int i=0; i<N; i++){
    getline(cin,s,'\n');
    //cout<<s<<endl;
    
    
    
    for(int j=0; j<s.length(); j++){
      if(s[j]!=' ')
	s[j] = transTable[(int)s[j]-(int)'a'];
    }
    printf("Case #%d: %s\n",i+1,s.c_str());
    
  }

  return 0;
}

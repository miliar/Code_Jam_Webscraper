#include <iostream>
#include <vector>
#include <string.h>
#include <functional>
#include <algorithm>
#include <math.h>
#include <cstdio>
#include <queue>
#include <string>
#include <sstream>
#include <cstdlib>
#include <map>
#include <fstream>
using namespace std;


3
string a1 = "ejp mysljylc kd kxveddknmc re jsicpdrysi";
string a2 = "our language is impossible to understand";
string b1 = "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd";
string b2 = "there are twenty six factorial possibilities";
string c1 = "de kr kd eoya kw aej tysr re ujdr lkgc jv";
string c2 = "so it is okay if you want to just give up";

map<char,char> alphabet;

int main(){
  for(i=0;i<a.size();++i){
    alphabet[a1[i]]=a2[i];
  }
  for(i=0;i<b.size();++i){
    alphabet[b1[i]]=b2[i];
  }
  for(i=0;i<c.size();++i){
    alphabet[c1[i]]=c2[i];
  }
  map<char,char>::iterator it;
  for(it = alphabet.begin(); it!=alphabet.end();++it){
    cout<<*it->second<<endl;
  }
  


}

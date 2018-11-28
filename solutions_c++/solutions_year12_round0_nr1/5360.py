#include <iostream>
#include <map>
using namespace std;
int main(int argc, const char *argv[])
{
  int i,j,k,N;
  string alien   = "ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv";
  string english = "our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up";
  map<char,char> dict;
  for(i = 0; i<alien.length(); i++){
    if(dict.find(alien[i]) == dict.end()){
      dict[alien[i]] = english[i];
    }
  }
  dict['q'] = 'z';
  dict['z'] = 'q';
  
  scanf("%d\n",&N);
  for (i = 0; i < N; i++) {
    string input,output;
    getline(cin,input);
    cout<<"Case #"<<i+1<<": ";
    for(j = 0; j<input.length(); j++){
      cout<<dict[input[j]];
    }
    cout<<endl;
  }
  //for(map<char,char>::iterator it = dict.begin(); it!=dict.end(); it++){
    //cout<<(*it).first<<":"<<(*it).second<<endl;
  //}

  return 0;
}

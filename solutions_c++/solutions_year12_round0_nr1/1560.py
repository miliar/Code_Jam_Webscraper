#include <string>
#include <iostream>

using namespace std;

const string key = "yhesocvxduiglbkrztnwjpfmaq";

string decode(string in){
  for(size_t i=0;i<in.size();++i){
    if(in[i]==' ') continue;
    int idx = in[i]-'a';
    in[i]=key[idx];
  }
  return in;
}

int main() {
  int T;
  cin>>T>>ws;
  string in;
  for(int t = 1 ;t<=T;++t) {
    getline(cin,in);
    cout << "Case #"<<t<<": "<<decode(in)<<endl;
  }
}

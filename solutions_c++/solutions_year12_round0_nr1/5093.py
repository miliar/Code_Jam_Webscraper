#include<iostream>
#include<string>
using namespace std;

int main(){
  int N;
  cin>>N;
  string tmp,t2;

  //  .............abcdefghijklmnopqrstuvwxyz...
  string repl="yhesocvxduiglbkrztnwjpfmaq";
  getline(cin,tmp);
  for (int i=0;i<N;i++){
    getline(cin,tmp);
    t2="";
    for (int j=0;j<tmp.length();j++){
      if (tmp[j]==' ') t2+=' ';
      else t2+=repl[tmp[j]-'a'];
    }
    cout<<"Case #"<<i+1<<": "<<t2<<endl;
  }
}

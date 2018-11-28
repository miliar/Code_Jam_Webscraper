#include <string>
#include <iostream>
#include <stdlib.h>

using namespace std;

int main(){
  string out_alpha = "yhesocvxduiglbkrztnwjpfmaq";

  string in_s;
  
  int num=0;
  getline(cin,in_s);
  num=atoi(in_s.c_str());

  for(int i=0; i<num; i++){
    cout << "Case #" << (i+1) << ": ";
    getline(cin,in_s);

    for(int j=0; j<in_s.size(); j++){
      if( in_s[j] == ' '){
        cout << ' ';
      }else{
        cout << out_alpha[ in_s[j] - 'a' ];
      }
    }
    cout << endl;
  }
};

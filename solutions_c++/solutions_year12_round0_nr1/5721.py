#include <iostream>
#include <string>
#include <fstream>
using namespace std;

string str = "yhesocvxduiglbkrztnwjpfmaq";

int main(){
  ifstream fin("c.in");
  ofstream fout("c.out");
  int c;
  string input;
  fin >> c;
  if(fin.peek() == '\n') fin.get();
  for(size_t i(0); i < c; ++i){
    getline(fin,input);
    fout << "Case #" << i + 1 << ": ";
    for(size_t j(0); j < input.size(); ++j){
      if(input[j] == ' ') fout << ' ';
      else fout << str[input[j]-'a'];
    }
    fout << endl;
  }
  return 0;
}


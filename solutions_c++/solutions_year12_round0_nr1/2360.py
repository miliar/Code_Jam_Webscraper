#include <iostream>
#include <string>
#include <fstream>
#include <map>
#include <vector>

using namespace std;


int main(){

  map<char, char> m;
  m['y'] = 'a';
  m['e'] = 'o';
  m['q'] = 'z';
  m['z'] = 'q';
  
  ifstream sample;
  sample.open("sample.in");
  
  int T;
  sample >> T;
  char dummy[1];
  sample.getline(dummy, sizeof(dummy));
  for(int t=0; t<T; t++){
    char cipher[256];
    char plain[256];
    sample.getline(cipher,sizeof(cipher));
    sample.getline(plain, sizeof(plain));
    string ct = string(cipher);
    string pt = string(plain);
    int i=0;
    for(int i=0; i<ct.size(); i++)
      m[ct[i]] = pt[i];
  }
  
  ifstream in;
  ofstream out;
  
  in.open("a.in");
  out.open("a.out");
  
  in >> T;
  in.getline(dummy, sizeof(dummy));
  for(int t=1; t<=T; t++){
    char cipher[256];
    in.getline(cipher, sizeof(cipher));
    string ct = string(cipher);
    out << "Case #" << t << ": ";
    for(int i=0; i<ct.size(); i++)
      out << m[cipher[i]];
    out << endl;
  
  }
  
  return 0;
}

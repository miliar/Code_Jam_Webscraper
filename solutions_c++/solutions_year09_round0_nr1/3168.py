#include <fstream>
#include <iostream>
#include <vector>
#include <string>
using namespace std;

class AmbiguousWord {
private:
  vector<string> word;

public:
  void parse(const string& str) {
    bool inParan = false;
    for(int i=0; i<str.length(); ++i) {
      switch(str[i]) {
        case '(':
          inParan = true;
          word.push_back("");
          break;
        case ')':
          inParan = false;
          break;
        default :
          if (inParan) {
            word[word.size() - 1] += str[i];
          } else {
            string tmp = "";
            tmp += str[i];
            word.push_back(tmp);
          }
      } 
    } 
  } 

  bool match(const string& str) {
    for(int i=0; i<word.size(); ++i) {
      bool found = false;
      for(int j=0; j<word[i].length(); ++j) {
        if(word[i][j] == str[i]) {
          found = true;
          break;
        }
      }
      if(!found) {
        return false;
      }
    } 
    return true;
  }
  void print() {
    for(int i=0; i<word.size(); ++i) {
      cout<<word[i]<<endl;
    } 
  }
};

int main(int argc, const char** argv) {
  if (argc != 2) {
    cout<<"Input filename has to be passed\n";
    exit(1);
  }

  fstream file;
  file.open(argv[1], ios::in);

  int L, D, N;
  file>>L>>D>>N;

  string* dict = new string[D];
  for(int i=0; i<D; ++i) {
    file>>dict[i];
  }
  
  for(int i=0; i<N; ++i) {
    AmbiguousWord w;
    string str;
    file>>str;
    w.parse(str); 
    int matches = 0;
    for(int j=0; j<D; ++j) {
      if(w.match(dict[j])) {
        ++matches;
      }
    }
    cout<<"Case #"<<i+1<<": "<<matches<<endl;
  }

  file.close();
}

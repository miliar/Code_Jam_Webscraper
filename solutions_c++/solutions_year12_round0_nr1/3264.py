#include <iostream>
#include <unordered_map>
#include <algorithm>
#include <vector>
#include <string>

using namespace std;

typedef unordered_map<char,char> Charmap;

Charmap getCharMap();

int main() {

  int nr = 0;
  int maxNr;
  cin >> maxNr;
  cin.ignore(10,'\n');
  cerr <<  "maxNr= " << maxNr << endl;

  Charmap cmap = getCharMap();

  string line;
  getline(cin,line);
  while(!cin.eof() && nr < maxNr) {
    transform(line.begin(),line.end(),line.begin(),[&cmap](char c){ 
	if(cmap.find(c) == cmap.end()) {
	  cerr << "Char not found" << c << endl;
	}
	return cmap[c];
      });
    cout << "Case #" << ++nr << ": " << line << endl; 
    getline(cin,line);
  }
  if(nr != maxNr) {
    cerr << "unexpected end of stream..." << nr << " " << maxNr << endl;
  }

  return 0;
}


Charmap getCharMap() {
  Charmap cmap;

  //get Input
  vector<string> inputs = {
    "ejp mysljylc kd kxveddknmc re jsicpdrysi",
    "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd",
    "de kr kd eoya kw aej tysr re ujdr lkgc jv"
  };
  vector<string> outputs = {
    "our language is impossible to understand",
    "there are twenty six factorial possibilities",
    "so it is okay if you want to just give up"
  };
  
  for(int i = 0; i < inputs.size(); ++i) {
    equal(inputs[i].begin(),inputs[i].end(),outputs[i].begin(),
	  [&cmap](char in, char out){
	    if(cmap.find(in)== cmap.end()) {
	      cmap[in] = out;
	      if(in >= 'a' && in <= 'z') {
		cmap[in-'a'+'A'] = (out -'a'+'A');
	      }
	    } else {
	      if(cmap[in] != out) {
		cerr << "Input Output missmatch" << endl;
	      }
	    }
	    return true;
	  });
  }

  cmap['z'] = 'q';
  cmap['q'] = 'z';

  return cmap;
}

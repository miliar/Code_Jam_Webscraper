#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <algorithm>
#include <boost/foreach.hpp>

using namespace std;

int calc(const vector<vector<char> >& token, const vector<string>& words, const string& str){
  const int pos = str.size();
  bool found(false);
  for(int i=0;i!=words.size();++i){
    if(words[i].substr(0, pos) == str){
      found = true;
      break;
    }
  }
  if(!found){
    return 0;
  }
  if(pos == token.size()){
    return 1;
  }
  int ret(0);
  for(int i=0;i!=token[pos].size();++i){
    ret += calc(token, words, str + token[pos][i]);
  }
  return ret;
}

int solve(int L, const vector<string>& words, const string& line){
  vector<vector<char> > token;
  int ret(1);
  int pos(0);
  while(pos<line.size()){
    while(token.size() < L){
      if(line[pos]!='('){
	token.push_back(vector<char>(1, line[pos]));
	++pos;
      }
      else{
	token.push_back(vector<char>());
	for(++pos;line[pos]!=')';++pos){
	  token.back().push_back(line[pos]);
	}
	++pos;
      }
    }
    ret *= calc(token, words, "");
  }
  return ret;
}

int main(int argc, char* argv[]){
  int L, D, N;
  cin >> L >> D >> N;

  vector<string> words;
  for(int i=0;i!=D;++i){
    string w;
    cin >> w;
    words.push_back(w);
  }
  sort(words.begin(), words.end());
  for(int i=0;i!=N;++i){
    string line;
    cin >> line;
    cout << "Case #" << (i+1) << ": " << solve(L,words,line) << endl;
  }
  return 0;
}

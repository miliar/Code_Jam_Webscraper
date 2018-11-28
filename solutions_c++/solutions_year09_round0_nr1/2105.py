#include <iostream>
#include <set>
#include <vector>
using namespace std;

int l, d, n;
vector< string > words;

struct Glyph{
public:
  vector< set<char> > g;
};

vector<Glyph> glyphs;

void processGlyph(const string &str){
  bool stop = false;
  Glyph gly;
  for (int i = 0, index = 0; i < str.length(); ++i){
    if (str[i] == '(')
      stop = true;
    else if (str[i] == ')'){
      stop = false;
      ++index;
    }else {
      if (index >= gly.g.size()){
	set<char> s;
	s.insert(str[i]);
	gly.g.push_back(s);
      } else {
	set<char> s = gly.g[index];
	s.insert(str[i]);
	gly.g[index] = s;
      }
      if (!stop)
	++index;
    }
  }
  glyphs.push_back(gly);
}

void glyphMatch(){
  for (int i = 0; i < n; ++i){
    Glyph gly = glyphs[i];
    int count = 0;
    for (int j = 0; j < d; ++j){
      bool match = true;
      for (int k = 0; k < l; ++k)
	if (gly.g[k].find(words[j][k]) == gly.g[k].end()){
	  match = false;
	  break;
	}
      if (match)
	++count;
    }
    cout<<"Case #"<<i+1<<": "<<count<<endl;
  }
}

int main(){
  cin>>l>>d>>n;
  string str;
  getline(cin, str);
  for (int i = 0; i < d; ++i){
    getline(cin, str);
    words.push_back(str);
  }
  for (int i = 0; i < n; ++i){
    getline(cin, str);
    processGlyph(str);
  }

  glyphMatch();
}

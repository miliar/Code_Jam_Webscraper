#include <iostream>
#include <sstream>
#include <string>
#include <vector>

using namespace std;

vector<vector<int> > patternize(const string& s);
int matches(const vector<string>& words,const vector<vector<int> >& pattern);

int main(){
  int L,D,N;
  cin>>L>>D>>N;
  vector<string> words(D);
  for(int i=0;i<D;i++)
    cin>>words[i];
  for(int i=1;i<=N;i++){
    string s;
    cin>>s;
    vector<vector<int> > pattern=patternize(s);
    cout<<"Case #"<<i<<": "<<matches(words,pattern)<<'\n';
  }
}

vector<vector<int> > patternize(const string& s){
  vector<vector<int> > ret;
  for(int i=0;i<s.size();i++){
    vector<int> now(26);
    if(s[i]=='('){
      i++;
      while(s[i]!=')')
        now[s[i++]-'a']=1;
    }else
      now[s[i]-'a']=1;
    ret.push_back(now);
  }
  return ret;
}

bool matches(const string& word,const vector<vector<int> >& pattern){
  if(word.size()!=pattern.size())
    return false;
  for(int i=0;i<word.size();i++)
    if(!pattern[i][word[i]-'a'])
      return false;
  return true;
}

int matches(const vector<string>& words,const vector<vector<int> >& pattern){
  int ret=0;
  for(int i=0;i<words.size();i++)
    ret+=matches(words[i],pattern);
  return ret;
}

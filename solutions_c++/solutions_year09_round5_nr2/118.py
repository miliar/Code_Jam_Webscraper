#include <iostream>
#include <sstream>
#include <string>
#include <vector>

using namespace std;

vector<int> answer();

int main(){
  int t;
  cin>>t;
  for(int i=1;i<=t;i++){
    vector<int> v=answer();
    cout<<"Case #"<<i<<":";
    for(int i=0;i<v.size();i++)
      cout<<' '<<v[i];
    cout<<'\n';
  }
}

vector<int> v;
vector<vector<int> > word;
vector<string> polynomial;
vector<string> parse(string& p);
vector<int> count_up(const string& s);
void dfs(int n,vector<bool>& used,vector<int>& count);

vector<int> answer(){
  string p;
  cin>>p;
  polynomial=parse(p);
  int K,words;
  cin>>K>>words;
  v=vector<int>(K);
  word=vector<vector<int> >(words);
  for(int i=0;i<words;i++){
    string s;
    cin>>s;
    word[i]=count_up(s);
  }
  vector<bool> used(words);
  vector<int> count(26);
  dfs(0,used,count);
  return v;
}

vector<string> parse(string& p){
  p+='+';
  string s;
  vector<string> ret;
  for(int i=0;i<p.size();i++)
    if(p[i]=='+'){
      ret.push_back(s);
      s="";
    }else
      s+=p[i];
  return ret;
}

const int MOD=10009;

int add(int a,int b){
  return (a+b)%MOD;
}

int mult(int a,int b){
  return (long long)(a)*b%MOD;
}

int eval(const string& s,const vector<int>& count){
  int ret=1;
  for(int i=0;i<s.size();i++)
    ret=mult(ret,count[s[i]-'a']);
  return ret;
}

void eval(int n,const vector<int>& count){
  int now=0;
  for(int i=0;i<polynomial.size();i++)
    now=add(now,eval(polynomial[i],count));
  //cout<<"now: "<<now<<'\n';
  v[n]=add(v[n],now);
}

void dfs(int n,vector<bool>& used,vector<int>& count){
  if(n)
    eval(n-1,count);
  if(n==v.size())
    return;
  for(int i=0;i<word.size();i++)
    if(!used[i]){
      //cout<<"adding in: "<<i<<'\n';
      for(int j=0;j<count.size();j++) count[j]+=word[i][j];
      dfs(n+1,used,count);
      for(int j=0;j<count.size();j++) count[j]-=word[i][j];
      //cout<<"removing: "<<i<<'\n';
    }
}

vector<int> count_up(const string& s){
  vector<int> ret(26);
  for(int i=0;i<s.size();i++)
    ret[s[i]-'a']++;
  return ret;
}

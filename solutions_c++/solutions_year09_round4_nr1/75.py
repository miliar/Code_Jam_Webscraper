#include <iostream>
#include <vector>
#include <string>

using namespace std;

int answer(const vector<string>& v);
int solvable(const vector<string>& v);

int main(){
  int t;
  cin>>t;
  for(int i=1;i<=t;i++){
    int n;
    cin>>n;
    vector<string> v(n);
    for(int j=0;j<v.size();j++)
      cin>>v[j];
    cout<<"Case #"<<i<<": "<<answer(v)<<'\n';
  }
}

char back(const string& s){
  return s[s.size()-1];
}

vector<string> trim(vector<string> v,int n){
  v.erase(v.begin()+n);
  for(int i=0;i<v.size();i++)
    v[i]=v[i].substr(0,v[i].size()-1);
  return v;
}

int answer(const vector<string>& v){
  if(v.size()==1)
    return 0;
  assert(solvable(v));
  int force=0;
  for(int i=0;i<v.size();i++)
    if(back(v[i])=='1'){
      int moves=v.size()-1-i;
      return moves+answer(trim(v,i));
    }
  for(int j=v.size()-1;j>=0;j--){
    vector<string> next=trim(v,j);
    if(solvable(next)){
      int moves=v.size()-1-j;
      return moves+answer(next);
    }
  }
  assert(false);
}

int number(const string& s){
  int ret=-1;
  for(int i=0;i<s.size();i++)
    if(s[i]=='1')
      ret=i;
  return ret;
}

int solvable(const vector<string>& v){
  vector<int> num(v.size());
  for(int i=0;i<v.size();i++)
    num[i]=number(v[i]);
  sort(num.begin(),num.end());
  for(int i=0;i<num.size();i++)
    if(num[i]>i)
      return false;
  return true;
}

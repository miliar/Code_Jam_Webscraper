#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

int solve();

int main(){
  int t;
  cin>>t;
  for(int i=0;i<t;i++)
    cout<<"Case #"<<i+1<<": "<<solve()<<'\n';
}

int encode(const vector<int>& order,string s);

int solve(){
  int k;
  string s;
  cin>>k>>s;
  vector<int> order(k);
  for(int i=0;i<order.size();i++)
    order[i]=i;
  int ret=s.size();
  do{
    ret=min(encode(order,s),ret);
  }while(next_permutation(order.begin(),order.end()));
  return ret;
}

int encode(const string& s){
  int ret=0;
  int k=0;
  while(k<s.size()){
    ret++;
    char now=s[k];
    while(k<s.size() && s[k]==now) k++;
  }
  return ret;
}

int encode(const vector<int>& order,string s){
  string next=s;
  for(int k=0;k<s.size();k+=order.size())
    for(int i=0;i<order.size();i++)
      next[k+order[i]]=s[k+i];
  return encode(next);
}

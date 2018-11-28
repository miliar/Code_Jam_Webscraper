#include <iostream>
#include <iomanip>
#include <string>
#include <vector>

using namespace std;

const string pattern="welcome to code jam";
const int MOD=10000;
int answer(const string& s);

int main(){
  int t;
  cin>>t;
  string line;
  getline(cin,line);
  cout.fill('0');
  for(int i=1;i<=t;i++){
    getline(cin,line);
    cout<<"Case #"<<i<<": "<<setw(4)<<answer(line)<<'\n';
  }
}

int add(int a,int b){
  return (a+b)%MOD;
}

int answer(const string& s){
  vector<int> total(pattern.size()+1);
  total[0]=1;
  for(int i=0;i<s.size();i++){
    vector<int> now=total;
    for(int j=0;j<pattern.size();j++)
      if(s[i]==pattern[j])
        now[j+1]=add(now[j+1],total[j]);
    total=now;
  }
  return total.back();
}

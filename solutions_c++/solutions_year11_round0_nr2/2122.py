#include <iostream>
#include <string>
#include <set>
#include <map>
#include <stack>
#include <algorithm>
using namespace std;

typedef map<string,string> invoke;

string magicka(string seq, invoke combo, invoke inhib){
  string result = seq.substr(0,1);
  string destroy = inhib[result];
  for (int i = 1; i < seq.length(); ++i){
    string temp = combo[result.substr(result.length() - 1, 1) + seq.substr(i, 1)];
    if (temp.length() != 0){
      result = result.substr(0, result.length() - 1) + temp;
      destroy = "";
      // not very efficient
      for (int j = 0; j < result.length() - 1; ++j)
        destroy = destroy + inhib[result.substr(j,1)];
    }else{
      temp = seq.substr(i, 1);
      result = result + seq.substr(i, 1);
    }
    if (destroy.find(temp) != destroy.npos){
      if (i == seq.length() - 1)
        result = "";
      else{
        i++;
        result = seq.substr(i, 1);
      }
      destroy = inhib[result];
    }else
      destroy = destroy + inhib[temp];
    //cout<<result<<endl;
  }
  return result;
}

int main(){
  int t; cin>>t;
  for (int count = 1; count <= t; ++count){
    int n; cin>>n; string str;
    invoke combine;
    for (int i = 0; i < n; ++i){
      cin>>str;
      combine[str.substr(0, 2)] = str.substr(2, 1);
      reverse(str.begin(), str.begin() + 2);
      combine[str.substr(0, 2)] = str.substr(2, 1);
    }
    cin>>n;
    invoke inhibit;
    for (int i = 0; i < n; ++i){
      cin>>str;
      inhibit[str.substr(0,1)] = inhibit[str.substr(0,1)] + str.substr(1,1);
      inhibit[str.substr(1,1)] = inhibit[str.substr(1,1)] + str.substr(0,1);
    }
    cin>>n;
    cin>>str;
    str = magicka(str, combine, inhibit);
    cout<<"Case #"<<count<<": [";
    bool isFirst = true;
    for (int i = 0; i < str.length(); ++i){
      if (isFirst)
        isFirst = false;
      else
        cout<<", ";
      cout<<str[i];
    }
    cout<<"]"<<endl;
  }
}

#include <iostream>
#include <string>
#include <vector>

using namespace std;
vector<string> known;
int L, D;

bool match(const string& a, const string& b) {
  int i=0, j=0;
  int s=b.size();
  while (i<L) {
    if (j>s) return false;
    if (b[j]=='(') {
      bool m=false;
      while (j<s &&  b[j] != ')') {
        if(b[j]==a[i]) m=true;
        j++;
      }
      if (!m) return false;
    } else {
      if (b[j]!=a[i]) return false;
    }
    j++;
    i++;
  }
  return true;
}

int num_matching(string p) {
  int m = 0;
  for(int i = 0; i<D;i++){
    if(match(known[i], p)){
      m++;
    }
  }
  return m;
}

int main(int argc, char** argv){
  int N;
  cin>>L>>D>>N;
  for(int i=0;i<D;i++){
    string w;
    cin>>w;
    known.push_back(w);
  }
  for(int i=1;i<=N;i++){
    string w;
    cin>>w;
    cout<<"Case #"<<i<<": " << num_matching(w)<<endl;
  }
  return 0;
}

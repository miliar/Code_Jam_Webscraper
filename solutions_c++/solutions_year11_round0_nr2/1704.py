#include <iostream>
#include <vector>
#include <map>
#include <set>
using namespace std;

int main(int argc, char *argv[])
{
  int cases; cin>>cases;
  for (int cn=1; cn<=cases; cn++){
    int c; cin>>c;

    map<char, map<char, char> > cv;
    for (int i = 0; i<c; ++i) {
      char a, b, t;
      cin>>a>>b>>t;
      cv[a][b]=t;
      cv[b][a]=t;
    }

    int d; cin>>d;
    map<char, set<char> > rm;
    for (int i = 0; i<d; ++i) {
      char a, b; cin>>a>>b;
      rm[a].insert(b);
      rm[b].insert(a);
    }

    int n; cin>>n;
    vector<int> v;
    for (int i = 0; i<n; ++i) {
      char c; cin>>c;
      if (v.size()>0 && cv[c].count(v.back())){
        char t=cv[c][v.back()];
        v.pop_back();
        v.push_back(t);
      }
      else{
        bool any=false;
        for (int j=0; j<(int)v.size(); ++j) {
          if (rm[c].count(v[j])){
            any=true;
            break;
          }
        }
        if (any)
          v.clear();
        else
          v.push_back(c);
      }
    }

    cout<<"Case #"<<cn<<": [";

    for (int i = 0; i<(int)v.size(); ++i) {
      if (i>0) cout<<", ";
      cout<<(char)v[i];
    }

    cout<<"]"<<endl;
  }
  return 0;
}

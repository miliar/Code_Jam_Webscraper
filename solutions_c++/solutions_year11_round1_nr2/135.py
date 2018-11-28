#include <iostream>
#include <vector>
#include <string>
#include <list>
#include <map>
using namespace std;

void calc(int pos, list<int> & dict,string & l, vector<vector<int> > &containers, vector<int> & res, int val)
{

  if (dict.size() == 1) {
    res[*dict.begin()] = max(res[*dict.begin()],val);
    return;
  };

  map<int,list<int> > conjs;

  for (list<int>::iterator it = dict.begin();it!=dict.end();it++) {
    conjs[containers[*it][l[pos]-'a']].push_back(*it);
  };

  if (conjs.size() == 1) {
    calc(pos+1,dict,l,containers,res,val);
  } else {
    for (map<int,list<int> >::iterator it = conjs.begin(); it!= conjs.end(); it++) {
      if (it->first == 0) {
        calc(pos+1,it->second,l,containers,res,val+1);
      } else {
        calc(pos+1,it->second,l,containers,res,val);
      }
    };
  };

};

int main() {

  int t;
  cin >> t;

  for (int i=0;i<t;i++) {
    int n;
    int m;
    cin >> n >> m;
    vector<string> dict(n);
    vector<vector<int> > containers(n,vector<int>(26,0));
    for (int j=0;j<n;j++) {
      cin >> dict[j];
      int bi = 1;
      for (int k=0;k<dict[j].size();k++) {
        containers[j][dict[j][k]-'a'] |= bi;
        bi <<= 1;
      };
    };

    cout << "Case #" << i + 1 << ":";

    for (int j=0;j<m;j++) {
      string lista;
      cin >> lista;

      vector<int> res(dict.size(),0);

      for (int k=1;k<=10;k++) {

        list<int> dict_n;
        for (int l=0;l<dict.size();l++) {
          if (dict[l].size() == k) {
            dict_n.push_back(l);
          };
        };
        if (dict_n.size()) {
          calc(0,dict_n,lista,containers,res,0);
        };

      };
      int max = res[0];
      int maxi = 0;
      for (int l=1;l<res.size();l++) {
        if (res[l] > max) {
          max = res[l];
          maxi = l;
        };
      };

      cout << " " << dict[maxi];

    };

    cout << endl;

  };

  return 0;
};

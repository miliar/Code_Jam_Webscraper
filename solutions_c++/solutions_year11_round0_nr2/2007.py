#include <iostream>
#include <string>
#include <set>
#include <map>
#include <algorithm>
#include <vector>
using namespace std;

class comp
{
public:
  bool operator()(string a, string b){
    return a < b;
  }
};

int main(){
  int T;
  cin>>T;
  for(int t=1; t<=T; t++){
    int C,D,N;
    cin >> C;
   
    map<string,char> combos;
    set<string> valid_combo;
    for(int i=0;i<C;i++){
      string combo;
      cin >> combo;
      string key = combo.substr(0,2);
      combos[key] = combo[2];
      valid_combo.insert(key);
      reverse(key.begin(),key.end());
      combos[key] = combo[2];
      valid_combo.insert(key);
    }
    cin >> D;
    set<string> oppose;
    for(int i=0;i<D;i++){
      string op;
      cin >> op;
      oppose.insert(op);
      reverse(op.begin(),op.end());
      oppose.insert(op);
    }
    cin >> N;
    string cmd;
    cin >> cmd;
    vector<char> res;
    for(int i=0;i<N;i++){
      char next = cmd[i];
      if(res.size()) {
	string combo = "";
	combo += res[res.size()-1];
	combo += next;
	if(valid_combo.find(combo)!=valid_combo.end()){
	  res.erase(res.begin()+res.size()-1);
	  res.push_back(combos[combo]);
	  continue;
	}
      }
      bool opp = false;
      for(int j=0;j<res.size();j++){
	string test_op = "";
	test_op += res[j];
	test_op += next;
	if(oppose.find(test_op)!=oppose.end()){
	  opp=true;
	  break;
	}
      }
      if(opp)
	res.clear();
      else
	res.push_back(next);
    }
    cout << "Case #" << t << ": [";
    for(int i=0; i<res.size(); i++){
      cout << res[i];
      if(i<res.size()-1)
	cout << ", ";
    }
    cout << "]" << endl;
  }

}

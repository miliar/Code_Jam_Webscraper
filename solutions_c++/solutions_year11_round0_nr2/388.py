#include <iostream>
#include <set>
#include <map>
#include <string>
#include <deque>
#include <cstring>
using namespace std;
string deque2comlist(deque<char> aDeque){
  if (aDeque.empty())
    return "";
  string ans=string("")+aDeque[0];
  for (int i = 1; i < aDeque.size(); ++i){
    ans += ", ";
    ans += aDeque[i];
  }
  return ans;
}
string solve(){
  string combine[36],oppose[28],invoke;
  deque<char> ans;
  ans.clear();
  map<char,int> inside;
  char combinel[128][128];
  bool opposel[128][128];
  memset(combinel,0,sizeof combinel);
  memset(opposel,0,sizeof opposel);
  inside.clear();
  int c,d,n;
  cin >> c;
  for (int i = 0; i < c; ++i){
    cin >> combine[i];
    combinel[combine[i][0]][combine[i][1]] = combinel[combine[i][1]][combine[i][0]] = combine[i][2];
  }
  cin >> d;
  for (int i = 0; i < d; ++i){
    cin >> oppose[i];
    opposel[oppose[i][0]][oppose[i][1]] = opposel[oppose[i][1]][oppose[i][0]] = true;
  }
  cin >> n;
  cin >> invoke;
  for (int i = 0; i < n; ++i){
    //    cout << i <<endl;
    //    for (deque<char>::iterator i = ans.begin();i!=ans.end();++i)
    //      cout<< *i;
    //    cout <<endl;
    bool pk = false;
    if (!ans.empty()){
      if (combinel[ans.back()][invoke[i]]){
	pk=true;
	char prev_back = ans.back();
	inside[ans.back()]--;
	if (inside[ans.back()]==0)
	  inside.erase(ans.back());
	ans.pop_back();
	ans.push_back(combinel[prev_back][invoke[i]]);
	if (inside.find(combinel[prev_back][invoke[i]])==inside.end())
	  inside[combinel[prev_back][invoke[i]]] = 1;
	else
	  ++inside[combinel[prev_back][invoke[i]]];
      }else{
	for (map<char,int>::iterator j = inside.begin(); j!=inside.end(); ++j)
	  if (opposel[j->first][invoke[i]]){
	    inside.clear();
	    ans.clear();
	    pk = true;
	    break;
	  }
      }	    
      if (!pk){
	if (inside.find(invoke[i])==inside.end())
	  inside[invoke[i]] = 1;
	else
	  ++inside[invoke[i]];
	ans.push_back(invoke[i]);
      }
    }
    else {
      if (inside.find(invoke[i])==inside.end())
	inside[invoke[i]] = 1;
      else
	++inside[invoke[i]];
      ans.push_back(invoke[i]);
    }
  }
  return string("[")+deque2comlist(ans)+"]";
}
int main(){
  int t;
  cin >> t;
  for (int i = 1; i <= t; ++i)
    cout << "Case #" << i << ": " << solve() << endl;
}

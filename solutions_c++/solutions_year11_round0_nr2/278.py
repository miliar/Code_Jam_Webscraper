#include <iostream>
#include <vector>
#include <utility>
#include <cstring>
#include <set>
#include <deque>
#include "../../print.hpp"

using namespace std;

int INF = -100000;
const static char base[8] =  {'Q', 'W', 'E', 'R', 'A', 'S', 'D', 'F'};

void solve(string& invoke, 
	   vector<vector<int> > & C , 
	   vector<vector<int> > & D, 
	   string & ans){

  deque<char> st;
  vector<int> stat(26);

  for(int i = 0;i< invoke.size();i++){
    
    /*
    if(!st.empty()){
      cout << "combine : " << st.back() - 'A' << " " <<invoke[i]- 'A' <<endl;
      cout << table[st.back() - 'A'][invoke[i]- 'A']  << endl;
    }
    */

    if(!st.empty() && C[st.back() - 'A'][invoke[i]- 'A'] >= 0){
      char to_be_removed = st.back();
      stat[to_be_removed - 'A']--;
      char to_be_put = 'A' + C[st.back() - 'A'][invoke[i]- 'A'];
      st.pop_back();
      st.push_back(to_be_put);
      stat[to_be_put - 'A']++;
      continue;
    }

    st.push_back(invoke[i]);
    stat[invoke[i] - 'A']++;

    for(int j = 0;j<8;j++){
      if(stat[base[j] - 'A'] > 0 && D[base[j]-'A'][invoke[i] - 'A'] == -1){
	st.clear();
	for(int k = 0;k < 26;k++){
	  stat[k] = 0;
	}
      }
    }    
  }
  ans.clear();
  ans += "[";
  while(!st.empty()){
    ans += st.front();
    ans += ", ";
    st.pop_front();
  }
  if(ans.size () >= 2) ans.erase(ans.end() -2, ans.end());
  ans += "]";

}

int main(){
  int t;cin >> t;
  for(int i = 1;i<=t;i++){
    vector<vector<int > > C(26, vector<int> (26));
    vector<vector<int > > D(26, vector<int> (26));
    for(int j = 0;j<26;j++){
      for(int k = 0;k<26;k++){
	C[j][k] = -1;
	D[j][k] = 0;
      }
    }

    int c,d;cin >> c;
    for(int j = 0;j<c;j++){
      string composed;cin >> composed;
      C[composed[0] - 'A'][composed[1] - 'A'] = composed[2] - 'A';
      C[composed[1] - 'A'][composed[0] - 'A'] = composed[2] - 'A';
    }
    cin >> d;
    for(int j = 0;j<d;j++){
      string opposed;cin >> opposed;
      D[opposed[0] - 'A'][opposed[1] - 'A'] = -1;
      D[opposed[1] - 'A'][opposed[0] - 'A'] = -1;
     }
    int n;cin >> n;
    string invoke;cin >> invoke;
    string ans;
    solve(invoke, C, D, ans);

    cout << "Case #" << i << ": " << ans <<endl;
  }
  return 0;

}

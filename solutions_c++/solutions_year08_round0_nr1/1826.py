#include <iostream>
#include <string>
#include <map>
#include <set>
#include <algorithm>
using namespace std;

int main() {
  int caseNum;
  cin >> caseNum;

  for(int loop=1; loop<=caseNum; loop++) {
    int engineNum;
    cin >> engineNum;
    map<string, int> engineIndex;
    string temp;
    getline(cin, temp);
    for(int i=0; i<engineNum; i++) {
      getline(cin, temp);
      engineIndex[temp] = i;
    }

    int queryNum;
    cin >> queryNum;
    getline(cin, temp);
    int table[engineNum];
    fill_n(table, engineNum, 0);

    set<pair<int, int> > state;  // cost, engineIndex
    for(int i=0; i<engineNum; i++) state.insert(make_pair(0, i));
    
    for(int i=0; i<queryNum; i++) {
      getline(cin, temp);
      int index = engineIndex[temp];
      set<pair<int, int> >::iterator itr = state.begin();
      pair<int, int> deleteState = make_pair(table[index], index);
      if(itr->second == index) ++itr;
      table[index] = itr->first + 1;
      state.erase(deleteState);
      state.insert(make_pair(table[index], index));
    }

    int switchNum = state.begin()->first;
    cout << "Case #" << loop << ": " << switchNum << endl;
  }

  return 0;
}

#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <utility>
#include <algorithm>

using namespace std;
typedef std::pair<int, int> my_pair;

bool sort_pred(const my_pair& left, const my_pair& right)
{
  return left.second > right.second;
}

void pvecdumpi(vector< pair<int, int> > vp) {
  for (size_t i=0; i<vp.size(); i++) {
    cout << vp[i].first << " : " << vp[i].second << endl;
  }
}

int main() {
  int N; cin >> N;
  for (int caseCount=0; caseCount<N; caseCount++) {
    // keys are 0 index.
    map<int, vector<string> > keyMap;
    //map<int, int> keyFreq;
    //    multimap<int, int> freqKey;

    vector<my_pair> keyFreq;

    int P, K, L;
    cin >> P >> K >> L;
    int tmp;
    my_pair tmpPair;
    for (int i=0; i<L; i++) {
      cin >> tmp;
      tmpPair = my_pair(i, tmp);
      keyFreq.push_back(tmpPair);
    }
    //pvecdumpi(keyFreq);
    sort(keyFreq.begin(), keyFreq.end(), sort_pred);

    // cout << "___________";
    //pvecdumpi(keyFreq);
    vector<int> keyLetterCount;
    for (int i=0; i<K; i++) {
      keyLetterCount.push_back(0);
    }
    long long keyPushCount = 0;
    int key=0;

    bool impossible = false;
    for (int i=0; i<L; i++){
      if (key == 0 && keyLetterCount[0] == P) {
	impossible = true;
	break;
      }
      tmpPair = keyFreq[i];
      keyLetterCount[key] += 1;
      keyPushCount += (keyLetterCount[key]) * (tmpPair.second);
      key++;
      if (key == K) {
	key = 0;
      }

      if (impossible) {
	break;
      }
    }
    cout << "Case #"<< (caseCount+1) << ": ";
    if (impossible) {
      cout << "Impossible";
    } else {
      cout  << keyPushCount;
    }
    cout << endl;

  }
  return 0;
}

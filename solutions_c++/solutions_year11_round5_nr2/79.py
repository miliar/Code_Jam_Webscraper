#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cassert>
#include <climits>
#include <ctime>
#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <algorithm>
#include <vector>
#include <deque>
#include <list>
#include <queue>
#include <set>
#include <map>
#include <limits>

using namespace std;

int cards[1100];
int nCards;

struct RevOrder {
  bool operator()(int i, int j) const {
    return i > j;
  }
};

ostream& operator<<(ostream& os, vector<int>& v) {
  os << "[";
  for (int i = 0; i < (int) v.size(); i++) {
    os << v[i] << " ";
  }
  return os << "]";
}

int computeOpt() {
  vector<int> oldSeq; // length of sequences ending with lastValue-1 (in increasing order)
  vector<int> newSeq; // length of sequences ending with lastValue
  int lastValue = -2;
  int minLength = nCards;
  
  for (int i = 0; i < nCards; i++) {
    if (cards[i] != lastValue) {
      if (!oldSeq.empty()) {
        minLength = min(minLength, *min_element(oldSeq.begin(), oldSeq.end()));
      }
      oldSeq.clear();
      if (cards[i] - lastValue > 1) {
        if (!newSeq.empty())
          minLength = min(minLength, *min_element(newSeq.begin(), newSeq.end()));
        newSeq.clear();
      }
      oldSeq.swap(newSeq);
      sort(oldSeq.begin(), oldSeq.end(), RevOrder());
      //cout << "newnewseq=" << oldSeq << endl;
      lastValue = cards[i];
    }
    if (!oldSeq.empty()) {
      newSeq.push_back(oldSeq.back() + 1);
      oldSeq.pop_back();
    }
    else {
      newSeq.push_back(1);
    }
    /*cout << "i=" << i << " lastV=" << lastValue << " card=" << cards[i] << endl
         << "  oldSeq=" << oldSeq << endl
         << "  newSeq=" << newSeq << endl;*/
  }
  if (!oldSeq.empty())
    minLength = min(minLength, *min_element(oldSeq.begin(), oldSeq.end()));
  if (!newSeq.empty())
    minLength = min(minLength, *min_element(newSeq.begin(), newSeq.end()));
  return minLength;
}

int main() {
  int nCases;
  scanf("%d", &nCases);
  for (int iCase = 1; iCase <= nCases; iCase++) {
    scanf("%d", &nCards);
    printf("Case #%i: ", iCase);
    if (nCards == 0)
      printf("0\n");
    else {
      for (int i = 0; i < nCards; i++) {
        scanf("%d", &cards[i]);
      }
      sort(cards, cards + nCards);
      printf("%i\n", computeOpt());
    }
  }
  return 0;
}

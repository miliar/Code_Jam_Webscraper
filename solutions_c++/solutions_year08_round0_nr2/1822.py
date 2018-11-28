#include <cstdio>
#include <algorithm>
#include <vector>
using namespace std;

int main() {
  int caseNum;
  scanf("%d", &caseNum);

  for(int loop=1; loop<=caseNum; loop++) {
    int turnAround, ab, ba;
    scanf("%d%d%d", &turnAround, &ab, &ba);

    vector<pair<int, int> > dataA, dataB;   // time, diff
    for(int i=0; i<ab; i++) {
      int hour, min;
      scanf("%d:%d", &hour, &min);
      dataA.push_back(make_pair(hour*60+min, 1));
      scanf("%d:%d", &hour, &min);
      dataB.push_back(make_pair(hour*60+min+turnAround, -1));
    }
    for(int i=0; i<ba; i++) {
      int hour, min;
      scanf("%d:%d", &hour, &min);
      dataB.push_back(make_pair(hour*60+min, 1));
      scanf("%d:%d", &hour, &min);
      dataA.push_back(make_pair(hour*60+min+turnAround, -1));
    }
    sort(dataA.begin(), dataA.end());
    sort(dataB.begin(), dataB.end());

    int stockA=0, stockB=0;
    int maxA=0, maxB=0;
    for(int i=0; i<(int)dataA.size(); i++) {
      stockA += dataA[i].second;
      maxA = max(maxA, stockA);
    }
    for(int i=0; i<(int)dataB.size(); i++) {
      stockB += dataB[i].second;
      maxB = max(maxB, stockB);
    }

    printf("Case #%d: %d %d\n", loop, maxA, maxB);
  }

  return 0;
}

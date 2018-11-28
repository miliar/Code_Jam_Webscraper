#include <iostream>
#include <vector>
using namespace std;

typedef vector<float> FloatList;

float getHitCount(FloatList& probList, int listSize, int backCount, int B)
{
  float allOkProb = 1;
  for (int i = 0; i < listSize; i++)
    allOkProb *= probList[i];
  int rest = B - listSize + backCount;
  float res = allOkProb * (rest + 1) + (1 - allOkProb) * (rest + 1 + B + 1);
  return res;
}

int main()
{
  int T; cin >> T;
  for (int t = 1; t <= T; t++)
  {
    int A, B; cin >> A; cin >> B;
    FloatList probList;
    for (int a = 0; a < A; a++)
    {
      float prob;
      cin >> prob;
      probList.push_back(prob);
    }

    float minHitCount = 10000000;
    int SIZE = (int)probList.size();
    for (int backCount = 0; backCount <= SIZE; backCount++)
    {
      int listSize = SIZE - backCount;
      float hitCount = getHitCount(probList, listSize, backCount, B);
      minHitCount = min(minHitCount, hitCount);
    }
    minHitCount = min(minHitCount, float(1 + B + 1)); // enter + retype + enter
    //cout << "Case #" << t << ": " << minHitCount << endl;
    printf("Case #%d: %f\n", t, minHitCount);
  }
}
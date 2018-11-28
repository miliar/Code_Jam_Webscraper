#include <iostream>
#include <map>
#include <utility>
#include <cstdlib>
#include <cstdio>
#include <fstream>
using namespace std;

int testID;
int start[1000002];
int stop[1000002];
int nowA;

map<pair<int, int>, bool> state;

bool getState(int a, int b)
{
  if (a == b)
    return false;
  if (a <= 0 || b <= 0)
    return true;
  if (a == 1 || b == 1)
    return true;

  pair<int, int> abPair;
  if (a < b) { int c = a; a = b; b = c; }

  if (a % b == 0)
    return true;

  if (a < nowA)
    return !(b >= start[a] && b <= stop[a]);

  abPair.first = a;
  abPair.second = b;;
  if (state.find(abPair) != state.end())
    return state[abPair];

  bool nowState = false;
  int up = a / b;
  for (int k = up; k >= 1; --k)
    if (getState(b, a - b * k) == false)
    {
      nowState = true;
      break;
    }

  state[abPair] = nowState;
  return nowState;
}

int range(int a, int b, int a1, int b1)
{
  int s = max(a, a1);
  int t = min(b, b1);
  if (t >= s)
    return t - s + 1;
  else
    return 0;
}

void deal()
{
  int A1, A2, B1, B2;
  scanf("%d%d%d%d", &A1, &A2, &B1, &B2);
  long long ans = 0;

  for (int a = A1; a <= A2; ++a)
  {
    ans += B2 - B1 + 1 - range(start[a], stop[a], B1, B2);
  }

  cout << "Case #" << testID << ": " << ans << endl;

}

void init()
{
  ifstream fin("dict");
  for (nowA = 1; nowA <= 1000000; ++nowA)
  {
    /**
    int left = 1;
    int right = nowA;
    int mid = right;
    while (right > left)
    {
      mid = (left + right) >> 1;
      if (getState(nowA, mid))
        left = mid + 1;
      else 
        right = mid;
    }
    start[nowA] = left;
    stop[nowA] = left + nowA - 1;
    */
    fin >> start[nowA] >> stop[nowA];
  }
  fin.close();
}


int main()
{
  init();
  /**
  for (int a = 1; a <= 40; ++a)
  {
    cout << a << "\t";
    for (int b = 1; b <= 10000; ++b)
      if (!getState(a, b))
        cout << b << " ";
    cout << endl;
    cout << start[a] << "\t" << stop[a] << endl;
  }
  */
  int T;
  scanf("%d", &T);
  for (testID = 1; testID <= T; ++testID)
   deal();
  return 0;
}



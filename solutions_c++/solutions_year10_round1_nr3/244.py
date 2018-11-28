#include <cstdio>
#include <iostream>
#include <algorithm>
#include <map>

using namespace std;

const int Max = 1024000;

typedef pair<int, int> PII;
typedef long long i64;

map<PII, bool> isWin;
int Left[Max], Right[Max];

bool calcWin(int i, int j)
{
  if (i > j) swap(i, j);
  if (i == 0) return true;

  if (Left[i] && Right[i])
    return (j < Left[i] || j > Right[i]);

  PII key(i, j);
  if (isWin.count(key))
    return isWin[key];

  isWin[key] = false;
  for (int k = j/i; k > 0; k--)
    if (false == calcWin(i, j-k*i)) {
      isWin[key] = true;
      break;
    }

  return isWin[key];
}

int countIntersect(int a, int b, int c, int d)
{
  a = max(a, c);
  b = min(b, d);
  if (a <= b)
    return b-a+1; else
    return 0;
}

int calcBound(int p0, int w)
{
  int p = p0;
  while (abs(p-w) > 1) {
    int middle = (w+p)/2;
    if (calcWin(p0, middle))
      w = middle; else
      p = middle;
  }
  return p;
}

int A1, A2, B1, B2;

i64 solve()
{
  i64 res = 0;
  for (int a = A1; a <= A2; a++) {
    if (Left[a] == 0) {
      Left[a] = calcBound(a, 0);
      Right[a] = calcBound(a, a*2);
    }

    res += countIntersect(0, Left[a]-1, B1, B2);
    res += countIntersect(Right[a]+1, Max, B1, B2);
  }
  return res;
}

int main()
{
  int nTest;
  scanf("%d", &nTest);

  for (int iTest = 1; iTest <= nTest; iTest++) {
    scanf("%d %d %d %d", &A1, &A2, &B1, &B2);
    printf("Case #%d: ", iTest);
    cout << solve() << endl;
  }

  return 0;  
}

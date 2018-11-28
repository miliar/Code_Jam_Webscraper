#include <limits.h>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <limits>
#include <cassert>
#include <string>
#include <vector>
#include <deque>
#include <fstream>
#include <algorithm>
#include <numeric>
#include <iostream>
#include <iomanip>
#include <sstream>
#include <queue>
#include <iterator>
#include <set>
static const int INF = std::numeric_limits<int>::max();
int N, M;
std::vector<long long> AN, BN;
std::vector<int> AT, BT;

long long check(int aidx, int first, int last,
                std::vector<long long>& an, std::vector<long long>& bn)
{
  // std::cout << "do check AT[aidx]=" << AT[aidx] << " AN[aidx]=" << an[aidx]
  //           << ", " << first << ":" << last << std::endl;
  long long res = 0;
  for(int i = first; i <= last && i < (int)bn.size(); ++i) {
    if(AT[aidx] == BT[i]) {
      long long num = std::min(an[aidx], bn[i]);
      // std::cout << "BT[" << i << "]=" << BT[i] << ", num=" << num << ", bn[i]=" << bn[i] << std::endl;
      an[aidx] -= num;
      bn[i] -= num;
      res += num;
    }
  }
  return res;
}

long long solve1()
{
  std::vector<long long> an(AN), bn(BN);
  return check(0, 0, BN.size(), an, bn);
}
long long solve2()
{
  long long res = 0;
  for(int i = 0; i <= (int)BN.size(); ++i) {
    long long rv = 0;
    std::vector<long long> an(AN), bn(BN);
    rv += check(0, 0, i, an, bn);
    rv += check(1, i, BN.size(), an, bn);
    res = std::max(res, rv);
  }
  return res;
}
long long solve3()
{
  long long res = 0;
  for(int i = 0; i <= (int)BN.size(); ++i) {
    for(int j = i; j <= (int)BN.size(); ++j) {
      long long rv = 0;
      std::vector<long long> an(AN), bn(BN);
      rv += check(0, 0, i, an, bn);
      rv += check(1, i, j, an, bn);
      rv += check(2, j, BN.size(), an, bn);
      // std::cout << "i=" << i << ", j="  << j << ", " << rv << std::endl;
      res = std::max(res, rv);
    }
  }
  return res;
}
long long solve()
{
  if(AN.size() == 1) {
    return solve1();
  } else if(AN.size() == 2) {
    return solve2();
  } else {
    return solve3();
  }
}
int main()
{
  int T;
  std::cin >> T;
  for(int test = 1; test <= T; ++test) {
    std::cin >> N >> M;
    AN = std::vector<long long>(N);
    AT = std::vector<int>(N);
    BN = std::vector<long long>(M);
    BT = std::vector<int>(M);
    for(int i = 0; i < N; ++i) {
      std::cin >> AN[i] >> AT[i];
    }
    for(int i = 0; i < M; ++i) {
      std::cin >> BN[i] >> BT[i];
    }
    std::cout << "Case #" << test << ": " << solve() << std::endl;
  }
}

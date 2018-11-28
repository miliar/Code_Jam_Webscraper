/******************************************************************************

 @File Name : {PROJECT_DIR}/templ.cc

 @Creation Date : 07-05-2011

 @Last Modified : Sat 11 Jun 2011 10:53:59 PM CST

 @Created By: Zhai Yan

 @Purpose :
        template for gcj

*******************************************************************************/


#include <iostream>
#include <algorithm>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <deque>

using namespace std;

static bool is_square(const char* str, int len)
{
  long long res = 0;
  for (int i = 0; i < len; i++) {
    res *= 2;
    res += str[i] - '0';
  }

  //fprintf(stderr, "check %lld\n", res);
  long long sum = 0;
  for (sum = sqrt(res); sum * sum < res; sum += 2) {
    ;
  }
  //fprintf(stderr, "sum = %lld\n", sum);
  return sum * sum == res;
}

static bool try_search(char* num, int step, int n, char* bin_num)
{
  if (step >= n) {
    return is_square(bin_num, n);
  }
  if (num[step] == '?') {
    bin_num[step] = '1';
    if (try_search(num, step + 1, n, bin_num)) {
      return true;
    }
    bin_num[step] = '0';
    return try_search(num, step + 1, n, bin_num);
  } else {
    bin_num[step] = num[step];
    return try_search(num, step + 1, n, bin_num);
  }
}

static void solve(int t)
{
  char num[121];
  char bin_num[121];
  scanf("%s", num);
  try_search(num, 0, strlen(num), bin_num);
  bin_num[strlen(num)] = '\0';
  printf("%s", bin_num);
}


int main()
{
  int T;
  scanf("%d", &T);
  for (int i = 0; i < T; i++) {
    printf("Case #%d: ", i + 1);
    solve(i + 1);
    printf("\n");
  }
  return 0;
}






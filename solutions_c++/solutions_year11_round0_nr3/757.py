/******************************************************************************

 @File Name : {PROJECT_DIR}/templ.cc

 @Creation Date : 07-05-2011

 @Last Modified : Sat 07 May 2011 09:51:47 PM CST

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
#include <climits>

using namespace std;

template <typename T>
static void check_min(T& dst, T src) { if (dst > src)  dst = src; }

int array[2000];
static void solve(int t)
{
  int n;
  int wsum = 0;
  int tsum = 0;
  int min =  INT_MAX;

  scanf("%d", &n);
  for (int i = 0; i < n; i++) {
    scanf("%d", &array[i]);
    wsum ^= array[i];
    tsum += array[i];
    check_min(min, array[i]);
  }
  if (wsum != 0) {
    printf("NO");
  } else {
    printf("%d", tsum - min);
  }
}


int main()
{
  int T;
  scanf("%d", &T);
  for (int i = 0; i < T; i++) {
    printf("Case #%d: ", i + 1);
    solve(i + 1);
    printf("\n", i + 1);
  }
  return 0;
}






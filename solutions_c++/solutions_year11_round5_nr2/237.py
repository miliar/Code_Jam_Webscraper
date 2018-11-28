/******************************************************************************

 @File Name : {PROJECT_DIR}/templ.cc

 @Creation Date : 07-05-2011

 @Last Modified : Sat 11 Jun 2011 11:26:51 PM CST

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


static bool check(int* a, int s, int e)
{
  int tmp = a[s];
  //  fprintf(stderr, "check %d %d\n", s, e);
  for (int i = s + 1; i <= e; i++) {
    if (tmp != a[i] - 1) return false;
    ++tmp;
  }
  return true;
}

int list[1000][1000];
int list_count[1000];
int listn = 0;
static void solve(int t)
{
  int n;
  int a[1000];
  scanf("%d", &n);
  if (n == 0) {
    printf("0");
    return ;
  }

  for (int i = 0; i < n; i++) {
    scanf("%d", &a[i]);
  }
  std::sort(a, a+n);

  listn = 0;
  fill(list_count, list_count+n, 0);
  for (int i = 0; i < n; i++) {
    bool found =false;
    for (int j = listn - 1; j >= 0; j--) {
      int& last = list_count[j];
      if (list[j][last - 1] == a[i] - 1) {
        found = true;
        list[j][last++] = a[i];
        break;
      }
    }
    //fprintf(stderr, "found %d for %d\n", found, a[i]);
    if (!found) {
      list_count[listn] = 1;
      list[listn++][0]  = a[i];
    }
  }
  int large = n;
  for (int i = 0; i < listn; i++) {
    large = min(list_count[i], large);
  }
  printf("%d", large);
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






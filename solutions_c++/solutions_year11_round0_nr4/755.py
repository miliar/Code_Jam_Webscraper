/******************************************************************************

 @File Name : {PROJECT_DIR}/templ.cc

 @Creation Date : 07-05-2011

 @Last Modified : Sun 08 May 2011 12:20:31 AM CST

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
/*
static double f[1002];
static double p[1002][1002];
static double e[1002];
static bool mask[1002];

static void init_wperm()
{
  f[1] = 0;
  f[2] = 0.5;
  for (int i = 3; i < 1002; i++) {
    f[i] = (1 - 1.0 / i) * f[i - 1] + f[i - 2] / i;
  }
  double tmp = 1;
  for (int i = 0; i < 1002; i++) {
    if (i > 0) tmp *= i;
    for (int j = i + 1; j < 1002; j++) {
      p[i][j] = f[j - i] / tmp;
    }
    p[i][i] = 1 / tmp;
    for (int j = 1; j < i; j++)
      p[i][j] = 0;
  }
  fill(mask, mask + 1002, false);
  fprintf(stderr, "debug: p[0][1] = %lf\n p[0][2] = %lf\n p[1][1] = %lf\n",
      p[0][1], p[0][2], p[1][1]);
}

static double do_expect(int n)
{
  fprintf(stderr, "debug: do expect %d\n", n);
  if (mask[n]) return e[n];
  mask[n]        = true;
  double& result = e[n];
  result         = 0;
  if (n <= 0) {
    return result;
  }
  for (int i = 1; i <= n; i++) {
    result += (do_expect(n - i) + 1) * p[i][n];
  }
  result /= (1 - p[0][n]);
  return result;
}
*/


/*
 *  Algorithm description
 *
 *    let wp[n] be the number of the derangements of n elements
 *      wp[n] = (n - 1) * (wp(n - 1) + wp(n - 2)), wp[1] = 0, wp[2] = 1
 *
 *      So each time we permutate n elments, the chance we get i elements sorted
 *      would be p[n,i] =  c[n, i] * wp[n - i] / n! = wp[n - i] / i! / (n - i)!
 *      p[n,n] = 1/n!, here we let wp[0] = 1 to make this uniform
 *
 *      Then the expectation of sorting the unsorted elements would be computed as
 *      E[n] = (1 + p[n, 0] + p[n, 0]^2 + ...) * (sum(i, 1, n) (p[n, i] * E[n - i])) + 1
 *      E[1] = 0;
 *      E[0] = 0;
 *
 */
static const int kMax = 1001;
static double wp[kMax];
static double p[kMax][kMax];
static double e[kMax];
static double f[kMax]; /* n! */
static bool mask[kMax];

static void init()
{

  /*
   *  Init the factors
   */
  f[0] = 1;
  for (int i = 1; i < kMax; i++) {
    f[i] = f[i - 1] * i;
  }

  /*
   *  Init wp. Let wp'[i] = wp[i] / i!, this might save
   *  the precision
   */
  wp[1] = 0;
  wp[2] = 0.5;
  wp[0] = 1; /* see notes */

  for (int i = 3; i < kMax; i++) {
    wp[i] = (1 - 1.0/i) * wp[i - 1] + wp[i - 2] / i;
  }

  /*
   *  Init p array
   */
  for (int i = 0; i < kMax; i++) {
    for (int n = i; n < kMax; n++) {
      p[n][i] = wp[n - i] / f[i];
    }
    for (int n = 0; n < i; n++) {
      p[n][i] = 0; /* Not possible */
    }
  }

  /*
   *  Init e array's first two elements
   */
  fill(mask, mask + kMax, false);
  e[0]    = 0;
  e[1]    = 0;
  mask[0] = true;
  mask[1] = true;
}

/*
 *  Compute E array
 */
static double do_expect(int n)
{
  if (mask[n]) return e[n];
  mask[n]     = true;
  double& res = e[n];
  for (int i = 1; i <= n; i++) {
    res += do_expect(n - i) * p[n][i];
  }
  res++;
  res /= (1 - p[n][0]);
  return res;
}


static double expect(vector<int>& array)
{
  int n = array.size();
  vector<int> cpy (array.begin(), array.end());
  sort(cpy.begin(), cpy.end());
  for (int i = 0; i < cpy.size(); i++) {
    if (cpy[i] == array[i])
      n--;
  }
  return do_expect(n);
}


static void solve(int t)
{
  int n;
  scanf("%d", &n);
  vector<int> array(n);
  for (int i = 0; i < n; i++) {
    int tmp;
    scanf("%d", &tmp);
    array[i] = tmp;
  }
  printf("%.6lf\n", expect(array));
}


int main()
{
  int T;
  scanf("%d", &T);
  init();
  for (int i = 0; i < T; i++) {
    printf("Case #%d: ", i + 1);
    solve(i + 1);
    printf("\n", i + 1);
  }
  return 0;
}






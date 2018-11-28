#include <iostream>
#include <vector>

typedef long long int64;

using namespace std;
int gcd(int m, int n)
{
  int r = m % n;
  if (r == 0) {
    return n;
  } else {
    m = n;
    n = r;
    gcd(m, n);
  }
}

struct node {
  int64 n;
  int pd;
  int pg;
};

int parse(struct node *ptmp)
{
  //cout << ptmp->n << "," << ptmp->pd <<"," << ptmp->pg << endl;
  if (ptmp->pd == 0) {
    if (ptmp->pg == 100)
      return 0;
   return 1;
  }
  if (ptmp->pg == 100) {
    if (ptmp->pd == 100)
      return 1;
   return 0;
  }
  if (ptmp->pg == 0) {
    if (ptmp->pd == 0)
      return 1;
   return 0;
  }
/*

 else if (ptmp->pd == 0 && ptmp->pg == 100) {
    return 0;
  } else if (ptmp->pg == 0 && ptmp->pd != 0) {
    return 0;
  }
  if (ptmp->pg == 100 && ptmp->pd == 100) {
    return 1;
  } else if (ptmp->pg == 100 && ptmp->pd != 100) {
    return 0;
  }

*/
  //int64 tmp = (int64) (ptmp->pg / gcd(ptmp->pd, 100));
  int64 tmp = (int64) (100 / gcd(ptmp->pd, 100));
  //cout << tmp <<"aaaaa"<<gcd(80,100)<<endl;

  if (tmp <= ptmp->n) {
    return 1;
  }
  return 0;
}

int main()
{
  int i, j, k, n, total_case;
  cin >> total_case;
  struct node dp;
  for (int which_case = 1; which_case <= total_case; which_case++) {
    cin >> dp.n;
    cin >> dp.pd;
    cin >> dp.pg;
    int result = parse(&dp);
    if (result == 1)
      cout << "Case #" << which_case << ": Possible"<<endl;
    else if (result == 0)
      cout << "Case #" << which_case << ": Broken"<<endl;
  }
}

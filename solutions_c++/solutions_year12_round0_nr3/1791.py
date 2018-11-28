#include <iostream>
#include <string>
#include <sstream>
#include <set>
#include <vector>
#include <algorithm>
#include <cstdio>
#include <cstring>

using namespace std;

typedef pair<int,int> ii;
typedef vector<int> vi;
typedef vector<ii> vii;
typedef vector<vi> vvi;


inline int ndig (int n) {
  int result = 0;
  while (n) result++,n/=10;
  return result;
}

int powers[] = {1,1,10,100,1000,10000,100000,1000000};

int main (int argc, char *argv[]) {
  int n, result, a, b, ll;

  scanf ("%d",&n);
  for (int i = 1; i <= n; i++) {
    result = 0;

    scanf("%d %d",&a,&b);
    int l = ndig(a);
    for (int j = a; j <= b; j++) {

      int cdt_a = j;
      int current = j;
      for (int k = 0; k < l; k++) {
        current = (current%10)*powers[l] + current/10;
        if (current == cdt_a) break;
        if (current >= a && current <= b && current > cdt_a) {
          result++;
        }
      }

    }

    printf ("Case #%d: %d\n",i,result);
  }

  return 0;
}

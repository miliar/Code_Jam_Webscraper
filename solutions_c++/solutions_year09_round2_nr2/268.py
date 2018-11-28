#include <iostream>
#include <algorithm>
#include <sstream>
#include <cstring>
#include <math.h>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <queue>
using namespace std;
#define For(i,a,b) for (i = a; i != b; i++)
#define Rep(i,n) For(i,0,n)
#define set(a,c) memset(a,c,sizeof(a))
#define GI ({int t; scanf("%d",&t);t;})
#define pb push_back
char A[40];
main() {
  int t = GI;
  int cas;
  For(cas,1,t+1) {
    cout << "Case #" << cas << ": ";
    scanf("%s",A);
    int len = strlen(A);
    if (next_permutation(A,A+len)) {
      cout << A << endl;
    } else {
      sort(A,A+len);
      if (A[0] == '0') {
	int i;
	for (i = 0; i < len; i++) {
	  if (A[i] != '0') {
	    break;
	  }
	}
	swap(A[i],A[0]);
      }
      cout << A[0];
      cout << "0";
      for (int i = 1; i < len; i++) {
	cout << A[i];
      }
      cout << endl;
    }
  }
}

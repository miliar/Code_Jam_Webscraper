#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

bool inter(int p1x, int p1y, int p2x, int p2y, int p3x, int p3y, int p4x, int p4y) {
  //x座標によるチェック
  bool f;
    if (p1x >= p2x) {
        if ((p1x < p3x && p1x < p4x) || (p2x > p3x && p2x > p4x)) {
	  f = false;
	  return f;
	}
        if ((p2x < p3x && p2x < p4x) || (p1x > p3x && p1x > p4x)){
	  f = false;
	  return f;
	}
    }
    //y座標によるチェック
    if (p1y >= p2y) {
        if ((p1y < p3y && p1y < p4y) || (p2y > p3y && p2y > p4y)) {
	  f = false;
	  return f;
	}
    }else {
        if ((p2y < p3y && p2y < p4y) || (p1y > p3y && p1y > p4y)) {
	  f = false;
	  return f;
	}
    }
    
    if (((p1x - p2x) * (p3y - p1y) + (p1y - p2y) * (p1x - p3x)) * ((p1x - p2x) * (p4y - p1y) + (p1y - p2y) * (p1x - p4x)) > 0) {
      f = false;
      return f;
    }
    if (((p3x - p4x) * (p1y - p3y) + (p3y - p4y) * (p3x - p1x)) *  ((p3x - p4x) * (p2y - p3y) + (p3y - p4y) * (p3x - p2x)) > 0) {
      f = false;
      return f;
    }
    return true;
}

int main() {
  freopen("A.in","r",stdin);
  //freopen("A-large.out","w",stdout);
  //	freopen("A-small-attempt0.in","r",stdin);freopen("A-small-attempt0.out","w",stdout);
  //	freopen("A-small-attempt1.in","r",stdin);freopen("A-small-attempt1.out","w",stdout);
  int testcase;
  scanf("%d",&testcase);
  for (int caseId=1;caseId<=testcase;caseId++) {
    cout << "Case #" << caseId << ": ";
    int hon;
    cin >> hon;
    vector<int> A,B;
    for (int i = 0; i < hon; ++i) {
      int a,b;
      cin >> a;cin >>b;
      A.push_back(a);B.push_back(b);
    }
    int ah = 0;
    int bh = 1;
    int re = 0;
    for (int i = 0; i < (int)A.size(); ++i) {
      for (int j = i+1; j < (int)A.size(); ++j){
	if (inter(ah,A[i],bh,B[i],ah,A[j],bh,B[j])) re++;
      }
    }
    std::cout << re << std::endl;
  } 
  return 0;
}


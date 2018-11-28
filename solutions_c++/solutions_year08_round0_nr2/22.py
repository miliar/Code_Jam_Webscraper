#include <string>
#include <vector>
#include <cmath>
#include <cctype>
#include <queue>
#include <map>
#include <set>
#include <algorithm>
#include <iostream>
#include <sstream>
#include <utility>
#include <numeric>
#include <complex>

using namespace std;

int gettime(void)
{
  int h, m;
  scanf("%d:%d", &h, &m);
  return 60*h + m;
}

int main(void)
{
  int N;
  cin >> N;
  for (int c = 1; c <= N; c++) {
    int T; cin >> T;
    vector <int> NAB(2); cin >> NAB[0] >> NAB[1];
    vector <int> starts[2], ends[2];
    for (int ab = 0; ab < 2; ab++) {
      for (int i = 0; i < NAB[ab]; i++) {
	starts[ab].push_back(gettime());
	ends[ab].push_back(gettime());
      }
      sort(starts[ab].begin(), starts[ab].end());
      sort(ends[ab].begin(), ends[ab].end());
    }
    vector <int> ans = NAB;
    for (int ab = 0; ab < 2; ab++) {
      int cur_start = 0, cur_end = 0;
      while (cur_start < NAB[ab] && cur_end < NAB[1-ab]) {
	/*
	cout << cur_start << " " << starts[ab][cur_start] << endl;
	cout << cur_end << " " << ends[1-ab][cur_end] << endl;
	cout << endl;
	*/
	if (starts[ab][cur_start] >= ends[1-ab][cur_end] + T) {
	  ans[ab]--;
	  cur_end++;
	}
	cur_start++;
      }
    }
    printf("Case #%d: %d %d\n", c, ans[0], ans[1]);
  }
}

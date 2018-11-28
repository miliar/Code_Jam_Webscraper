#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <algorithm>
#include <cmath>
#include <cstdio>
#include <cstdlib>
using namespace std;

int main()
{
  int NN;
  scanf("%d", &NN);
  for (int ii = 0; ii < NN; ii++) {
    int N;
    scanf("%d", &N);
    vector<pair<int, int> > v;
    for (int i = 0; i < N; i++) {
      int a, b;
      scanf("%d %d", &a, &b);
      v.push_back(make_pair(a, b));
    }
    //for (int i = 0; i < N; i++) {
    //  printf("%d %d\n",v[i].first, v[i].second);
    //}
    int c = 0;
    for (int i = 0; i < N; i++) {
      for (int j = 0; j < N; j++) {
	if (i != j) {
	  if (v[i].first < v[j].first && v[i].second > v[j].second) {
	    c++;
	  }
	  else if (v[i].first > v[j].first && v[i].second < v[j].second) {
	    c++;
	  }
	}
      }
    }
    
    printf("Case #%d: %d\n", ii+1, c/2);
  }
  return 0;
}

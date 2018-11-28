//Tadrion
#include <cstdio>
#include <vector>
#include <iostream>
#include <deque>
#include <map>
#include <set>
#include <string>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <queue>
#include <stack>
#include <algorithm>
#include <utility>
#define MAX(a,b) ((a) > (b) ? (a) : (b))
#define MIN(a,b) ((a) < (b) ? (a) : (b))
#define LL long long
#define ST first
#define ND second
#define PII pair<int,int>
#define VI vector<int>

using namespace std;
int t,n,c;
vector <int> v,m;
int odw[1010];
int main() {
  scanf("%d",&t);
  for(int i = 1; i<=t; i++) {
    scanf("%d",&n);
    v.clear();
    m.clear();
    v.push_back(-1);
    for(int j = 1; j<= n; j++) {
      scanf("%d",&c);
      v.push_back(c);
    }
    for(int j = 1; j <= n; j++) {
      odw[j] = 0;
    }

    for(int j = 1; j<=n; j++) {
      if(odw[j] == 0) {
	odw[j] = 1;
	int k = v[j];
	int len = 1;
	while(k != j) {
	  odw[k] = 1;
	  k = v[k];
	  len++;
	}
	m.push_back(len);
      }
    }
    int sum = 0;
    for(int j = 0; j< m.size(); j++) {
      if(m[j] > 1) sum+=m[j];
    }
    float ff = sum;
    printf("Case #%d: %f\n",i,ff);
  }

  return 0;
}

#include <cstdio>
#include <climits>
#include <cstring>
#include <cctype>
#include <queue>
#include <sstream>
#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <string>

using namespace std;
typedef long long ll;

int ai[1000];
int len[100100];
ll dist[100100];


int main() {
  int ca;
  scanf(" %d", &ca);

  for (int ii = 0; ii < ca; ii++) {
    int L, t, N, C;
    scanf(" %d%d%d%d", &L, &t, &N, &C);


    for (int i = 0; i < C; i++) {
      scanf(" %d", ai + i);
      ai[i] *= 2;
    }


    ll sum = 0;    

    for (int i = 0; i < N; i++) {
      len[i] = ai[i % C];
      dist[i] = sum;
      sum += ai[i % C];
    }

    dist[N] = sum;

    ll maxv = 0;
    if (L == 2) {
      for (int i = 0; i < N; i++) {
	for (int j = i + 1; j < N; j++) {
	  ll dif = 0;
	  if (dist[i] >= t) {
	    dif = len[i] / 2;
	  } else if (dist[i + 1] > t) {
	    dif = (dist[i + 1] - t) / 2;
	  }
	  
	  if (dist[j] - dif >= t) {
	    dif += len[j] / 2;
	  } else if (dist[i + 1] - dif > t ) {
	    dif += dist[i + 1] - dif - t;
	  }
	  maxv = max(maxv, dif);
	}
      }
    } else if (L == 1) {
      for (int i = 0; i < N; i++) {
	ll dif = 0;
	if (dist[i] >= t) {
	  dif = len[i] / 2;
	} else if (dist[i + 1] > t) {
	  dif = (dist[i + 1] - t) / 2;
	}
	maxv = max(maxv, dif);
	
      }
    }
    //printf("%lld %lld\n", dist[N], maxv);
    printf("Case #%d: %lld\n", ii+1, dist[N] - maxv);

  }
}

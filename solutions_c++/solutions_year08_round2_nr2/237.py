#include <cstdio>
#include <cstring>
#include <map>
#include <vector>

using namespace std;

typedef unsigned long long ULL;

map<int, int> uni;

void init(int u) {
  if (uni.find(u) == uni.end()) {
    uni[u] = u;
  }
}

int parent(int u) {
  if (uni[u] == u) {
    return u;
  } else {
    return uni[u] = parent(uni[u]);
  }
}

void merge(int u, int v) {
  init(u);
  init(v);

  uni[parent(u)] = parent(v);
}

int go() {
  ULL A, B, P; scanf("%llu%llu%llu", &A, &B, &P);

  uni.clear();
  int cnt = 0;
  for(; A<=B; ++A) {
    ULL z=A;
    vector<int> u;
    if (!(z%2)) {
      if (2 >= P) {
	u.push_back(2);
      }
      while(!(z%2)) {
	z /= 2;
      }
    }
    for(ULL p=3; z>1; p+=2) {
      if (!(z%p)) {
	if (p >= P) {
	  u.push_back(p);
	}
	while(!(z%p)) {
	  z /= p;
	}
      }
    }
    if (u.empty()) {
      ++cnt;
    } else if (u.size() == 1) {
      init(u[0]);
    } else {
      for(int i=1, n=(int)u.size(); i<n; ++i) {
	merge(u[0], u[i]);
      }
    }
  }

  for(map<int, int>::iterator i=uni.begin(); i!=uni.end(); ++i) {
    if (i->first == i->second) {
      ++cnt;
    }
  }

  return cnt;
}

int main() {
  int T; scanf("%d", &T);
  for(int i=1; i<=T; ++i) {
    printf("Case #%d: %d\n", i, go()); 
  }
}

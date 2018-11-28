#include <algorithm>
#include <cassert>
#include <climits>
#include <cmath>
#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <stack>
#include <string>
#include <vector>

using namespace std;

#define tr(container, it)for(typeof(container.begin()) it = container.begin(); it != container.end(); it++) 
int inline ABS(int a){ return a>0?a:-a; }
typedef pair<int,int> pi;
typedef unsigned long long ULL;
typedef long long LL;

/* Main code starts from here */

struct ss {
  vector<int>list;
}G[1111];
int vis[1111];
int coun;
queue<int>Q;
int main() {
	int t,T;
	scanf("%d", &T);
	for (t=1; t<=T; t++) {
		int n;
		scanf("%d", &n); 
		coun = 0;
		memset(vis, 0, sizeof vis);
		for (int i = 0; i < n; i++) {
		  int m;
		  scanf("%d", &m);
		  G[i].list.clear();
		  for (int j = 0; j < m; j++) {
		    int a;
		    scanf("%d", &a);
		    G[i].list.push_back(a-1);
		  }
		}
		for (int i = 0; i < n; i++) {
		  memset(vis, 0, sizeof vis);
		  vis[i] = 1;
		  while (!Q.empty())Q.pop();
		  Q.push(i);
		  while (!Q.empty()) {
		    int u = Q.front(); Q.pop();
		    for (int j = 0; j < G[u].list.size(); j++) {
		      int v = G[u].list[j];
		      if (vis[v] == 1) coun = 1;
		      else vis[v] = 1, Q.push(v);
		    }
		  }
		}
		printf("Case #%d: ",t);
		if (coun == 1) puts("Yes");
		else puts("No");
	}
	return 0;
}

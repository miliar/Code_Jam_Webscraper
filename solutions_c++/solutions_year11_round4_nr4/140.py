#include <stdio.h>
#include <algorithm>
#include <iostream>
#include <stack>
#include <math.h>
#include <deque>
#include <queue>
#include <map>
#include <set>
#include <stdlib.h>
#include <memory.h>
using namespace std;
int _T;
int d[44];
vector<int> g[44];
int c,w;
int used[44];
int ans;

void rec(int x) {
  if (x == 1) {
    int cur = 0;
    for (int i=0;i<=c;i++)
      if (!used[i])
	 for (int j=0;j<g[i].size();j++)
	   if (used[ g[i][j] ]) {
	    cur++;
	    break;
	  }
    
    if (cur > ans) ans = cur;
    return;
  }
  
  used[x] = 1;
  for (int i=0;i<g[x].size();i++)
    if (d[ g[x][i] ] == d[x] - 1) {
      rec(g[x][i]);
    }
  used[x] = 0;
}

int main() {
	freopen("in","r",stdin);
	freopen("out","w",stdout);

	cin >> _T;
	for (int _t=1;_t<=_T;_t++) {
	  printf("Case #%d: ", _t);
	  
	  cin >> c >> w;
	  
	  ans = -1;
	  
	  for (int i=0;i<=c;i++) g[i].clear();
	  memset(d,63,sizeof(d));
	  
	  d[1] = 0;
	  
	  while (w--) {
	    int x,y; scanf("%d",&x);
	    char C = getchar();
	    while (C != ',') C = getchar();
	    cin >> y;
	    g[x].push_back(y);
	    g[y].push_back(x);
	  }
	  
	  queue<int> q;
	  q.push(1);
	  while (!q.empty()) {
	    int x = q.front(); q.pop();
	    for (int i=0;i<g[x].size();i++)
	      if (d[ g[x][i] ] > d[x] + 1) {
		d[ g[x][i] ] = d[x] + 1;
		q.push(g[x][i]);
	      }
	  }
	  
	  rec(0);
	  
	  cout << d[0] - 1 << ' ' << ans << endl; 
	}


	return 0;
}

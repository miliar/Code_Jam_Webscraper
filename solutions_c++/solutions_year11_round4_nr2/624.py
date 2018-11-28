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
struct cell {
  double x,y;
  
  cell operator -(const cell& A) const {
    cell T; T.x = x - A.x; T.y = y - A.y;
    return T;
  }
  
  cell operator +(const cell& A) const {
    cell T; T.x = x + A.x; T.y = y + A.y;
    return T;
  }
  
  cell operator *(const double& A) const {
    cell T; T.x = x * A; T.y = y * A;
    return T;
  }
} a[555][555];

double g[555][555];

int main() {
	freopen("in","r",stdin);
	freopen("out","w",stdout);

	cin >> _T;
	for (int _t=1;_t<=_T;_t++) {
	  printf("Case #%d: ", _t);
		
	  int n,m,d;
	  cin >> n >> m >> d;
	  
	  int Ans = 0;
	  for (int i=0;i<n;i++) {
	    for (int j=0;j<m;j++) {
	      char c = getchar();
	      while (c < '0' || c > '9') c = getchar();
	      a[i][j].x = ((double) i + 0.5);
	      a[i][j].y = ((double) j + 0.5);
	      a[i][j] = a[i][j];
	      g[i][j] = c - '0';
	    }
	  }
	  
	  for (int i=0;i<n;i++)
	     for (int j=0;j<m;j++)
		for (int k=max(3,Ans+1);i+k<=n && j+k<=m;k++) {
		  cell cent; 
		  cent.x = (double) i + (double) k / 2.0;
		  cent.y = (double) j + (double) k / 2.0;
		  
		  cell ans; ans.x = ans.y = 0;
		  for (int x=0;x<k;x++)
		    for (int y=0;y<k;y++) {
		      if (x == 0 && y == 0) continue; 
		      if (x == 0 && y == k-1) continue;
		      if (x == k-1 && y == 0) continue;
		      if (x == k-1 && y == k-1) continue;
		      ans = ans + ((a[i+x][j+y] - cent) * (double) g[i+x][j+y]);
		    }
		  if (fabs(ans.x) < 1e-8 && fabs(ans.y) < 1e-8) { 
		    Ans = k;
		    //cout << i << " " << j << " " << k;  
		  }
		}
	  
	  if (Ans == 0) cout << "IMPOSSIBLE" << endl;
	  else cout << Ans << endl;
	}


	return 0;
}

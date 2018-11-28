#include <algorithm>
#include <string>
#include <set>
#include <map>
#include <vector>
#include <queue>
#include <iostream>
#include <cmath>
#include <cstdio>
#include <cstdlib>

#define MP make_pair
#define ST first
#define ND second
#define PB push_back
#define LL long long
#define VII vector<int>
#define PII pair<int, int>

#define MAXN 505

using namespace std;

int t;
int n, m, D;

char tab[MAXN][MAXN];
int rowsums[MAXN][MAXN];
int fields[MAXN][MAXN];


int get(int x, int y){
  return tab[x][y]-'0';
}

bool xcm(int x, int y, int k){
    double cm = 0.0;
    for(int i = x; i <= x+k-1; i++){
      for(int j = y; j <= y+k-1; j++){
	cm += (get(i,j))*(x+ 1.0 * k / 2.0 - 0.5 - i * 1.0);
      }
    }
    
    cm -= (get(x,y))*(x+ 1.0 * k / 2.0 - 0.5 - x * 1.0);
    cm -= (get(x,y+k-1))*(x+ 1.0 * k / 2.0 - 0.5 - x * 1.0);
    cm -= (get(x+k-1,y))*(x+ 1.0 * k / 2.0 - 0.5 - (x+k-1) * 1.0);
    cm -= (get(x+k-1,y+k-1))*(x+ 1.0 * k / 2.0 - 0.5 - (x+k-1) * 1.0);
    if(cm <= 1e-9 && cm >= -1e-9) return true;
    else return false;
}

bool ycm(int x, int y, int k){
    double cm = 0.0;
    for(int i = x; i <= x+k-1; i++){
      for(int j = y; j <= y+k-1; j++){
	cm += (get(i,j))*(y+ 1.0 * k / 2.0 - 0.5 - j * 1.0);
      }
    }
    
    cm -= (get(x,y))*(y+ 1.0 * k / 2.0 - 0.5 - y * 1.0);
    cm -= (get(x,y+k-1))*(y+ 1.0 * k / 2.0 - 0.5 - (y+k-1) * 1.0);
    cm -= (get(x+k-1,y))*(y+ 1.0 * k / 2.0 - 0.5 - y * 1.0);
    cm -= (get(x+k-1,y+k-1))*(y+ 1.0 * k / 2.0 - 0.5 - (y+k-1) * 1.0);
    if(cm <= 1e-9 && cm >= -1e-9) return true;
    else return false;
}


int main(){
    scanf("%d", &t);
    for(int testcase = 1; testcase <= t; testcase++){
	scanf("%d %d %d", &n, &m, &D);
	
	for(int i = 0; i < n; i++){
	    scanf("%s", tab[i]);
	}
	
	int res = -1;
	int i0, j0;
	for(int k = min(m, n); k >= 3; k--){
	    for(int i = 0; i <= n-k; i++){
		for(int j = 0; j <= m-k; j++){
		    if(xcm(i,j,k) && ycm(i,j,k))
		    {
		      res = k;
		      i0 = i; j0 = j;
		    }
		    if(res != -1) break;
		}
		if(res != -1) break;
	    }
	    if(res != -1) break;
	}
	
	if(res != -1) printf("Case #%d: %d\n", testcase, res);
	else printf("Case #%d: IMPOSSIBLE\n", testcase);
    }
    return 0;
}
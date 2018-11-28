#include <map>     
#include <set>     
#include <cmath>    
#include <cstdio>   
#include <vector>     
#include <string>     
#include <sstream>    
#include <iostream>    
#include <algorithm>     
using namespace std;     
#define FOR(i,a,b) for(int i=(a); i<(b); ++i)     
#define FORE(it,x) for(typeof(x.begin()) it=x.begin(); it!=x.end(); ++it)     
#define SET(x, v) memset(x, v, sizeof (x))     
#define sz size()     
#define cs c_str()     
#define pb push_back     
#define mp make_pair    
 
typedef long long i64;     
 bool chk[128][128];
 int qu[128*128*2][2];
 int front,rear;
int main() {

	freopen("B.in","r",stdin);
	int e = 0, T, n;
	int W, H;
	int x1, y1, x2, y2;
	int a, b;
	scanf("%d",&T);

	while(T--) {
		scanf("%d%d",&W,&H);
		scanf("%d%d",&x1,&y1);
		scanf("%d%d",&x2,&y2);
		SET(chk,0);
		scanf("%d%d",&a,&b);
		chk[a][b] = 1;
		front = rear = 0;
		qu[rear][0] = a;
		qu[rear++][1] = b;
		for(;front<rear;front++) {
			int x = qu[front][0];
			int y = qu[front][1];
			int px = x + x1;
			int py = y + y1;
			if(px>=0 && py>=0 && px<W && py<H && !chk[px][py]) {
				chk[px][py] = 1;
				qu[rear][0] = px;
				qu[rear++][1] = py;
			}
			px = x + x2;
			py = y + y2;
			if(px>=0 && py>=0 && px<W && py<H && !chk[px][py]) {
				chk[px][py] = 1;
				qu[rear][0] = px;
				qu[rear++][1] = py;
			}
		}
		printf("Case #%d: %d\n",++e, rear);
	}


	return 0;
}



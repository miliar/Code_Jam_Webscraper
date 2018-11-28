#include <iostream>
#include <algorithm>
#include <cstring>
#include <vector>
#include <string>
#include <cmath>
#include <queue>
#include <map>
using namespace std;
const int M = 210;
const int inf = 1000000000;
const double eps = 1e-10;

char g[M][M];
struct Node{
	int tot;
	int win;
}p[M];

struct Point{
	double a, b, c;
}outt[M];
int n;
double work(int i, int j){
	Node t = p[j];
	if(g[j][i] != '.'){
		t.tot --;
		if(g[j][i] =='1')
			t.win --;
	}
	if(t.tot == 0) return 1;
	else return t.win *1.0 / t.tot;
}
void solve(){
	scanf ("%d", &n);
	int i, j;
	for(i  = 0; i < n; i ++){
		scanf ("%s",g[i]);
		p[i].tot= p[i].win = 0;
		for(j= 0;  j < n; j ++){
			if(g[i][j] != '.'){
				p[i].tot ++;
				if(g[i][j] == '1')
					p[i].win++;
			}
		}
		if(p[i].tot == 0) outt[i].a = 1;
		else outt[i].a = p[i].win*1.0/p[i].tot;
	}
	int cnt ;
	for(i = 0; i < n;i ++){
		outt[i].b = 0;
		cnt = 0;
		for(j = 0; j < n; j ++){
			if(i == j || g[i][j] =='.')
				continue;
			outt[i].b += work(i, j);
			cnt ++;
		}
		outt[i].b /= cnt;
	}
	for(i = 0; i < n; i ++){
		cnt = 0;
		outt[i].c = 0;
		for(j = 0; j < n; j ++){
			if(i == j || g[i][j] =='.')
				continue;
			outt[i].c += outt[j].b;
			cnt ++;
		}
		outt[i].c /= cnt;
	}
	double t;
	for(i = 0; i < n;i ++){
		t = outt[i].a *0.25 + outt[i].b*0.5 + outt[i].c *0.25;
		printf ("%.10lf\n", t);
	}
}
int main()
{
	int cas;
	int i;
	freopen("A-large.in","r", stdin);
	freopen("A.out","w", stdout);
	scanf ("%d", &cas);

	for(i = 1; i <= cas; i ++){
		printf ("Case #%d:\n", i);
		solve();
	}
	return 0;
}
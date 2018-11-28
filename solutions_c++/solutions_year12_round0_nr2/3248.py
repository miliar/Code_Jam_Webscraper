#include <iostream>
#include <stdio.h>
#include <fstream>
#include <string>
#include <vector>
#include <queue>
using namespace  std;
struct triple{
	int s1, s2, s3;
	bool sup;
};
vector<vector<triple> > v;
struct node{
	int cur;
	int sup;
	int v;
}N, P;
int dp[110][110];
int sum[110];
int s;
int n;
int p;
int casid = 0;
void bfs()
{
	triple curv;
	memset(dp, -1, sizeof(dp));
	N.cur = 0; 
	N.sup = s;
	N.v = 0;
	dp[N.cur][N.sup] = 0;
	queue<node> Q;
	Q.push(N);
	while(!Q.empty()) {
		N = Q.front();
		Q.pop();
		if(dp[N.cur][N.sup] != N.v || N.cur == n) continue;
		for(int j = 0; j < v[sum[N.cur]].size(); ++j) {
			curv = v[sum[N.cur]][j];
			if(curv.sup ) {
				if(N.sup  > 0 ) {
					P.sup = N.sup - 1;
					P.cur = N.cur + 1;
					if(curv.s3 >= p) {
						P.v = N.v + 1;
					}else P.v = N.v;
					if(dp[P.cur][P.sup] < P.v) {
						dp[P.cur][P.sup] = P.v;
						Q.push(P);
					}
				}
			}else {
				P.sup = N.sup;
				P.cur = N.cur + 1;
				if(curv.s3 >= p) {
					P.v = N.v + 1;
				}else P.v = N.v;
				if(dp[P.cur][P.sup] < P.v) {
					dp[P.cur][P.sup] = P.v;
					Q.push(P);
				}
			}
		}
	}
	printf("Case #%d: %d\n", ++casid, dp[n][0]);
}
void dancing()
{

// 	freopen(".\\B-small-attempt1.in","r", stdin);
// 	freopen(".\\B-samll-attempt1.out", "w", stdout);
// 
 	freopen(".\\B-large.in","r", stdin);
 	freopen(".\\B-large.out", "w", stdout);
	
	int t;
	v.resize(32);
	for(int i = 0; i < 31; ++i)
		v[i].clear();
	triple tri;
	for(int i = 0; i <= 10; ++i) {
		for(int j = i; j <= 10; ++j) {
			for(int k = j ; k <= 10; ++k) {
				if(k - i > 2) break;
				tri.s1 = i;
				tri.s2 = j;
				tri.s3 = k;
				tri.sup = ( k - i == 2 )? true:false;
				v[i+j+k].push_back(tri);
			}
		}
	}

// 	for(int i= 0; i <= 30; i ++ ) {
// 		for(int j = 0; j < v[i].size(); ++j)
// 			cout<<v[i][j].s1 << " " << v[i][j].s2 << " "<<v[i][j].s3 <<" ";
// 		cout<<endl;
// 	} 
	scanf("%d", &t);
	while(t--) {
		scanf("%d %d %d", &n, &s, &p);
		for(int i = 0; i < n;  i ++)
			scanf("%d", &sum[i]);
		bfs();
	}
}
int main()
{
	dancing();
	
	
	
}
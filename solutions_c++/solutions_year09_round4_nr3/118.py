#include  <cstdio> 
#include  <cstdlib> 
#include  <cstring> 
#include  <string> 
#include  <vector> 
#include  <cmath> 
#include  <algorithm> 
#include  <cassert> 
#include  <set> 
#include  <map> 
#include  <queue> 
#include  <iostream> 
#include <fstream> 
using namespace std; 
#define pb push_back 
#define REP(i,n) for(int i=0;i<(n);i++ )  

typedef long long LL; 
typedef pair<int,int> pii; 

int g[120][120];
int num[120][120];
int N, K;

int over(int i, int j)
{
	REP(t, K)
		if (num[i][t] >= num[j][t])
			return false;
	return true;
	
}


//二分图最大匹配,hungary算法,邻接阵形式,复杂度O(m*m*n)
//返回最大匹配数,传入二分图大小m,n和邻接阵mat,非零元素表示有边
//match1,match2返回一个最大匹配,未匹配顶点match值为-1
const int MAXN = 120;
#define _clr(x) memset(x, 0xff, sizeof(int) * MAXN)
int match1[MAXN], match2[MAXN];
int mat[MAXN][MAXN];

int hungary(int m) {
	int n = m;
	int s[MAXN + 1], t[MAXN], p, q, ret = 0, i, j, k;
	_clr(match1);
	_clr(match2);
	for (i = 0; i < m; ret += (match1[i++] >= 0)) {
		_clr(t);
		for (s[p = q = 0] = i; p <= q && match1[i] < 0; p++) {
			k = s[p];
			for (j = 0; j < n && match1[i] < 0; j++) {
				if (mat[k][j] && t[j] < 0) {
					s[++q] = match2[j];
					t[j] = k;
					if (s[q] < 0) {
						for (p = j; p >= 0; j = p) {
							match2[j] = k = t[j];
							p = match1[k];
							match1[k] = j;
						}
					}
				}
			}
		}
	}
	return ret;
}

int main()
{
	int cases;
	scanf("%d", &cases);
	REP(caseIndex, cases)
	{
		//int res = 0;
		cin>>N>>K;
		REP(i,N)
			REP(j,K)
				cin>>num[i][j];
		REP(i,N)
			REP(j,N)
		{
				mat[i][j] = over(i,j);
			//cout<<i<<' '<<j<<' '<<g[i][j]<<endl;
		}
		int R = hungary(N);
		//cerr<<R<<endl;
		printf("Case #%d: %d\n", caseIndex + 1,N - R);
	}
}

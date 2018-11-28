#include <stdio.h>
#include <vector>
#include <limits.h>
#define MQ 102
#define min(a,b) (((a)<(b))?(a):(b))
using namespace std;
vector<int> d;
int c[MQ][MQ], _c[MQ][MQ];
int C(int i, int j)
{
	if (j-i <= 1) return 0;
	if (_c[i][j]) return c[i][j];
	_c[i][j] = 1; c[i][j] = INT_MAX;
	for (int k = i+1; k < j; k++)
		c[i][j] = min(C(i,k)+C(k,j),c[i][j]);
	c[i][j] += d[j]-d[i]-2;
//	printf("c(%d,%d) = %d\n", i, j, c[i][j]);
	return c[i][j];
}
int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int t, T, P, Q, i;

	scanf("%d",&T);
	for (t = 1; t <= T; t++) {
		d.clear(); d.push_back(0);
		for (scanf("%d%d",&P,&Q); Q--;) {
			scanf("%d",&i);
			d.push_back(i);
		}
		d.push_back(P+1);
		memset(c,0,sizeof(c));
		memset(_c,0,sizeof(_c));
		printf("Case #%d: %d\n",t,C(0,d.size()-1));
	}
	return 0;
}
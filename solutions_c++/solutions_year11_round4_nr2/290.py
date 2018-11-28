#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <cassert>
#include <algorithm>
#include <limits>
#include <vector>
#include <queue>
#include <map>
#include <set>
#include <list>
#include <string>
#include <complex>
using namespace std;
typedef long long ll;
typedef pair<int,int> pii;
typedef complex<int> pt;
const int INF = numeric_limits<int>::max();

const int nmax = 505;
char buf[nmax];
int w[nmax][nmax];
pt cc[nmax][nmax];
int sw[nmax][nmax];
pt sc[nmax][nmax];
int R, C, D;

bool checkcom(int r, int c, int k)
{
	int bw = 0;
	pt bc;
	for(int i=r;i<=r+k;i++)
		for(int j=c;j<=c+k;j++)
		{
			bw += w[i][j];
			bc += cc[i][j];
		}
	bw = bw-w[r+k][c+k]-w[r+k][c]-w[r][c+k]-w[r][c];
	bc += -cc[r+k][c+k]-cc[r+k][c]-cc[r][c+k]-cc[r][c];
	if(bw == 0)
		return true;
	//printf("%d %d %d: %d %d %d\n", r, c, k+1, bw, bc.real(), bc.imag());
	if(bw * k % 2 == 1)
		return false;
	return (bc == pt(bw*r+bw*k/2, bw*c+bw*k/2));
}

int test()
{
	for(int k=min(R, C); k>=3; k--)
		for(int i=0;i<=R-k;i++)
			for(int j=0;j<=C-k;j++)
			{
				if(checkcom(i, j, k-1))
					return k;
			}
	return -1;
}

int main(int argc,char* argv[])
{
    int num_test_cases;
    scanf("%d",&num_test_cases);
    for(int test_case=1; test_case<=num_test_cases; test_case++)
    {
		memset(sw, 0, sizeof(sw));
		memset(sc, 0, sizeof(sc));
		
		scanf("%d%d%d", &R, &C, &D);
		for(int i=0;i<R;i++)
		{
			scanf(" %s", buf);
			for(int j=0;j<C;j++)
				w[i][j] = buf[j]-'0';
		}
		for(int i=0;i<R;i++)
			for(int j=0;j<C;j++)
			{
				cc[i][j] = w[i][j]*pt(i, j);
				sw[i+1][j+1] = sw[i][j+1]+sw[i+1][j]-sw[i][j]+w[i][j];
				sc[i+1][j+1] = sc[i][j+1]+sc[i+1][j]-sc[i][j]+cc[i][j];
			}

		printf("Case #%d: ",test_case);
		int k = test();
		if(k<0)
			printf("IMPOSSIBLE\n");
		else
			printf("%d\n", k);
    }
    return 0;
}

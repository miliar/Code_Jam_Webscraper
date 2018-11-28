#pragma comment(linker,"/STACK:16000000")

#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <set>
#include <map>

using namespace std;

#define nul(a) memset(a,0,sizeof(a))
#define fil(a,b) memset(a,b,sizeof(a))
#define cpy_to(a,b) memcpy(b,a,sizeof(a))
#define lld "%I64d"
const int mod = 10007;
int a[100][100];
void solve()
{
	int n, m, r;
	scanf("%d%d%d",&n , &m, &r);
	nul(a);
	for (int i = 0; i < r; i++){
		int x,y;
		scanf("%d%d",&x, &y);
		a[x-1][y-1] = -1;
	}
	for (int i = 0; i < n; i++)
		for (int j = 0; j < m; j++){
			if (i==0 && j==0){
				a[i][j] = 1;
				continue;
			}
			if (a[i][j] == -1)
				continue;
			a[i][j] = 0;
			if (i - 2>=0 && j-1>=0)
				a[i][j]+= max(0, a[i-2][j-1]);
			if (i - 1>=0 && j-2>=0)
				a[i][j]+= max(0, a[i-1][j-2]);
			a[i][j] %= mod;
		}
	printf("%d", a[n-1][m-1]);
}

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int nTests;
	scanf("%d", &nTests);
	for (int iTest = 1; iTest <= nTests; iTest++){
		printf("Case #%d: ", iTest);
		solve();
		printf("\n");
	}
	return 0;
}
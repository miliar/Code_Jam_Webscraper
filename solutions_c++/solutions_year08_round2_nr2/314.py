#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <sstream>
#include <map>
#include <set>
#include <cmath>
#include <queue>
#include <stack>
#include <list>
#include <numeric>
#include <bitset>
#include <ext/algorithm>
#include <ext/numeric>
#define fr(_a,_f,_t) for(int _a=(_f),__t=(_t);_a<__t;_a++)
#define fo(_a,_n) fr(_a,0,_n)
#define all(_v) (_v).begin(),(_v).end()
#define sz size()
typedef long long LL; using namespace std; using namespace __gnu_cxx; 

bitset<1001> c[1001];
bool G[1001][1001];
bool used[1001];
int C, A, B, P;

void dfs(int x)
{
	//printf("--visiting %d (A = %d, B = %d)\n", x, A, B);
	used[x] = true;
	for (int i = A; i <= B; ++i)
		if (G[x][i] && !used[i]) dfs(i);
}

int main()
{	
	scanf("%d", &C);
	for (int test = 1; test <= C; ++test)
	{
		scanf("%d %d %d", &A, &B, &P);
		
		memset(G,0,sizeof G);
		for (int i = 0; i <= 1000; i++) c[i].reset();
		
		for (int i = 1; i <= 1000; ++i)
		{
			int k = i;
			for (int j = 2; j <= i; ++j)
			{
				if ((k % j) > 0) continue;
				if (j >= P) c[i].set(j);
				while ((k % j) == 0) k /= j;
			}
		}
		
		for (int i = A; i < B; ++i)
			for (int j = i + 1; j <= B;	++j)
			{
				G[i][j] = G[j][i] = (c[i] & c[j]).any();
				//if (G[i][j]) printf("in rel %d %d\n", i, j);
			}
		//if (G[15][10]) printf("AHAA");
		
		memset(used, 0, sizeof used);
		int res = 0;
		for (int i = A; i <= B; ++i) if (!used[i]) {
			//printf("dfs on %d\n", i);
			dfs(i); ++res;
		}
		printf("Case #%d: %d\n", test, res);
	}
	return 0;
}

#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
 
using namespace std;
 
#define RP(a,h) for(a=0; a<(h); a++)
#define FR(a,l,h) for(a=(l); a<=(h); a++)
#define GMAX(X, Y) ((X) > (Y) ? (X) : (Y))
#define GMIN(X, Y) ((X) < (Y) ? (X) : (Y))
#define SZ(a) (LL)a.size()
#define ALL(a) a.begin(), a.end()
#define pb push_back
typedef vector <int> VI;
typedef vector <string> VS;
typedef pair<int, int> PII;
#define LL long long

const int INF = 100000000;
const int MAX = 105;

bool dfs(int n1,int n2,int a[][MAX],int m1[],int m2[],bool v1[],bool v2[],int x){v1[x]=true;int i;RP(i,n2)if(a[x][i]&&!v2[i]){v2[i]=true;int y=m2[i];if(y==-1){m2[i]=x;m1[x]=i;return true;}else{if(!v1[y]&&dfs(n1,n2,a,m1,m2,v1,v2,y)){m2[i]=x;m1[x]=i;return true;}}}return false;}
bool pushflow(int n1,int n2,int a[][MAX],int m1[],int m2[]){bool v1[MAX];bool v2[MAX];memset(v1,false,sizeof(v1));memset(v2,false,sizeof(v2));int i;RP(i,n1)if(m1[i]==-1&&!v1[i]&&dfs(n1,n2,a,m1,m2,v1,v2,i))return true;return false;}
int bipartite(int n1,int n2,int a[][MAX],int m1[],int m2[]){int i;RP(i,n1)m1[i]=-1;RP(i,n2)m2[i]=-1;int nmatch=0;while(pushflow(n1,n2,a,m1,m2))nmatch++;return nmatch;}

int n, k, ans;
int price[MAX][MAX];

bool isLower(int x, int y)
{
	int i;
	RP(i, k) if (price[x][i] >= price[y][i]) return false;
	return true;
}

void process()
{
	int a[MAX][MAX];
	int m1[MAX], m2[MAX];
	memset(a, false, sizeof(a));
	memset(m1, 0, sizeof(m1));
	memset(m2, 0, sizeof(m2));
	int i, j;
	RP(i, n) RP(j, n) if (isLower(i, j)) a[i][j] = 1;
	int w = bipartite(n, n, a, m1, m2);
	ans = n - w;
}

int main()
{
	//freopen("sample.in", "r", stdin); //freopen("sample.out", "w", stdout);
	//freopen("C-small-attempt0.in", "r", stdin); freopen("C-small-attempt0.out", "w", stdout);
	freopen("C-large.in", "r", stdin); freopen("C-large.out", "w", stdout);

	int tc, testcase, i, j;
	cin >> tc;

	RP(testcase, tc)
	{
		cin >> n >> k;
		RP(i, n)
		{
			RP(j, k) cin >> price[i][j];
		}
		process();
		printf("Case #%d: %d\n", (testcase+1), ans);
	}

	return 0;
}

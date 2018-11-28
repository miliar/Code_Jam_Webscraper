#include <vector> 
#include <map> 
#include <set> 
#include <deque> 
#include <queue> 
#include <stack> 
#include <bitset> 
#include <algorithm> 
#include <functional> 
#include <utility> 
#include <complex> 
#include <sstream> 
#include <iostream> 
#include <cstdio> 
#include <cmath> 
#include <cstdlib> 
#include <cstring> 
#include <cassert> 
using namespace std;

#define SZ(X) ((int)(X.size()))
#define PB(X) push_back(X)
#define two(X) (1<<(X))
#define MP make_pair
#define FILL(a, b) memset(a, b, sizeof(a))
#define ALL(X) (X).begin(), (X).end()
#define IT iterator

typedef long long LL;
const double pi = acos(-1.0);

char a[110][100];
int m;
int state[110][27];
int tst, T, n;
char que[30];

int calc(int p) {
	vector < int > Q;Q.clear();
	int vis[27];
	memset(vis, 0, sizeof(vis));
	for(int i = 0; i < n; ++i) 
		if(state[i][26] == state[p][26]) {
			Q.PB(i);
			for(int j = 0; j < 26; ++j)
				if(state[i][j]>0)
					vis[j]++;
		}
		
	int res = 0;
	for(int i = 0; i < 26; ++i) {
		if(Q.size() == 1) break;
		if(!vis[que[i]-'a']) continue;
		if(state[p][que[i]-'a'] == 0) {
			res++;
			for(int j = 0; j < Q.size(); ++j)
				if(state[Q[j]][que[i]-'a'] != 0) {
					for(int k = 0; k < 26; ++k) if(state[Q[j]][k]>0)
					vis[k]--;
					Q.erase(Q.begin()+j,Q.begin()+j+1);
					j--;
				}
				
			continue;
		}
		for(int j = 0; j < Q.size(); ++j)
			if(state[Q[j]][que[i]-'a'] != state[p][que[i]-'a']) {
				for(int k = 0; k < 26; ++k) if(state[Q[j]][k]>0)
					vis[k]--;
				Q.erase(Q.begin()+j,Q.begin()+j+1);
				j--;
			}
	}
	return res;
}

void work() {
	scanf("%d%d", &n, &m);
	for(int i = 0; i < n; ++i) 
		scanf("%s", a[i]);
	memset(state, 0, sizeof(state));
	
	for(int i = 0; i < n; ++i) {
		int l = state[i][26] = strlen(a[i]);
		for(int j = 0; j < l; ++j)
			state[i][a[i][j]-'a'] |= two(j);
	}
	
	for(int i = 0; i < m; ++i) {
		scanf("%s", que);
		int k = -1, sc = 0;
		for(int j = 0; j < n; ++j) {
			int tmp = calc(j);
			if(tmp > sc || k == -1) {
				k = j;
				sc = tmp;
			}
		}
		printf("%s", a[k]);
		if(i == m-1) puts("");
		else printf(" ");
	}
}

int main()
{
	freopen("b.in", "r", stdin);
	freopen("b.out", "w", stdout);
	scanf("%d", &T);
	while(tst < T) {
		printf("Case #%d: ", ++tst);
		work();
	}
	
	return 0;
}

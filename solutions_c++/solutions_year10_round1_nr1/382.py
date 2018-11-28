#include<cstdio>
#include<cstdlib>
#include<cmath>
#include<iostream>
#include<sstream>
#include<string>
#include<vector>
#include<set>
#include<queue>
#include<deque>
#include<map>
#include<functional>
#include<algorithm>

using namespace std;

#define REP(i,n) for(int i=0; i<(n); i++)
#define FOREACH(i,x) for(typeof(x)::iterator it=(x).begin(); it!=(x).end(); ++it)
#define EACH(i,x) REP(i,(x).size())
#define sz	size()
#define all(x) (x).begin(), (x).end()
#define sqr(x) ((x)*(x))
#define pb	push_back
#define mp	make_pair
#define eps	1e-15
#define inf 0x3FFFFFFF

typedef long long int lint;
typedef vector<int> vi;
typedef vector<string> vs;
typedef pair<int, int> pii;

char m1[60][60];
char m2[60][60];
int n;

bool find(char c, int k)
{
	REP(i, n) REP(j,n) {
		if(m2[i][j] != c) continue;

		int kk = 1;
		for(int l=i+1; l<n; l++) {
			if(m2[l][j] == c) kk++;
			else break;
		}
		if (kk >= k) return true;
		kk = 1;
		for(int l=j+1; l<n; l++) {
			if(m2[i][l] == c) kk++;
			else break;
		}
		if (kk >= k) return true;
		int ii = i+1;
		int jj = j+1;
		kk = 1;
		while( ii<n && jj < n ) {
			if(m2[ii][jj] == c) kk++;
			else break;
			ii++; jj++;
		}
		if (kk >= k) return true;
		ii = i+1;
		jj = j-1;
		kk = 1;
		while( ii<n && jj >=0 ) {
			if(m2[ii][jj] == c) kk++;
			else break;
			ii++; jj--;
		}
		if (kk >= k) return true;

	}
	return false;
}

void solve()
{
	int k;
	scanf("%d%d",&n, &k);

	REP(i,n) scanf("%s",m1[i]);

	REP(i,n)REP(j,n) m2[j][i] = m1[i][j];
	REP(j,n) {
		int pos = n - 1;
		for(int i=n-1; i>0; i--) {
			if (m2[i][j] != '.') continue;
			pos = min(pos, i - 1);
			while(pos >= 0) {
				if (m2[pos][j] != '.') {
					m2[i][j] = m2[pos][j];
					m2[pos][j] = '.';
					break;
				}
				pos--;
			}			
		}
	}
	bool red = find('R', k);
	bool blue = find('B', k);

	if(red&&blue) printf("Both\n");
	else if (red) printf("Red\n");
	else if (blue) printf("Blue\n");
	else printf("Neither\n");
}


int main(void)
{
	int test;
	scanf("%d",&test);
	REP(i,test) {
		printf("Case #%d: ", i + 1);
		solve();
	}
	return 0;
}


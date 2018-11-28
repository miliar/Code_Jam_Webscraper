#include <algorithm>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>

#define SIZE(a) ((int)((a).size()))
#define ALL(a) (a).begin(),(a).end()
#define FILL(a) memset(&a,0,sizeof(a))
#define PB push_back
#define MP make_pair
#define FOR(i,a,b) for (int i = (int)(a); i < (int)(b); ++i)
#define REP(i,a) for (int i = 0; i < (int)(a); ++i)
typedef long long LL;

using namespace std;

int n, k;
int pr[100][100];
bool le[100][100];
int nom[100], p[100];
bool v[100];

bool fin(int k){
	if (v[k])
		return false;
	v[k] = true;
	REP(i,n){
		if (le[k][i] && (p[i] == -1 || fin(p[i]))){
			p[i] = k;
			return true;
		}
	}
	return false;
}

int main(){
	freopen("c.in","r",stdin);
	freopen("c.out","w",stdout);
	int tc;
	scanf("%d",&tc);
	REP(it,tc){
		printf("Case #%d: ", it+1);
		scanf("%d%d", &n, &k);
		REP(i,n){
			REP(j,k){
				scanf("%d", &pr[i][j]);
			}
		}
		FILL(le);
		REP(i,n){
			REP(j,n){
				bool fl = true;
				REP(l,k)
					fl &= pr[i][l] < pr[j][l];
				le[i][j] = fl;
			}
		}
		REP(i,100)
			p[i] = -1;
		int c = 0;
		REP(i,n){
			FILL(v);
			if (fin(i))
				++c;
		}
		cout << n - c << "\n";
	}
}

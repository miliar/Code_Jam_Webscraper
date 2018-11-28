#include<cstdio>
#include<cstdlib>
#include<cmath>
#include<iostream>
#include<sstream>
#include<vector>
#include<set>
#include<string>
#include<map>
#include<algorithm>


using namespace std;

#define REP(i,n) for(int i=0; i<(n); i++)
#define EACH(i,x) REP(i,(x).size())
#define sz	size()
#define all(x) (x).begin(), (x).end()
#define mp make_pair
#define pb push_back
#define eps	1e-15

typedef vector<int> vi;
typedef vector<string> vs;
typedef long long int lint;

bool solve()
{
	int n, m;
	vector<int> favor[2000];
	int malted[2000];
	int result[2000];
	int degree[2000];
	bool select[2000];

	memset(result, 0, sizeof(result));
	memset(degree, 0, sizeof(degree));
	memset(malted, -1, sizeof(malted));
	memset(select, 0, sizeof(select));
	scanf("%d%d",&n,&m);
	REP(i,m) {
		int t;
		scanf("%d", &t);
		REP(j, t){
			int t1, t2;
			scanf("%d%d",&t1,&t2);
			t1--;
			if (t2) malted[i] = t1;
			else favor[i].pb(t1);
		}
	}
	bool changed = true;

	while(changed)
	{
		changed = false;
		REP(i,m) {
			if (select[i]) continue;
			if (malted[i] != -1 && result[malted[i]]) {
				select[i] = true;
				continue;
			}
			bool flag = false;

			EACH(j, favor[i]) {
				if (!result[favor[i][j]]) {
					flag = true;
					break;
				}
			}
			if (!flag) {
				if (malted[i] == -1) return false;
				if (result[malted[i]] == 0) {
					result[malted[i]] = 1;
					changed = true;
				}
				select[i] = true;
			}
		}
	}

	REP(i,n)
		printf(" %d", result[i]);
	printf("\n");

	return true;
}


int main(void)
{
	int test;
	int cnt = 0;
 	scanf("%d", &test);

	REP(i, test) {
		printf("Case #%d:", ++cnt);
		if (solve() == false)
			printf(" IMPOSSIBLE\n");
	}

	return 0;
}


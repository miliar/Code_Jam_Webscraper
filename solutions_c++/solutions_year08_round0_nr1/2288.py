#include <cstdio>
#include <vector>
#include <algorithm>
#include <string>
#include <queue>
#include <set>
#include <map>

#define pb push_back
#define mp make_pair
#define REP(i,n) for(int i=0; i<(n); ++i)
#define sz size()

using namespace std;

typedef vector<int> vi;
typedef long long ll;

void solve()
{
	int s,q;
	int dy[1001][101];
	map<string, int> dic;

	scanf("%d\r\n",&s);
	REP(i,s) {
		char buf[1024];
		gets(buf);
		dic[buf] = i;
		dy[0][i] = 0;
	}
	
	scanf("%d\r\n",&q);
	REP(i,q) {
		char buf[1024];
		gets(buf);
		int cur = dic[buf];
		REP(j,s) {
			dy[i+1][j] = 2000;
			if(cur != j) {
				REP(k,s) {
					int next = dy[i][k];
					if(k != j) ++next;
					if(next < dy[i+1][j]) dy[i+1][j] = next;
				}
			}
		}
	}
	int mm = 2000;
	REP(i,s) {
		mm = min(mm,dy[q][i]);
	}
	printf("%d\n",mm);
}

int main()
{
	int t;
	scanf("%d",&t);
	REP(i,t) {
		printf("Case #%d: ",i+1);
		solve();
	}
	return 0;
}

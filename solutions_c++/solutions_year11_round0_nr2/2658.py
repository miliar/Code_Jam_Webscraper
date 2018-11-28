#include <string>
#include <cctype>
#include <vector>
#include <list>
#include <map>
#include <queue>
#include <set>
#include <iostream>
#include <sstream>
#include <fstream>
#include <algorithm>
#include <cmath>
#include <numeric>
#include <cstdlib>
#include <cstdio>
#include <queue>
#include <stack>
#include <memory.h>
#include <assert.h>
using namespace std;
#define SZ(a) (int)(a).size()
#define FOR(i,a,b) for (int i=(a); i<=(b); ++i)
#define REP(i,n) for (int i=0; i<(n); ++i)
#define ALL(c) c.begin(), c.end()
#define TR(container, it) for(typeof(container.begin()) it = container.begin(); it != container.end(); it++)
#define CONTAIN(container, it) (container.find(it)!=container.end())
#define CLR(c,n) memset(c,n,sizeof(c))
#define MCPY(dest,src) memcpy(dest,src,sizeof(src))
template<class T> T checkmax(T &a, T b) {return a=max(a,b);}
template<class T> T checkmin(T &a, T b) {return a=min(a,b);}
typedef vector<int> VI;
typedef vector<string> VS;
typedef pair<int, int> PII;
const double EPS=1e-9;
const double PI=acos(-1);
const int INF=0x3F3F3F3F;

int main(int argc, char *argv[])
{
	freopen("B.in", "r", stdin);
	freopen("B.out", "w", stdout);
	int test_case;
	scanf("%d", &test_case);
	int c, d, n;
	char comb[128][128], oppo[128];
	string s,t;
	for (int test_case_id=1; test_case_id<=test_case; ++test_case_id) {
		CLR(comb,0); CLR(oppo,0);
		for(cin>>c;c;--c) {
			cin>>s;
			comb[s[0]][s[1]]=s[2];
			comb[s[1]][s[0]]=s[2];
		}
		for(cin>>d;d;--d) {
			cin>>s;
			oppo[s[0]]=s[1];
			oppo[s[1]]=s[0];
		}
		cin>>n>>s;
		t="";
		REP(i,n) {
			t+=s[i];
			int m=SZ(t);
			if (m>=2&&comb[t[m-1]][t[m-2]]) t=t.substr(0,m-2)+comb[t[m-1]][t[m-2]];
			else {
				REP(j,m) if (oppo[t[m-1]]==t[j]) {
					t="";
					break;
				}
			}
		}
		fprintf(stderr, "Case %d of %d\n", test_case_id, test_case);
		printf("Case #%d: ", test_case_id);
		printf("[");
		if (t!="") printf("%c",t[0]);
		for (int i=1; i<t.size(); ++i) printf(", %c", t[i]);
		printf("]\n");
	}
}

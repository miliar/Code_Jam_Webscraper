#include <cstdio>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <cctype>
#include <numeric>
#include <queue>
#define FOR(i,s,e) for(int i=(s);i<(int)(e);i++)
#define FOE(i,s,e) for(int i=(s);i<=(int)(e);i++)
#define CLR(s) memset(s,0,sizeof(s))
#define PB push_back
using namespace std;
typedef long long LL;
typedef pair<int,int> pii;
typedef vector<int> vi;
#define x first
#define y second

char comb[200][200];
char pro[200][20];
int c,d,n;
char s[200],t[200];

int main() {
	int T;
	scanf("%d", &T);
	FOE(ttt,1,T) {
		scanf("%d", &c);
		FOR(i,0,c) scanf("%s", comb[i]);
		scanf("%d", &d);
		FOR(i,0,d) scanf("%s", pro[i]);
		scanf("%d%s", &n, s);
		int m = 0;
		FOR(i,0,n) {
			char u=s[i];
			t[m++]=u;
			bool some=0;
			if(m>=2) {
				char v=t[m-2];
				FOR(k,0,c) if(!some) {
					if(comb[k][0]==u && comb[k][1]==v || comb[k][1]==u && comb[k][0]==v) {
						--m;
						t[m-1]=comb[k][2];
						some=1;
					}
				}
			}
			if(!some) {
				bool ss=0;
				FOR(j,0,m-1) {
					char v=t[j];
					FOR(k,0,d) {
						ss |= (pro[k][0]==u && pro[k][1]==v);
						ss |= (pro[k][1]==u && pro[k][0]==v);
					}
				}
				if(ss) m=0;
			}
		}

		printf("Case #%d: [", ttt);
		FOR(j,0,m) {
			if(j) printf(", ");
			printf("%c", t[j]);
		}
		puts("]");
	}
	return 0;
}

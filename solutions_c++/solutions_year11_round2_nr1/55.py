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

int T,ca=0;
const int N=300;
char s[N][N];
int p[N];
int w[N];
double owp[N];

int main() {
	scanf("%d", &T);
	while (T--) {
		printf("Case #%d:\n", ++ca);
		CLR(w);
		CLR(p);
		int n;
		scanf("%d", &n);
		FOR(i,0,n) scanf("%s",s[i]);
		FOR(i,0,n) {
			FOR(j,0,n) if(s[i][j]!='.'){
				p[i]++;
				w[i]+=(s[i][j]=='1');
			}
		}
		CLR(owp);
		FOR(i,0,n) {
			FOR(j,0,n) if(s[i][j]!='.'){
				double add=(1.0*(w[j]-(s[j][i]=='1'))/(p[j]-1));
				owp[i]+=add;
			}
			owp[i] /= p[i];
		}
		FOR(i,0,n) {
			double oowp=0;
			FOR(j,0,n) if(s[i][j]!='.') {
				oowp+=owp[j];
			}
			double sum=0.25*w[i]/p[i] + 0.5*owp[i] + 0.25*oowp/p[i];
			printf("%.15f\n", sum);
		}
	}
	return 0;
}

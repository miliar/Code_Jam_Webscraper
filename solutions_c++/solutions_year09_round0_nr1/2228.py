#define DBG
// Grzegorz Guspiel 1e
// V-LO Krakow

#include <iostream>
#include <cassert>
#include <algorithm>
#include <vector>

using namespace std;

#ifdef DBG
#define REPORT(s) cout<<s<<endl
#else
#define REPORT(s)
#define NDEBUG
#endif
#define REP(i,n) for(int (i)=0; (i)<(n); (i)++)

const int maxn=5010;
const int maxl=17;
const int maxe='z'-'a'+1;
char words[maxn][maxl];

int l,n,z;

int main()
{
	scanf("%d %d %d\n", &l, &n, &z);
	REP(i,n) scanf("%s\n", words[i]);
	REP(zz,z)
	{
		char buf[maxl*100];
		scanf("%s\n", buf);
		int p=0;
		int t[maxl][maxe];
		REP(i,l) {
			REP(j,maxe) t[i][j]=0;
			if(buf[p]!='(') {
				t[i][buf[p]-'a']=1;
				p++;
				continue;
			}
			p++;
			while(buf[p]!=')') {
				t[i][buf[p]-'a']=1;
				p++;
			}
			p++;
		}
		int cnt=0;
		REP(i,n) {
			bool ok=1;
			REP(j,l) if(t[j][words[i][j]-'a']==0) { ok=0; break; }
			if(ok) cnt++;
		}
		printf("Case #%d: %d\n", zz+1, cnt);
	}
	return 0;
}


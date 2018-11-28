#define all(v) v.begin(), v.end()
#define pb push_back
#define mp make_pair
#define fs first
#define sc second
#define sz(v) (int(v.size()))
#define pch putchar
#define gch getchar()
#define FORD(i,a,b) for (int i=(a); i<=(b); i++)
#define FORP(i,a,b) for (int i=(a); i>=(b); i--)
#define REP(i,n) for (int i=0; i<(n); i++)
#define clean(v) memset(v,0,sizeof(v))

#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>

using namespace std;

template<typename T> T sqr(const T& c) {return c*c;} 

typedef long long ll;
typedef double lf;

pair<int,ll> to[1000];//who will be first, how much money will be earned
ll x[1000];

int main() {
	int tests, r; ll k; int n;
	scanf("%d",&tests);
	FORD(curTest,1,tests) {
		scanf("%d%I64d%d",&r,&k,&n); ll ans = 0;
		REP(i,n) scanf("%I64d",&x[i]), to[i] = mp(-1,-1);
		int cur = 0;
		REP(i,r) {
			
			//cerr << cur << ' ' << ans << '\n';
			
			if (to[cur].fs!=-1) {
				
				int uk = 0; ans = 0;
				ll pre = 0;

				while (uk!=cur)
					pre += to[uk].sc, r--, uk = to[uk].fs;
				
				int per_length = 1; ll period = to[cur].sc;
				uk = to[cur].fs;
				while (uk!=cur)
					period += to[uk].sc, uk = to[uk].fs, per_length++;
					                            
				int last = r % per_length;
				ans = pre+period*(r/per_length);
				
				REP(i,last) {
					ans += to[uk].sc, uk = to[uk].fs;
				}
				
				break;
			}

			int cc = cur; ll sum = 0;
			while (sum+x[cc]<=k && (sum==0 || cc!=cur)) {
				sum += x[cc++];
				cc %= n;
			}
			ans += sum;
			to[cur] = mp(cc,sum); cur = cc;

		}
		printf("Case #%d: %I64d\n",curTest,ans);

	}
}

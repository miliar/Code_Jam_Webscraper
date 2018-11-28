
#include<cassert>
#include<iostream>
#include<cstdio>
#include<vector>
#include<algorithm>
#include<cmath>
#include<map>
#include<set> 
#include<queue>
#include<cstring>
#include<stack>
#include<sstream>
#include<complex>
#define FORE(it,c) for(__typeof((c).begin()) it=(c).begin();it!=(c).end();++it) 
#define debug(x) cerr << #x << " = " << x << "\n";
#define debugv(x) { cerr << #x << " = "; FORE(it,(x)) cerr<< *it <<","; cerr<<"\n"; }
#define fup(i,a,b) for(int i=(a);i<=(b);i++)
#define fdo(i,a,b) for(int i=(a);i>=(b);i--)
#define REP(i,n) for(int i=0;i<(n);++i)
#define ALL(x) (x).begin(),(x).end()
#define CLR(x) memset((x),0,sizeof (x))
#define abso(a) ((a)<0?(-(a)):(a))
#define maxi(a,b) ((a)>(b)?(a):(b))
#define mini(a,b) ((a)<(b)?(a):(b))
#define MP make_pair
#define PB push_back
#define FI first
#define SE second
#define siz(a) ((int)a.size())
#define inf 1000000000
#define SQR(a) ((a)*(a))

using namespace std;
typedef long long lli;
typedef double ld;
#define maxn 40
int t[maxn];
int n;

int main(){
	int cas;
	cin >> cas;
	fup(j, 1, cas) {
		cin >> n;
		fup(i, 1, n) {
			string x; cin >> x;
			int maxi = -1;
			fup(j, 0, siz(x) - 1) if (x[j] == '1') maxi = j;
			t[i] = maxi + 1;
		}
		int sum = 0;
		fup(i, 1, n) {
			int gdzie = -1;
			fup(j, i, n) {
				if (t[j] <= i) {
					gdzie = j;
					break;
				}
			}	
			int x = t[gdzie];
			fdo(j, gdzie, i + 1) {
				t[j] = t[j - 1];
				sum++;
			}
			t[i] = x;
		}
		printf("Case #%d: %d\n", j, sum);

	}

	return 0;	
}



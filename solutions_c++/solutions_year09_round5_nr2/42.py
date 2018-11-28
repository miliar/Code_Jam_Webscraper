#include <iostream>
#include <cstring>
#include <string>
using namespace std;

const int MOD = 10009;
const int MAXN = 100;
const int MAXK = 10;
const int MAXPL = 4;
const int MAXTN = 5;

int n, K, tn;
int a[MAXK+1][MAXN+1][1 << MAXPL];
int ans[MAXK+1];
int binom[MAXK+1][MAXK+1];
int cnt[26];
string dict[MAXN], term[MAXTN];


void makeBinom(){
	memset(binom, 0, sizeof(binom));
	for(int i=0; i<=MAXK; i++)
		binom[i][0] = 1;
	for(int i=1; i<=MAXK; i++)
		for(int j=1; j<=MAXK; j++){
			binom[i][j] = (binom[i-1][j-1]+binom[i-1][j])%MOD;
//			cerr << "binom[" << i << "][" << j << "]=" << binom[i][j] << endl;
		}
}

void read(){
	string poly;
	cin >> poly >> K;
	cin >> n;
	for(int i=0; i<n; i++)
		cin >> dict[i];
	int lastpos = -1;
	tn = 0;
	for(int i=0; i<poly.size()+1; i++)
		if (i >= poly.size() || poly[i] == '+'){
			term[tn++] = poly.substr(lastpos+1, i-lastpos-1);
			lastpos = i;
		}
}

int calcP(const string& P, int mark, string w, int b){
	for(int i=0; i<w.size(); i++)
		cnt[w[i]-'a']++;

	int res = 1;
	for(int i=0; i<P.size(); i++)
		if (mark&(1 << i))
			res = (res*cnt[P[i]-'a']*b)%MOD;

	for(int i=0; i<w.size(); i++)
		cnt[w[i]-'a']--;
//	cerr << "calcP(" << P << "_" << mark << "(" << w << "^" << b << ")=" << res << endl;
	return res;
}

void calc(string P){
	memset(a, 0, sizeof(a));
	for(int k=0; k<=K; k++)
		for(int p=0; p<(1 << P.size()); p++)
			a[k][1][p] = calcP(P, p, dict[0], k);
	for(int m=1; m<n; m++)
		for(int k=0; k<=K; k++)
			for(int p=0; p<(1 << P.size()); p++){
				for(int b=0; b<=k; b++){
					int delta = 0;
					for(int c=0; c<(1 << P.size()); c++)
						if ((c&p) == c)
							delta = (delta+calcP(P, c, dict[m], b)*a[k-b][m][p-c])%MOD;
					a[k][m+1][p] = (a[k][m+1][p]+delta*binom[k][b])%MOD;
				}
			}
	for(int k=0; k<=K; k++)
		ans[k] = (ans[k]+a[k][n][(1 << P.size())-1])%MOD;
}

int main(){
	makeBinom();
	memset(cnt, 0, sizeof(cnt));
	int T;
	cin >> T;
	for(int it=0; it<T; it++){
		read();
		memset(ans, 0, sizeof(ans));
		for(int i=0; i<tn; i++)
			calc(term[i]);
		printf("Case #%d:", it+1);
		for(int i=0; i<K; i++)
			cout << " " << ans[i+1];
		cout << endl;
	}
}


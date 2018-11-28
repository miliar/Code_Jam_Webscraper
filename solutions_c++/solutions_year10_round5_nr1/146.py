#include <cstdio>
#include <vector>
#include <algorithm>

using namespace std;

typedef long long ll;

ll fastPow( ll base, ll exp, ll p){
	ll res = 1;
	ll acc = base;
	while(exp){
		if(exp&1){
			res = (res*acc)%p;
		}
		acc = (acc*acc)%p;
		exp >>= 1;
	}
	return res;
}

ll inv ( ll co, ll p){
	return fastPow( co, p-2, p);
}

bool isprime(int co){
	for(int t = 2; t*t <= co; t++){
		if(co%t==0) return false;
	}
	return true;
}

int ver(const vector<int> &seq, ll a, ll b, int p){
	int cur = seq[0];
	for(int i = 1; i < (int)seq.size(); i++){
		cur = (((ll)cur)*a+b)%p;
		if( cur != seq[i] ) return -1;
	}
	return ((ll)cur*a+b)%p;
}

int main(){
	int lz;
	scanf("%d", &lz);
	for(int cnt = 1; cnt <= lz; cnt++){
		int d, k;
		scanf("%d%d", &d, &k);
		int limd = 1;
		for(int i = 0; i < d; i++) limd *= 10;
		vector<int> seq(k);
		//printf("wektor si: %d\n", (int)seq.size());
		for(int i = 0; i < k; i++) scanf("%d", &seq[i]);
		//printf("ok\n");
		int mm = 0;
		for(int i = 0; i < k; i++) mm = max(mm, seq[i]);
		int res = -1;
		if( k > 1 && seq[0] == seq[1]){
			res = seq[1];
		}
		else if( k > 2){
			for(int p = max(2,mm+1); p < limd; p++){
				if(!isprime(p)) continue;
				ll small = seq[1]-seq[0];
				ll big = seq[2] - seq[1];
				if(small < 0) small += p;
				if(big < 0) big += p;
				ll a = big*inv(small, p);
				ll b = seq[1] - seq[0]*a;
				if(b < 0){
					ll todo = -b;
					ll sk = (todo+p-1)/p;
					b += sk*p;
				}
				int prop = ver(seq,a,b,p);
				if(prop!=-1){
					if(res == -1){
						res = prop;
					}
					else if( res >= 0 && res != prop){
						res = -2;
					}
				}
				if(res == -2) break;
			}
		}
		if( res >= 0) printf("Case #%d: %d\n",cnt, res);
		else printf("Case #%d: I don't know.\n",cnt);
	}
	return 0;
}

#include <cstdio>
#include <algorithm>
#include <vector>
#include <cstring>

using namespace std;

int n, k;
vector<int> p;
int p10[10];
int l[20];

bool ok(int x){
	for(int i=3; i*i<=x; i+=2)
		if(x%i == 0) return false;
	return true;
}

typedef long long ll;
int P;
int pwr(int a, int x){
	int res = 1;
	int m = a;
	while(x > 0){
		if(x&1) res = ((ll)res*m) % P;
		x >>= 1;
		m = ((ll)m*m) % P;
	}
	return res;
}
int inv(int x){ return pwr(x,P-2); }

bool all(){
	for(int i=1; i<n; ++i)
		if(l[i] == l[i-1]) return true;
	return false;
}

bool pass(int a, int b){
	for(int i=1; i<n; ++i){
		int c = ((ll)l[i-1]*a + b)%P;
		if(c != l[i]) return false;
	}
	return true;
}

int main()
{
	p10[0] = 1;
	for(int i=1; i<=6; ++i) p10[i] = p10[i-1]*10;
	p.push_back(2);
	for(int i=3; i<1000000; i+=2)
		if(ok(i)) p.push_back(i);
	int cases;
	scanf("%d", &cases);
	for(int iii=1; iii<=cases; ++iii){
		scanf("%d%d", &k, &n);
		int mx = -1;
		for(int i=0; i<n; ++i) scanf("%d", &l[i]),
		mx = max(mx, l[i]);
		printf("Case #%d: ", iii);
		vector<int> R; R.clear();
		if(n == 1){ printf("I don't know.\n"); continue; }
		else if(all()){ printf("%d\n", l[n-1]); continue; }
		else if(n == 2){ printf("I don't know.\n"); continue; }
		for(int i=0; i<p.size(); ++i){
			P = p[i];
			if(P >= p10[k]) break;
			if(P <= mx) continue;
			int A = ((((ll)(l[1]-l[2])) * inv((P + l[0]-l[1]) % P))%P+P)%P;
			int B = (((ll)l[1] - (ll)A*l[0])%P + P)%P;
			if(pass(A,B)){
				int C = ((ll)l[n-1]*A + B)%P;
				if(R.empty() || R.back() != C)
					R.push_back(C);
			}
		}
		if((int)R.size() != 1) printf("I don't know.\n");
		else printf("%d\n", R[0]);
	}
	return 0;
}

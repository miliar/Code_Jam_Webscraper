#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <vector>
#include <set>

using namespace std;

typedef long long LL;

LL module(LL n, LL m,const LL K){
	LL ret = 0;
	n %= K;
	m %= K;
	for (int i = 62; i >= 0; i--){
		ret <<= 1;
		if (ret > K) ret -= K;
		if (n & (1ll << i)){
			ret += m;
			if (ret > K) ret -= K;
        }
	}
	return ret;
}

LL power(LL N, LL r, LL M){
	LL ret = 1;
	for (int i = 62; i >= 0;i--){
		ret = module(ret, ret, M);
		if (r & (1ll << i))
			ret = module(ret ,N , M);
	}
	return ret;
}


LL rho(LL N){
	while (true){
		for (LL x = rand(),y = x,i = 2,d;;i++){
			x = (module( x , x , N) + N - 1 ) % N;
			d = __gcd(N, abs(x - y));
			if(d != 1 && d != N) return d;
			if(d == N) break;
			if(!(i & (i - 1))) y = x;
		}
	}	
}

int Rabin_Miller(int B, LL N){
	LL t = N - 1, x = 1;
	while (t % 2 == 0) t /= 2;
	x = power(B, t, N);
	while (t != N - 1){
		LL next = module(x, x, N);
        if (next == 1 && x != 1 && x != N - 1) return 0;
        x  =  next;
		t <<= 1;
	}
	return x == 1;
		
}

int PrimeTest(LL N){
	int a[] = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 41, 61};
	for (int i = 0; i < 12; i++)
		if (a[i] >= N) return 1;
			else if (Rabin_Miller(a[i] , N) == 0) return 0;
	return 1;
}

int isPrime(LL x){
	for (LL i = 2;i * i <= x; i++)
		if ( x % i == 0)
			return 0;
	return 1;
}

vector<LL> factor(LL x){
	vector<LL> ret;
	while (x % 2 == 0){
		x /= 2;
		ret.push_back(2);
	}
	if (x == 1) return ret;
	ret.push_back(x);
	for (int i = 0;i < ret.size();i++)
		if (!PrimeTest(ret[i])){
			LL x = rho(ret[i]);
			ret[i] /= x;
			ret.push_back(x);
			--i;
		}
	return ret;
}

LL w[1<<20];
int main(){    
    
    freopen("C.in","r",stdin);
    freopen("C.out","w",stdout);
    int T,N;
    LL L,H;
    
    scanf("%d",&T);
    for (int Test = 1;Test <= T; Test++){
        cin >> N >> L >> H;
        for (int i = 1;i <= N;i++)
            cin >> w[i];
        sort(w+1,w+1+N);
        set<LL> v;
        v.clear();
        vector<LL> ret = factor(w[N]);       
        for (int i = 0;i < (1<<ret.size()); i++) {
            LL it = 1;
            for (int k = 0;k < ret.size(); k++)
                if ( (1 << k) & i) it *= ret[k];
            v.insert(it);
        }
        LL ans = H + 1;
        while (!v.empty()){
            LL x = *v.begin();
            v.erase(v.begin());
            if (x > H || x < L) continue;
            bool flag = 1;
            for (int i = 1; i<= N;i++)
                if (x % w[i] && w[i] % x) {
                    flag = 0;
                    break;
                }
            if (flag) {
                ans = x;
                break;
            }
        }
        if (ans < H) {
            printf("Case #%d: ",Test);
            cout << ans <<endl;
        }
        else {
            LL ans = 1;
            bool flag = 1;
            for (int i = 1;i <= N; i++){
                LL tmp =  __gcd(ans,w[i]);
                ans /= tmp;
                if (ans > H / w[i]){
                    flag = 0;
                    break;
                }
                ans *= w[i];
            }
            if (flag) {
                if (ans <= L)
                    ans *= (L - 1) / ans + 1;
                printf("Case #%d: ",Test);
                cout << ans <<endl;
            }
            else printf("Case #%d: NO\n",Test);
                
        }
    }    
    return 0;
}

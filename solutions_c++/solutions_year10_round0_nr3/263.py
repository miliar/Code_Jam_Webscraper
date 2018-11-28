#include<iostream>
#include<cstring>

using namespace std;

typedef struct {
	long long a, b, c;
}triple;

long long inline findans(long long r, long long k, long long n, long long g[]){
	triple *mem = new triple[n];
	long long ans = 0, from = 0;

	for(long long i = 0; i < n; ++i){
		long long j, m = 0, rd = 0, tmp = 0, p = 0;
		for(j = i; ; ++j){
			if(tmp + g[j] > k || p >= n){
				m   += tmp;
				rd  += 1; 
				tmp  = g[j];
				p    = 1;
				if(j >= n){ 
					mem[i].c = j - n;
					break;
				}

				continue;
			}

			p += 1;
			tmp += g[j];
		}

		mem[i].a = m;
		mem[i].b = rd;
	}

	//for(long long i = 0; i < n; ++i)
	//	cout << mem[i].a << ' ' << mem[i].b << ' ' << mem[i].c << endl;

	while(r > 0){
		if(r >= mem[from].b){
			ans += mem[from].a;
			r   -= mem[from].b;
			from = mem[from].c; 
			continue;
		}
	
		long long j, m = 0, rd = 0, tmp = 0, p = 0;
		for(j = from; ; ++j){
			if(tmp + g[j] > k || p >= n){
				ans += tmp;
				r   -= 1;
				tmp  = g[j];
				p    = 1;
				if(j >= n || r == 0) break;

				continue;
			}
			
			p   += 1;
			tmp += g[j];
		}
		

	}
	
	delete [] mem;

	return ans;
}

int main(){
	long long cs;

	cin >> cs;
	for(long long csn = 1; csn <= cs; ++csn){
		long long  ans;
		long long  r, k, n;
		long long* g;

		cin >> r >> k >> n;
		g = new long long[2*n];
		for(long long i = 0; i < n; ++i) cin >> g[i];
		memcpy(g + n, g, 4*n);

		ans = findans(r, k, n, g);

		delete [] g;

		cout << "Case #" << csn << ": " << ans << endl;
	}

	return 0;
}

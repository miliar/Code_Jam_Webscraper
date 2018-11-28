#include <iostream>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <algorithm>
#include <string>
#include <sstream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cassert>
#include <ctime>
#include <cctype>

using namespace std;
typedef long long int64;
const int inf = 0x3f3f3f3f;
typedef double real;
const real eps = 1e-6;
typedef pair<int,int> pip;
#define Eo(x) { cerr << #x << " = " << (x) << endl; }

const int maxn = (1 << 20);
char isp[maxn];
vector<int> primes;
int a[1024];

int main(){
	memset(isp,1,sizeof(isp));
	isp[0] = isp[1] = 0;
	for (int i =2; i * i < maxn; i++) if (isp[i]){
		for (int j = i*i; j < maxn; j += i) isp[j] = 0;
	}
	for (int i = 0; i < maxn; i++) if (isp[i]) primes.push_back(i);
	int T; cin >> T;
	for (int  _ = 0; _ < T; _++){
		printf("Case #%d: ",_+1);
		int d,k; cin >> d >> k;
		int lim = 1;
		for (int i = 0; i < d; i++) lim *= 10;
		int mx = 0;
		for (int i = 0; i < k; i++) {
			cin >> a[i];
			mx = max(mx,a[i]);
		}
		if (k == 1){
			puts("I don't know.");
			continue;
		}
		bool did = false;
		for (int i = 0; i < k-1; i++) if (a[i] == a[k-1]){
			printf("%d\n",a[i+1]);
			did = true;
			break;
		}
		if (did) continue;
		int cnt = 0;
		int result = -1;
		set<int> canbe;
		for (int i = 0; canbe.size() < 2 && i < primes.size(); i++){
			int p = primes[i];
			if (p > lim) break;
			if (p <= mx) continue;
			for (int A = 0; A < p; A++){
				int SA = (a[0]*A)%p;
				int B = (a[1]-SA+p)%p;
				bool ok = true;
				for (int j = 0; j < k-1; j++){
					int expect = (a[j]*A+B)%p;
					if (expect != a[j+1]){
						ok = false;
						break;
					}
				}
				if (ok){
					cnt++;
					result = (a[k-1]*A+B)%p;
					canbe.insert(result);
				}
			}
		}
		if (canbe.size() != 1){
			puts("I don't know.");
		} else {
			printf("%d\n",*canbe.begin());
		}
	}
	return 0;
}


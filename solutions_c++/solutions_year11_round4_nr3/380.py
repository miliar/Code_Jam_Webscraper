#include <cstdio>
#include <cstring>
#include <algorithm>
#include <cmath>
#include <cctype>
#include <iostream>
#include <vector>

using namespace std;

typedef long long ll;
typedef unsigned long long ull;
typedef pair<int,int> PII;

#define maxn (1200000)
#define PB push_back
#define MP make_pair

const int bound=1100000;
int prime[maxn];
bool flag[maxn];
int n;

void ready(){
	for (int i=2;i<=bound;i++) if (!flag[i]) {
		prime[++n]=i;
		for (int k=i;k<=bound;k+=i) flag[k]=true;
	}
}

int main(){
	ready();
	int T; scanf("%d",&T);

	for (int tt=1;tt<=T;tt++) {
		printf("Case #%d: ",tt);
		ll x; cin >> x ;

		ll a=0ll,b=0ll;

		for (int i=1;i<=n;i++) {
			ll now=prime[i];
			if (now<=x) a++;
			else break;
		}
		if (x==1ll) a=1ll;

		b=1ll;
		for (int i=1;i<=n;i++) {
			ll now=prime[i],k=now;

			while (k<=x) {
				b++; k*=now;
			}
		}

		cout << b-a << endl ;
	}

	return 0;
}

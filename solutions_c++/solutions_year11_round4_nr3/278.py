#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <vector>
#include <algorithm>
#include <set>
#include <queue>
#include <map>
#include <string>
#include <ctime>
#include <climits>
#include <cassert>
//#pragma comment(linker, "/STACK:640000000")
#ifdef _Win32
#  define I64 "%I64d"
#else
#  define I64 "%lld"
#endif
#define fs first
#define sc second
#define mp make_pair
#define pb push_back
#define next ksdjgsd
#define prev lsfnasd
using namespace std;
typedef long long ll;
typedef long double ld;
typedef pair<int, int> pi;
const ld E=1e-8;
const int inf=(int)1e9;

int p[1000010];

int main(){
	freopen("a.in", "r", stdin);
	freopen("a.out", "w", stdout);
	int tn;
	int maxn=1000005;
	for(int i=2;i<maxn;i++) if(p[i]==0) for(int j=2;i*j<maxn;j++) p[i*j]=1;

	scanf("%d", &tn);
	for(int tt=0;tt<tn;tt++){
		ll n;
		scanf("%I64d", &n);
		ll m=min((ll)sqrt(n*1.0)+10, n);
		int res=1;
		for(int i=2;i<m;i++){
			if(p[i]==0){
				ll j=i;
				while(j*i<=n){
					j*=i;
					res++;
				}
			}
		}
		printf("Case #%d: ", tt+1);
		if(n==1) printf("0\n");
		else printf("%d\n", res);
	}
	return 0;
}

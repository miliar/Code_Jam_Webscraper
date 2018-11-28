#include <cstdio>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
using namespace std;
typedef long long LL;


int ntc,n,k,b,t,res;
int x[107],v[107],s[107]; // 2 - dodaj 1 - usun 0 - nie rob
bool can(int a) {
	if(((LL)x[a]+(LL)t*(LL)v[a])>=(LL)b) return 1; else return 0;
}

int main() {
	scanf("%d", &ntc);
	for(int i=1; i<=ntc; ++i) {
		printf("Case #%d: ", i);
		scanf("%d%d%d%d", &n,&k,&b,&t);
		for(int i=0; i<n; ++i) scanf("%d", &x[i]);
		for(int i=0; i<n; ++i) scanf("%d", &v[i]);
		//for(int i=0; i<n; ++i) printf("%d ",can(i)); printf("\n");
		for(int i=n-1; i>=0 && k; --i) {
			if(can(i)) { s[i]=2; --k; }
			else s[i]=1;
		}
		if(k) { printf("IMPOSSIBLE\n"); }
		else {
			int act=0;
			for(int i=0; i<n; ++i) {
				if(s[i]==2) ++act;
				else if(s[i]==1) res+=act;
			}
			printf("%d\n", res);	
		}
		for(int i=0; i<n; ++i) s[i]=0;
		res=0;

	}
}











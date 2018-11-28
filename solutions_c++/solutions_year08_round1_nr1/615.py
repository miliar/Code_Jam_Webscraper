#include <stdio.h>
#include <assert.h>
#include <string.h>
#include <math.h>
#include <string>
#include <set>
#include <map>
#include <vector>
#include <algorithm>

using namespace std;

#define FOR(i,a,b) for (int i=(a),_b=(b); i<=_b; i++)
#define FORD(i,a,b) for (int i=(a),_b=(b); i>=_b; i--)
#define REP(i,n) for (int i=0,_n=(n); i<_n; i++)

long long res;
int nTC,n;

void minplus(vector<long long> &a, vector<long long> &b){
	while (a.size() > 0 && a.front() < 0){
		if (b.back() > 0){
			res += a.front() * b.back();
			a.erase(a.begin());
			b.pop_back();
		} else if (b.back() <= 0) break;
	}
}

void zeroit(vector<long long> &a, vector<long long> &b){
	for (int i=0; i<a.size(); i++){
		if (a[i]==0){
			a[i] = a.back();
			a.pop_back();

			if (labs(b.front()) > labs(b.back())){
				b.erase(b.begin());
			} else {
				b.pop_back();
			}
		}
	}
	sort(a.begin(),a.end());
}

int main(){
	scanf("%d",&nTC);
	FOR(TC,1,nTC){
		scanf("%d",&n);
		vector<long long> a(n),b(n);
		REP(i,n) scanf("%lld",&a[i]);
		REP(i,n) scanf("%lld",&b[i]);
		sort(a.begin(),a.end());
		sort(b.begin(),b.end());

		res = 0;
		
		minplus(a,b);
		minplus(b,a);

		zeroit(a,b);
		zeroit(b,a);

		REP(i,a.size()) assert(a[i]*b[i] >= 0);
		reverse(a.begin(),a.end());
		REP(i,a.size()) res += a[i]*b[i];

		printf("Case #%d: %lld\n",TC,res);
	}
}

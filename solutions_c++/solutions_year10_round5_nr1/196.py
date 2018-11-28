//be name oo
#include <cstdio>
#include <iostream>
#include <algorithm>
#include <set>
#include <string>
#include <map>
#include <utility>
#include <cstring>
#include <sstream>
#include <complex>
#include <vector>

#define FOR(i, n) for(int i = 0; i < (n); i++)
#define SZ(x) ((int)x.size())
#define PB push_back
#define X first
#define Y second

using namespace std;
typedef pair<int, int> joft;
typedef complex<double> point;

const int MAX_K = 10 + 2;
const int MAX_P = 1000 * 1000 + 10;

vector<int> ans;
vector<int> prm;
bool isp[MAX_P];

void init(){
	memset(isp, 1, sizeof isp);
	for(int i = 2; i < MAX_P; i++)
		if(isp[i]){
			prm.PB(i);
			for(int j = i + i; j < MAX_P; j += i)
				isp[j] = 0;
		}
}

int k;
int num[MAX_K];

bool check(int a, int b, int p){
	int cur = num[0] % p;
	FOR(i, k){
		if(num[i] != cur)
			return false;
		cur = a * cur + b;
		cur %= p;
	}
	return true;
}

joft solve(int a, int b, int d){
	if(!b)
		return joft(d / a, 0);
	joft cur = solve(b, a % b, d);
	return joft(cur.Y, cur.X - cur.Y * (a / b));
}

int main(){
	init();
	int t;
	scanf("%d", &t);
	for(int test = 1; test <= t; test++){
		int d;
		scanf("%d %d", &d, &k);
		FOR(i, k)
			scanf("%d", &num[i]);
		if(k == 1){
			printf("Case #%d: I don't know.\n", test);
			continue;
		}
		if(k == 2){
			if(num[0] == num[1])
				printf("Case #%d: %d\n", test, num[0]);
			else	printf("Case #%d: I don't know.\n", test);
			continue;
		}
		
		ans.clear();
		int pow = 1;
		FOR(i, d)	pow *= 10;
		
		for(int i = 0; i < SZ(prm) && prm[i] <= pow; i++){
			int p = prm[i];
			
			int d1 = num[1] - num[0];	d1 %= p;	d1 += p;
			int d2 = num[2] - num[1];	d2 %= p;	d2 += p;
			int a = ((solve(d1, p, d2).X % p) + p) % p;
			int b = (((num[1] - a * num[0]) % p) + p) % p;
			
			if(check(a, b, p)){
				int last = num[0];
				FOR(i, k)
					last = (a * last + b) % p;
				ans.PB(last);
				//cerr<<a<<" "<<b<<" "<<p<<" "<<last<<endl;
			}
		}
		
		sort(ans.begin(), ans.end());
		int sz = unique(ans.begin(), ans.end()) - ans.begin();
		if(sz == 1){
			printf("Case #%d: %d\n", test, ans[0]);
		}else	printf("Case #%d: I don't know.\n", test);
	}
	return 0;
}

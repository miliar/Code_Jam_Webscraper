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
#define F first
#define S second

using namespace std;
typedef pair<int, int> joft;
typedef complex<double> point;

const int MAX_N = 1000 + 10;

int n, su;
int num[MAX_N];
int unq[MAX_N];
vector<int> baze;

vector<int> cur;
int sum[MAX_N];

bool can(int m){
	memset(sum, 0, sizeof sum);
	cur = baze;
	FOR(i, SZ(cur)){
		int val = min(cur[i], sum[i]);
		sum[i + 1] += val;
		cur[i] -= val;
		val = cur[i];
		if(val){
			for(int j = i; j < i + m; j++)
				if(j >= SZ(cur) || cur[j] < val)
					return false;
				else	cur[j] -= val;
			sum[i + m] += val;
		}
	}
	return true;
}

int solve(){
	int s = 0, e = SZ(baze) + 1;
	while(s + 1 < e){
		int m = (s + e) / 2;
		if(can(m))
			s = m;
		else	e = m;
	}
	return s;
	/*FOR(i, SZ(baze))
		cerr<< baze[i] << " ";
	cerr << endl;
	return 0;*/
}

int main(){
	int testN;
	cin >> testN;
	FOR(testI, testN){
		cin >> n;
		FOR(i, n){
			cin >> num[i];
			unq[i] = num[i];
		}
		sort(num, num + n);
		sort(unq, unq + n);
		su = unique(unq, unq + n) - unq;
		
		int first = 0;
		int ans = n;
		while(first < su){
			baze.clear();
			int last = first;
			while(last < su && (last - first) == (unq[last] - unq[first])){
				baze.push_back( count(num, num + n, unq[last]) );
				last++;
			}
			first = last;
			ans = min(ans, solve());
		}
		
		printf("Case #%d: %d\n", testI + 1, ans);
	}
	return 0;
}

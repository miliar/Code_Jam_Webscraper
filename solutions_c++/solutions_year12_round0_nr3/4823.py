#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <climits>
#include <cfloat>
#include <map>
#include <utility>
#include <set>
#include <iostream>
#include <memory>
#include <string>
#include <vector>
#include <algorithm>
#include <functional>
#include <sstream>
#include <complex>
#include <stack>
#include <queue>
#include <fstream>

typedef long long ll;

using namespace std;

#define INF (1<<29)

int digits(int num){
	int cnt = 0;
	while ( num  > 0 ){
		num /= 10;
		cnt++;
	}
	return cnt;
}

vector<int> generate(int num){
	vector<int> d;
	int temp = num;
	while ( temp > 0 ){
		d.push_back( temp % 10 );
		temp /= 10;
	}
	reverse(d.begin(), d.end());
	int n = d.size();
	vector<int> res;
	for ( int i = 1; i < n; i++ ){
		int p = 0;
		for ( int j = 0; j < n; j++ ){
			p = p*10 + d[(i+j) % n];
		}
		if ( p != num && digits(p) == n ){
			res.push_back(p);
		}
	}
	return res;
}

int calc(int A, int B){
	set< pair<int, int> > S;
	for ( int n = A; n <= B; n++ ){
		vector<int> ms = generate(n);
		for ( int i = 0; i < ms.size(); i++ ) if ( A <= ms[i] && ms[i] <= B ) {
			S.insert( make_pair(n, ms[i]) );
		}
	}
	return S.size() / 2;
}

int main(){
	freopen( "C-small-attempt0.in", "r", stdin );
	freopen( "C-small-attempt0.out", "w", stdout );
	
	int T; cin >> T;
	int A, B; 
	
	for ( int i = 0; i < T; i++ ){
		cin >> A >> B;
		printf("Case #%d: %d\n", i+1, calc(A, B));
	}
}
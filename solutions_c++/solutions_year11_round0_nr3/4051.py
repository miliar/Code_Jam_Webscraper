#pragma comment(linker,"/STACK:32000000")
#include <stdio.h>
#include <iostream>
#include <sstream>
#include <queue>
#include <algorithm>
#include <vector>
#include <math.h>
#include <set>
#include <map>
#include <string>

using namespace std;

#define infile ".in"
#define outfile ".out"
#define FOR(i, n) for (int i = 0; i <(n); i++)
#define DFOR(i, n) for (int i = (n) - 1; i >= 0; i--)
#define PB push_back
#define MP make_pair
#define ALL(x) x.begin(), x.end()
#define LL long long
#define SQR(x) ((x) * (x))
#define ABS(x) ((x) < 0 ? -(x) : (x))
#define MAX(a, b) ((a) > (b) ? (a) : (b))
#define MIN(a, b) ((a) < (b) ? (a) : (b))
#define CLR(a, b) memset((a), (b), sizeof(a))
#define SS stringstream
#define PII pair<int, int>
#define VPII vector < PII >

void init(){
	freopen(infile, "r", stdin);
	freopen(outfile, "w", stdout);
}


#define maxn 1100

int n;
int a[maxn];
int ans;

int bit(int x, int i){
	return ((x & (1<<i))==0? 0 : 1);
}

void solvecase(){
	int s = 0;
	ans = 0;
	for(int i=0; i<n; i++)
		s ^= a[i];
	if(s!=0){
		cout << "NO" << endl;
		return;
	}
	for(int x=1; x<(1<<n)-1; x++){
		int s1 = 0, s2 = 0;
		for(int j=0; j<n; j++){
			if(bit(x, j)==0) s1 ^= a[j];
			else s2 ^= a[j];
		}
		if(s1 != s2) continue;
		s1 = s2 = 0;
		for(int j=0; j<n; j++){
			if(bit(x, j)==0) s1 += a[j];
			else s2 += a[j];
		}
		if(s1>ans) ans = s1;
		if(s2>ans) ans = s2;	
	}
	cout << ans << endl;
}

void solve(){
	int t;
	cin >> t;
	for(int i=0; i<t; i++){
		cin >> n;
		for(int j=0; j<n; j++)
			cin >> a[j];
		cout << "Case #" << i+1 << ": ";
		solvecase();			
	}
}

int main(){
	init();
	solve();
	return 0;
}
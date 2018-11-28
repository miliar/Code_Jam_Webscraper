// Author: Swarnaprakash
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <queue>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cctype>
#include <cassert>

using namespace std;

const int M = 105;
const int INF = 0x3f3f3f3f;
const bool debug=true;

#define SET(x,v)	memset(x,v,sizeof(x))
#define ALL(x) 		(x).begin() , (x).end()
#define SZ(x)		((int)((x).size()))
#define DB(x) 		if(debug) cout << #x << " : " << x <<endl;

typedef long long LL;
typedef vector<int> VI;
typedef vector<string> VS;
typedef vector<VI> VVI;
typedef pair<int,int> PII;
typedef pair<int,PII> PIII;

bool fill(vector<string> &a) {
	for(int i=0;i<SZ(a);++i) {
		for(int j=0;j<SZ(a[i]);++j) {
			if(a[i][j] == '#') {
				if(j+1 >= SZ(a[0]) || a[i][j+1] != '#') return false;
				if(i+1 >= SZ(a) || a[i+1][j] != '#') return false;
				if(j+1 >=SZ(a[0]) || i+1 >=SZ(a) || a[i+1][j+1] != '#') return false;
				a[i][j] = '/';
				a[i][j+1] = '\\';
				a[i+1][j] = '\\';
				a[i+1][j+1] = '/';
			}
		}
	}
	return true;
}

void print(vector<string> &a) {
	for(int i=0;i<SZ(a);++i) puts(a[i].c_str());
}

void solve() {
	int r,c;
	cin>>r>>c;
	vector<string> data;
	for(int i=0;i<r;++i){
		string s;
		cin>>s;
		data.push_back(s);
	}
	if(fill(data)) {
		print(data);
	} else {
		puts("Impossible");
	}
}

int main() {
	int tc;
	scanf("%d",&tc);
	for(int t=1;t<=tc;++t) {
		printf("Case #%d:\n",t);
		solve();
	}
	return 0;
}


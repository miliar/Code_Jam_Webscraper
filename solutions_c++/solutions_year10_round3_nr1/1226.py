#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cfloat>
#include <climits>
#include <cctype>
#include <cmath>
#include <cassert>
#include <ctime>

#include <iostream>
#include <iomanip>
#include <algorithm>
#include <sstream>
#include <string>
#include <vector>
#include <deque>
#include <queue>
#include <stack>
#include <map>
#include <set>
#include <bitset>
#include <numeric>

using namespace std;

typedef long long ll;
typedef unsigned long long ull;

#define eps 1e-10
#define inf 0x3f3f3f3f

#define console cout
#define dbg(x) //console << #x << " == " << x << endl
#define print(x) //console << x << endl

int bit[1<<14];
pair<int, int> pi[1<<14];
int N;

void update(int idx, int val){
	//dbg(idx);
	while(idx < (1<<14)){
		bit[idx] += val;
		idx += idx & (-idx);
	}
}
int query(int idx){
	int ret = 0;
	print("query");
	while(idx){
		ret += bit[idx];
		dbg(idx);
		dbg(bit[idx]);
		idx -= idx & (-idx);
		
	}
	return ret;
}
int read(){
	scanf("%d", &N);
	memset(bit,0,sizeof bit);
	for(int i =0 ; i < N; i++){
		scanf("%d%d", &pi[i].first, &pi[i].second);
		update(pi[i].second,1);
	}
	return 1;
}
void process(){
	long long ret = 0;
	sort(pi, pi+N);
	for(int i = 0; i < N; i++){
		//if(pi[i].first < pi[i].second){
			dbg(query(pi[i].second-1));
			dbg(pi[i].second);
			ret += query(pi[i].second-1);
		//}
		update(pi[i].second, -1);
	}
	printf("%lld\n", ret);
}
// BEGIN CUT HERE
int main() {
//freopen("out.txt","w",stdout);
//freopen("out.txt","w",stderr);
	
	int casos;
	scanf("%d", &casos);
	for(int i = 1; i <= casos && read(); i++){
		printf("Case #%d: ", i);
		process();
	}
	return 0;
}
// END CUT HERE 

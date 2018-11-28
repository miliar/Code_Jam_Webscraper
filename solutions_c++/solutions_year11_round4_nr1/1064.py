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
#define dbg(x) console << #x << " == " << x << endl
#define print(x) console << x << endl

int X,R,S,t,N;
int p[1001][3];
multiset<double> ss;
int read(){
	cin >> X >> R >> S >> t >> N;
	ss.clear();
	int tt = X;
	for(int i = 0; i < N; i++){
		cin >> p[i][0] >> p[i][1] >> p[i][2];
		tt -= p[i][1]-p[i][0];
		for(int j = p[i][0]; j < p[i][1]; j++)ss.insert(p[i][2] + 0.0);
	}
	
	for(int i = 0; i < tt; i++)ss.insert(0.0+0.0);
	return 1;
}

void process(){
	int qtd = 0;
	double tt = t;
	double ret = 0.0;
	while(tt > 0 && !ss.empty()){
		double dd = *(ss.begin());
		ss.erase(ss.begin());
		if(tt < 1.0/(dd+S)){
			ret += tt + (1.0-(dd+S)*tt)/(dd+R);
			break;
		}
		tt -= 1.0/(dd+S);
		ret += 1.0/(dd+S);
	}
	for(set<double>::iterator it = ss.begin(); it != ss.end(); it++){
		ret += 1.0/((*it) + R);
	}
	printf("%.10lf\n", ret);
}
// BEGIN CUT HERE
int main() {
//freopen("out.txt","w",stdout);
//freopen("out.txt","w",stderr);
	int casos;
	scanf("%d", &casos);
	for(int i = 1; i <= casos && read(); i++){
		fprintf(stderr, "i(%d)\n", i);
		printf("Case #%d: ", i);
		process();
	}
	return 0;
}
// END CUT HERE 

#include <iostream>
#include <sstream>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>

#include <vector>
#include <string>
#include <queue>
#include <map>
#include <set>

#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

typedef vector<int> vi; 
typedef vector<vi> vvi;
typedef vector<string> vs;
#define sz(a) int((a).size()) 
#define pb push_back 
#define all(c) (c).begin(),(c).end() 
#define rep(i, n) for(int i = 0; i < n; ++i) 
#define foreach(it, c) for(__typeof((c).begin()) it = (c).begin(); it != (c).end(); ++it) 

#define TRACE(x...) x
#define watch(x) TRACE(cout << #x" = " << x << endl)
#define watcharr(i, x) TRACE(cout << #x" = "); rep(i, sz(x)) cout << x[i] << " "; cout << endl

string d[31];

void init() 
{
	d[2] = "027";
	d[3] = "143";
	d[4] = "751";
	d[5] = "935";
	d[6] = "607";
	d[7] = "903";
	d[8] = "991";
	d[9] = "335";
	d[10] = "047";
	d[11] = "943";
	d[12] = "471";
	d[13] = "055";
	d[14] = "447";
	d[15] = "463";
	d[16] = "991";
	d[17] = "095";
	d[18] = "607";
	d[19] = "263";
	d[20] = "151";
	d[21] = "855";
	d[22] = "527";
	d[23] = "743";
	d[24] = "351";
	d[25] = "135";
	d[26] = "407";
	d[27] = "903";
	d[28] = "791";
	d[29] = "135";
	d[30] = "647";
}

int main() {
	
	int t, n;
	scanf("%d", &t);
	
	init();
	
	rep(z, t) 
	{
		scanf("%d", &n);	
		
		printf("Case #%d: %s\n", z + 1, d[n].c_str());
	}
	
	return 0;
	
}


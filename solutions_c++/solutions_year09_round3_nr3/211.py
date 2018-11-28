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

using namespace std;

typedef long long ll;
typedef unsigned long long ull;

#define eps 1e-10
#define inf 0x3f3f3f3f

#define fr(x,y,z) for(int x = (y); x < (z); x++)

#define console cout
#define dbg(x) console << #x << " == " << x << endl
#define print(x) console << x << endl

int p, q;
int seq[1000];

void read() {
	scanf("%d %d",&p,&q);
	seq[0] = 0;
	for(int i = 1; i <= q; i++) {
		scanf("%d",&seq[i]);
	}
	q++;
	seq[q] = p+1;
	
	/*for(int i = 0; i < q; i++) {
		dbg(seq[i]);
	}*/
}

ll dp[210][210];

void process() {
	sort(seq,seq+q);

	dp[0][0] = 0;
	for(int i = 1; i < q; i++) {
		//dp[i][i] += (seq[i] - seq[i-1]);
		//dp[i][i] += (seq[i+1] - seq[i] - 1);
		dp[i][i] = (seq[i] - seq[i-1] - 1) + (seq[i+1] - seq[i] - 1);
		//(seq[i-1] ... seq[i] - 1)
		//(seq[i]+1 ... seq[i+1])
		
		//printf(">> %d -> ",seq[i]);
		//dbg(dp[i][i]);
		dp[i+1][i] = dp[i][i-1] = 0;
	}
	dp[q+1][q] = 0;dp[q][q-1] = 0;
	
	//dbg(q);
	
	for(int t = 1; t <= q; t++) {
		for(int i = 1; i + t < q; i++) {
			ll& r = dp[i][i+t];
			r = inf;
			for(int k = i; k <= i+t; k++) {
				//dbg(k);
				r <?= dp[i][k-1] + dp[k+1][i+t];
			}
			//
			r += seq[i+t+1] - seq[i-1] - 2;
			/*dbg(i);
			dbg(i+t);
			dbg(r);
			print("----------------");*/
		}
	} 
	
	
	//printf("%d\n",dp[1][q-1]);
	cout << dp[1][q-1] << endl;
	
}

int main() {

	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	
	int t;
	scanf("%d",&t);
	for(int i = 1; i <= t; i++) {
		read();
		printf("Case #%d: ",i);
		process();
	}	
	return 0;
	
}

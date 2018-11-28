#include <queue>
#include <algorithm>
#include <set>
#include <map>
#include <cmath>
#include <vector>
#include <cstdio>
#include <complex>
#include <stack>
#include <cctype>
#include "assert.h"
#include <cstdlib>
#include <iostream>

#define PB push_back
#define MP make_pair
#define FR(i,n) for( long long i = 0; i < n; i ++ )
#define FOR(i,a,n) for(long long i = a; i < n; i ++)
#define FREACH(it,v) for( typeof(v.end()) it = v.begin(); it != v.end(); it ++ )
#define EPS 1e-9
using namespace std;
typedef long long ll;
const int NITERS=100000;

int d[10001], l[10001];
bool dp[10000][10000];

int main() {
	int T;
	scanf("%d",&T);
	FR(i,T) {
		cout << "Case #" << i+1 << ": ";
		int N;
		scanf("%d",&N);
		FR(i,N) {
			scanf("%d %d",&d[i],&l[i]);
		}
		int DD;
		scanf("%d",&DD);
		int left_pos=0, right_pos=2*d[0];
		if(right_pos>=DD) {
			cout << "YES" << endl;
			continue;
		}
		memset(dp,0,sizeof(dp));
		FR(i,N) {
			if(d[i]>=left_pos&&d[i]<=right_pos) {
				dp[0][i]=true;
			}
		}
		
		
		FR(i,N) {
			FR(j,N) {
				if(dp[i][j]) {
				//	cout << i << " " << j << endl;
					for(int k=i+1;k<N;k++) {
						if(d[k]<=d[j]+min(l[j],d[j]-d[i])) {
							dp[j][k]=true;
						} else {
							break;
						}
					}
					if(d[j] + min(l[j],d[j]-d[i]) >= DD) {
						cout << "YES" << endl;
						goto NXT;
					}
				}
			}
		}
		cout << "NO" << endl;
		
	NXT:;
	}
}
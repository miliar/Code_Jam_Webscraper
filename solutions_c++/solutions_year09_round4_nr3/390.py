#include <iostream>
#include <sstream>
#include <cstring>
#include <cstdio>
#include <cassert>
#include <vector>
#include <queue>
using namespace std;

vector<vector<int> > words;
#define fu(i,m,n) for(int i=m; i<n; i++)
typedef long long i64;

inline int sgn(int x) {
	return x?x>0?1:-1:0;
}

int price[200][200];
int ord[200][200];
int n,k;
int dp[1<<17];
vector<int> pos;

int doit(int msk) {
	int& ret=dp[msk];
	if(ret+1) return ret;
	if(msk+1==(1<<n)) return 0;
	ret=1000000;
	for(int i=0; i<pos.size(); i++) {
		int msk2=pos[i];
		if((msk|msk2) == msk) continue;
		ret=min(ret, doit(msk|msk2)+1);
	}
	return ret;
}

int main(void) {
	int T;
	cin >> T;
	fu(t,0,T) {
		cin >> n >> k;
		fu(i,0,n) fu(j,0,k) cin >> price[i][j];
		fu(i,0,n) fu(j,0,n) {
			ord[i][j]=sgn(price[j][0]-price[i][0]);
			fu(h,0,k) {
				if(sgn(price[j][h]-price[i][h])!=ord[i][j]) {
					ord[i][j]=0;
					break;
				}
			}
		}
		if(false) fu(i,0,n) {
			fu(j,0,n) cout << ord[i][j] << "\t";
			cout << endl;
		}
		memset(dp,-1,sizeof(dp));
		pos.clear();
		fu(msk,0,1<<n) {
			bool good=true;
			fu(j,0,n) if(msk&(1<<j)) fu(k,j+1,n) if(msk&(1<<k)) if(ord[j][k]==0) { good=false; break; }
			if(good) { pos.push_back(msk);
				//cout << msk << endl;
			}
		}
		cout << "Case #" << t+1 << ": " << doit(0) << endl;
	}
}

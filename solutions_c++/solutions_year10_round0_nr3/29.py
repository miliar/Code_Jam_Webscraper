#include <cstring>
#include <string.h>
#include <map>
#include <deque>
#include <queue>
#include <stack>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <algorithm>
#include <vector>
#include <set>
#include <complex>
#include <list>

using namespace std;
typedef long long ll;

int n,N;
ll arr[1010],s[1010],next[1010];
bool vis[1010];
#define SMALL
#define LARGE
int main() {
	freopen("a.txt", "rt", stdin);
//	freopen("a-small.out","wt",stdout);
#ifdef SMALL
	freopen("C-small-attempt2.in","rt",stdin);
	freopen("C-small.out","wt",stdout);
#endif
#ifdef LARGE
	freopen("C-large.in","rt",stdin);
	freopen("C-large.out","wt",stdout);
#endif

	ll r,k;
	cin >> N;
	for(int nn = 1 ; nn <= N ; nn++ ) {
		cin>>r>>k>>n;
		memset(arr,0,sizeof arr);
		memset(s,0,sizeof s);
		memset(next,0,sizeof next);
		for(int i = 0 ; i < n; i++)
			cin>>arr[i];
//		int cur = 0;
//		int turn = 0;
//		int money = 0;
//		while( turn < r ){
//			int tot = 0;
//			while(1){
//				if( tot + arr[cur] > k )
//					break;
//				tot
//			}
//			turn++;
//		}
		for (int i = 0; i < n; ++i) {
			ll sum = 0;
			int j = i;
			do{
				if( sum + arr[j] > k )
					break;
				sum += arr[j++];
				if( j == n )
					j = 0;
				if( i == j )
					break;
			}while(1);
			s[i] = sum;
			next[i] = j;
		}
		memset(vis,0,sizeof vis);
		int i = 0;
		vector <ll> seq;
		vector <ll> cumS(1,0);
		ll prev = 0;
		while( !vis[i] ){
			seq.push_back(i);
			cumS.push_back(s[i]+prev);
			prev = cumS.back();
			vis[i] = 1;
			i = next[i];
		}
		vector <ll> realSeq, cumRS(1,0);
		bool found = 0;
		int bef = 0;
		ll useless = 0;
		prev = 0;
		for (int j = 0;  j < seq.size(); ++j) {
			if( seq[j] == i ){
				bef = j;
				found = 1;
			}
			if( found ){
				realSeq.push_back(seq[j]);
				cumRS.push_back(s[seq[j]]+prev);
				prev = cumRS.back();
			}
			else
				useless = cumS[j+1];
		}
		ll res = 0;
		if( r < seq.size() )
			res = cumS[r];
		else{
			r -= bef;
			res += useless;
			res += (r/realSeq.size()) *prev;
			res += cumRS[(r%realSeq.size())];
		}
		cout << "Case #" << nn << ": ";
		cout << res << endl;
	}
	return 0;
}

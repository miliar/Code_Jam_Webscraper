/*
Author : OmarEl-Mohandes
PROG   : C
LANG   : C++
*/
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
#include <memory.h>
using namespace std;
#define pb push_back
#define all(v) v.begin(),v.end()
#define sz size()
#define rep(i,m) for(int i=0;i<m;i++)
#define REP(i,k,m) for(int i=k;i<m;i++)
#define mem(a,b) memset(a,b,sizeof(a))
#define mp make_pair
typedef stringstream ss;
typedef pair<int, int> pii;
typedef vector<pii> vpii;
typedef vector<string> vs;
typedef vector<int> vi;
typedef vector<vector<int> > vii;
typedef long long ll;
#define oo ((int)1e9)
ll arr[1001] ;
int next[1001];
ll ans[1001];
int main()
{
	freopen("C.in" , "rt" , stdin);
	freopen("C.out" , "wt" , stdout);
	ll R , K , N , T;
	cin >> T;
	for (int cas = 0; cas < T; ++cas) {
		cin >> R >> K >> N;
		memset(arr, 0 , sizeof arr);
		memset(ans, 0 , sizeof ans);
		memset(next, 0 , sizeof next);
		for (int k = 0; k < N; ++k)cin >> arr[k];
		ll res = 0 , countR = 0 ;
		for (int i = 0; i < N; ++i) {
			int r =K , id = i;
			for (int j = 0; j < N && r-arr[id] >= 0; ++j) {
				r -= arr[id] , id = (id+1)%N;
			}
			ans[i] = K - r;
			next[i] = id;
		}
		ll  wr = 0;
		for (int i = 0 ; countR < R ;countR++, wr = i = next[i])res+=ans[i];
				res+=((R / countR)-(ll)1)*res;
				countR += ((R / countR) - (ll)1 )*countR;
				for(int i = countR ; i < R ; i++)
				{
					res+=arr[wr];
					wr = next[wr];
				}
		cout << "Case #" << cas+1 << ": " << res << endl;
	}
	return 0;
}

#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>


using namespace std;

#define INF 999999
#define pb push_back
#define sz(x) ((int)((x).size()))
#define all(x) (x).begin(),(x).end()
#define db double
#define ll long long
#define rep(i,n) for (int (i)=0; (i)<(n); ++(i))
#define forn(i,a,n) for (int (i)=(a); (i)<(n); ++(i))
#define VI vector<int>
#define VB vector<bool>

#define EPS 10E-5
int cmp(db a,db b){
	db tmp = a - b;
	if (fabs(tmp) < EPS)
		return 0;
	else if (tmp > 0)
		return 1;
	else return -1;
}
#define MAXN 1024
bool bit[MAXN][MAXN];
bool mark[MAXN][MAXN];
int n,m;
void print(){
	rep(i,n){
		rep(j,m)
			cout << bit[i][j];
		cout << endl;
	}	
}
bool check(int a, int b, int k){
	for (int i = a; i < a + k; ++ i)
		for (int j = b; j < b + k; ++ j)
			if (mark[i][j])
				return 0;
	for (int i = a + 1; i < a + k; ++ i)
		for (int j = b; j < b + k; ++ j)
			if (bit[i][j] == bit[i-1][j])
				return 0;
	for (int i = a; i < a + k; ++ i)
		for (int j = b+1; j < b + k; ++ j)
			if (bit[i][j] == bit[i][j-1])
				return 0;
	return 1;
}
int anscnt;
int ans[MAXN];
void mk(int a, int b, int k){
	for (int i = a; i < a + k; ++ i)
		for (int j = b; j < b + k; ++ j)
			mark[i][j] = 1;
}
void find(int k){
	rep(i,n-k+1)
		rep(j,m-k+1)
			if (check(i,j,k)){
				mk(i,j,k);
				ans[k]++;
			}
}

void sol(){
	for (int i = min(n,m); i >= 1; -- i)
		find(i);
}

int main(){
	freopen("input.txt","rt",stdin); freopen("output.txt","wt",stdout);
	int C;
	cin >> C;

	rep(qwer,C){

		cin >> n >> m;
		char k;
		rep(i,n)
			rep(j,m)
			mark[i][j] = 0;
		rep(i,MAXN)
			ans[i] = 0;
		rep(i,n)
			rep(j,m/4){
				cin >> k;
				if (k >= 'A' && k <= 'F')
					k = k - 'A' + 10;
				for (int l = 0; l < 4; ++ l)
					bit[i][j*4+l] = (k >> (4-l-1)) & 1;	
		}
		//print();
		bool tmp = check(11,0,4);

		sol();
		//find(4);

		anscnt = 0;

		rep(i,MAXN)
			if (ans[i])
				++anscnt;
		printf("Case #%d: %d\n",qwer+1,anscnt);
		for (int i = MAXN - 1; i >= 1; -- i)
			if (ans[i])
				cout << i << " " << ans[i] << endl;

	}
	return 0;
}
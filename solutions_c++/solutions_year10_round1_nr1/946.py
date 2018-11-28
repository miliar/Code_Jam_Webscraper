/*
Author : OmarEl-Mohandes
PROG   : A
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
#include <map>
#include <complex>
#include <valarray>
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
bool BFS(vector<string>mat , char c , int K)
{
	for (int i = 0; i < mat.size(); ++i) {
		for(int j = 0 ; j < mat.size() ; j ++){
			if(mat[i][j] != c)continue;
			int f = 0;
			int ii = i , jj = j;
			while(ii < mat.size()&&mat[ii++][jj] == c)f++;
			if(f >= K)return 1;
			ii = i ;
			f = 0;
			while(jj < mat[0].size()&&mat[ii][jj++] == c)f++;
			if(f >= K)return 1;
			jj = j;
			f = 0;
			while(ii < mat.size()&&jj < mat[0].size()&&mat[ii++][jj++] == c)f++;
			if(f >= K)return 1;
			f = 0;
			ii = i;jj = j;
			while(ii < mat.size()&& jj >= 0&& mat[ii++][jj--] == c)f++;
			if(f >= K)return 1;
		}
	}
	return 0;
}
int main()
{
	freopen("A.in" , "rt" , stdin);
	freopen("A.out" , "wt" , stdout);
	int t;
	cin >> t;
	for (int i = 0; i < t; ++i) {
		int n , K;
		cin >> n >> K;
		vector<string>v(n) , a;
		for (int j = 0; j < n; ++j) {
			cin >> v[j];
		}
		for (int k = 0 ; k <  n ; k ++) {
			string t = "";
			for (int j = 0; j < n; ++j) {
				t += v[j][k];
			}
			reverse(all(t));
			a.pb(t);
		}
		for (int k = n-1; k >= 0; --k) {
			for (int j = 0; j < n; ++j) {
				int kk = k+1 , jj = j;
				bool f = 0;
				if(a[k][j] == '.')continue;
				while(kk <= n-1 && a[kk][jj] == '.')kk++,f=1;
				kk--;
				if(f)
				swap(a[kk][jj] , a[k][j]);
			}
		}

		bool r = BFS(a , 'R' , K);
		bool b = BFS(a , 'B' , K);
		if(!r && !b)
			cout << "Case #" << i+1 << ": " << "Neither" << endl;
		if(r && b)
			cout << "Case #" << i+1 << ": " << "Both" << endl;
		if(r && !b)
			cout << "Case #" << i+1 << ": " << "Red" << endl;
		if(!r && b)
			cout << "Case #" << i+1 << ": " << "Blue" << endl;
	}
	return 0;
}

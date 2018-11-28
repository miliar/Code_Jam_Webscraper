/*
Author : OmarEl-Mohandes
PROG   : C
LANG   : C++
*/
#include <map>
#include <string>
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
int getlen(int n)
{
	int r = 0;
	while(n)
		r ++ , n/=10;
	return r;
}
int countn(int n , int a , int b)
{
	int ret = 0 ;
	set<int>vis;
	int len = getlen(n);
	int nn = n;
	while(vis.insert(n).second){
		int mod = 10;
		while(n%mod == 0)
			mod *= 10;
		n = ((n%mod)*(int)pow(10.0 , (len-(getlen(mod)-1))))+(n/mod);
		if(n > nn && n <= b)
			ret ++;
	}
	return ret ;
}
int main()
{
	freopen("test.in" , "rt" , stdin);
	freopen("C.out" , "wt" , stdout);
	int t;
	scanf("%d" , &t);
	int a , b;
	for(int i = 0 ; i < t ; i ++){
		scanf("%d%d" , &a , &b);
		ll res = 0;
		for(int k = a ; k <= b ; k ++)
			res += countn(k , a , b);
		cout << "Case #" << i+1 << ": " << res << endl;
	}

	return 0;
}


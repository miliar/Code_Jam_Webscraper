/*
Author : OmarEl-Mohandes
PROG   : C.cpp
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
int main()
{
	freopen("C.in" , "rt" , stdin);
	freopen("C.out" , "wt" , stdout);
	int t , n;
	scanf("%d" , &t);
	for(int i = 0 ; i < t ; i ++){
		scanf("%d" , &n);
		vi v(n);
		int s = 0, r = 0 , m = 1e9;
		for(int k = 0 ; k < n ; k ++)
		{
			scanf("%d" , &v[k]);
			r ^= v[k];
			s += v[k];
			m = min(m , v[k]);
		}
		if(r != 0)
			printf("Case #%d: NO\n" , i+1);
		else
			printf("Case #%d: %d\n" , i+1 , s-m);
	}
	return 0;
}

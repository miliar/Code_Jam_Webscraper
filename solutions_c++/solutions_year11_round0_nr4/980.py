/*
Author : OmarEl-Mohandes
PROG   : D.cpp
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
	freopen("D.in" , "rt" , stdin);
	freopen("D.out" , "wt" , stdout);
	int t;
	scanf("%d" , &t);
	for(int i = 0 ; i < t ; i ++){
		int n;
		scanf("%d" , &n);
		vi v(n);
		double s = 0;
		for(int k = 0 ; k < n ; k ++)
		{
			scanf("%d",&v[k]);
			s += v[k] != k+1;
		}
		printf("Case #%d: %.6lf\n" , i+1 , s);
	}
	return 0;
}

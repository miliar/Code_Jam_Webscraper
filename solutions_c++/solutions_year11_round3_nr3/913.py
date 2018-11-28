/*
 * B.cpp
 *
 *  Created on: May 22, 2011
 *      Author: marwan
 */

#include <algorithm>
#include <iostream>
#include <cstring>
#include <cstring>
#include <sstream>
#include <complex>
#include <iomanip>
#include <cstdlib>
#include <cstdio>
#include <cmath>
#include <string>
#include <vector>
#include <queue>
#include <deque>
#include <stack>
#include <list>
#include <set>
#include <map>

using namespace std;

#define Fori(i,x,n)     for(int i=((int)x) ; i<=((int)n) ; i++)
#define For(i,n)        Fori(i,0,n-1)
#define Forri(i,x,n)    for(int i=((int)n) ; i>=x ; i--)
#define Forr(i,n)       Forri(i,0,n-1)
#define Forit(it,c)     for(__typeof(c).begin() it=(c).begin();it!=(c).end();it++)
#define all(c)          (c).begin(),(c).end()
#define rall(c)         (c).rbegin(),(c).rend()
#define mem(arr,n)      memset(arr,n,sizeof(arr))
#define MP(x,y)         make_pair((x),(y))
#define pii             pair<int,int>
#define Size(x)         ((int)x.size())

const int oo = (int) 1e9;
const double PI = 2 * acos(0.0);
const long double eps = 1e-12;
int diri[] = { 0, 1, 0, -1 };
int dirk[] = { 1, 0, -1, 0 };

#define TEST
//#define small
//#define large

int main() {
#ifdef TEST
    freopen("a.in", "rt", stdin);
	freopen("a.out" , "wt" , stdout) ;
#endif

#ifdef small
    freopen("a-small.in", "rt", stdin);
	freopen("a-small.out" , "wt" , stdout) ;
#endif

#ifdef large
    freopen("a-large.in", "rt", stdin);
	freopen("a-large.out" , "wt" , stdout) ;
#endif
	int t , d = 1 ;
	scanf ("%d" , &t) ;
	while (t--){
		printf ("Case #%d: " , d++) ;
		int n , l , h ;
		scanf ("%d%d%d" , &n , &l , &h) ;
		vector <int> f (n) ;
		For (i,n)
			scanf ("%d" , &f[i]) ;

		int ans = -1 ;
		for (int i=h ; i>= l ; i--){
			int myf = i ;
			For (k , f.size()){
				if (myf%f[k] != 0 && f[k] %myf != 0)
					goto no ;
			}
			ans = i ;
			no : ;
		}
		if (ans == -1)
			printf ("NO\n") ;
		else
			printf ("%d\n", ans) ;
	}
    return 0;
}

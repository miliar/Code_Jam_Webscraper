/*
 * D.cpp
 *
 *  Created on: May 7, 2011
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


int main() {
#ifndef ONLINE_JUDGE
    freopen("D-large.in", "rt", stdin);
	freopen ("D.out" , "wt" , stdout) ;
#endif
	int t , cnt , n , x , d=1;
	cin >> t ;
	while (t--){
		cnt = 0 ;
		cin >> n ;
		For (i,n){
			cin >> x ;
			cnt += (x != i+1) ;
		}
		printf ("Case #%d: %.6lf\n" , d++ , (double) cnt) ;
	}
    return 0;
}

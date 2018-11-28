/*
 * A.cpp
 *
 *  Created on: May 21, 2011
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


vector < vector <char> > maze ;
int n ;
double WP (int i , vector <vector <char> > &maze){
	double ans = 0.0 ;
	int cnt = 0 ;
	For(k,maze[i].size()){
		if (maze[i][k] == '.')
			continue ;
		cnt ++ ;
		if (maze[i][k] == '1')
			ans+=1.0 ;
	}
	if (cnt == 0)
		return 0.0 ;
	return (double) ans / (double) cnt ;
}

double OWP (int i){
	//cout << "calc OWP for " << i << endl ;

	vector <vector <char> > mymaze = maze ;
	For (k , n)
		mymaze[i][k] = mymaze[k][i] = '.';
	int cnt = 0 ;
	double ans = 0.0 ;
	For (k,n){
		if (k==i || maze[i][k] == '.')
			continue ;
		cnt ++ ;
		double tmp = WP (k , mymaze) ;
		//cout << "for team " << k << " -->  " << tmp << endl;
		ans +=  tmp ;
	}
	if (cnt == 0)
		return 0.0 ;
	return (double) ans / (double) cnt ;
}

double OOWP (int i){
	int cnt = 0 ;
	double ans = 0.0 ;
	For (k,n){
		if (k==i || maze [i][k] == '.')
			continue ;
		cnt ++ ;
		double tmp = OWP (k) ;
		ans += tmp ;
	}
	if (cnt == 0)
		return 0.0 ;
	return (double) ans / (double) cnt ;
}
#define TEST
//#define small
//#define large
int main() {
#ifdef TEST
    freopen("A-l.in", "rt", stdin);
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
		printf ("Case #%d:\n" , d++) ;
		scanf ("%d" , &n) ;
		maze = vector <vector <char> > (n) ;
		For (i,n){
			string s ;
			cin >> s ;
			For (k,n){
				maze[i].push_back(s[k]) ;
			}
		}
		For (i,n){
			double wp , owp , oowp ;
			wp = WP (i,maze) , owp = OWP (i) , oowp = OOWP (i) ;
			double RPI = (0.25* wp) + (0.50 * owp) + (0.25 *oowp) ;
			printf ("%.8lf\n" , RPI) ;
		}
	}
    return 0;
}

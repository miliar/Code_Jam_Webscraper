/*
 * B.cpp
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
int c , n , t , dd =1 , d;


int main() {
#ifndef ONLINE_JUDGE
	freopen ("a.in" , "rt" , stdin) ;
    freopen("a.out", "wt", stdout);
#endif
	cin >> t ;
	while (t--){
		bool op[128][128] ;
		memset (op , 0 , sizeof(op));
		map <pair<char , char>, char> mp ;
		cin >> c;
		For (i,c) {
			string s ;
			cin >> s ;
			mp[MP(s[0] , s[1])] = s[2] ;
			mp[MP(s[1] , s[0])] = s[2] ;
		}
		cin >> d ;
		For (i,d){
			string s ;
			cin >> s ;
			op[(int)s[0]][(int)s[1]] = 1 ;
			op[(int)s[1]][(int)s[0]] = 1 ;
		}
		cin >> n ;
		vector <char> v ;
		For (i,n){
			char c ;
			cin >> c ;
			if (!v.size()){
				v.push_back(c);
				continue ;
			}
			if (mp[MP(c,v.back())]){
				char x = mp[MP(c,v.back())] ;
				v.pop_back();
				v.push_back(x) ;
				continue ;
			}
			else {
				For(k , v.size()){
					if (op[(int)c][(int)v[k]]){
							v.clear() ;
							goto done ;
					}
				}
			}
			v.push_back(c) ;
			done : ;
		}
		printf ("Case #%d: [" , dd++) ;
		string ss = "" ;
		For (i,v.size()){
			cout << ss << v[i] ;
			ss = ", " ;
		}
		printf ("]\n");
	}
    return 0;
}

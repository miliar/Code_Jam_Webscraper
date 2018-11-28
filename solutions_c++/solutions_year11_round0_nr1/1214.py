/*
 * A.cpp
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
	//freopen("a-small.in", "rt", stdin);
	freopen("a-small.out", "wt", stdout);
#endif
	int t , n , x , co , cb , res , d=1 ;
	cin >> t ;
	while (t--){
		deque <pii> o , b ;
		co = cb = 1 ;
		res = 0 ;
		cin >> n ;
		For(i,n){
			char c ;
			cin >> c >> x ;
			if (c == 'O')
				o.push_back(MP(i,x)) ;
			else
				b.push_back(MP(i,x)) ;
		}
		while (true){
			if (o.size() && b.size()){
				if (o.front().first < b.front().first){ // the next move is for orange ...
					res += abs (o.front().second - co)+1 ;


					if (abs (o.front().second - co) < abs (b.front().second - cb))
						cb += (abs(o.front().second - co)+1)*((cb>b.front().second)?-1:1) ;
					else
						cb = b.front().second ;
					co = o.front().second ;
					o.pop_front() ;
				}
				else { // the next move is for Blue ..
					res += abs (b.front().second - cb)+1 ;


					if (abs (b.front().second - cb) < abs (o.front().second - co))
						co += (abs(b.front().second - cb)+1)*((co>o.front().second)?-1:1) ;
					else
						co = o.front().second ;
					cb = b.front().second ;
					b.pop_front() ;
				}
			}
			else if (o.size()){
				For(i,o.size()){
						res += abs(o[i].second - co)+1 ;
						co = o[i].second ;
				}
				break ;
			}
			else if (b.size()){
				For(i,b.size()){
					res += abs (b[i].second - cb)+1 ;
					cb = b[i].second ;
				}
				break ;
			}
			else break ;
		}
		printf("Case #%d: %d\n",d++ , res) ;
	}

	return 0;
}

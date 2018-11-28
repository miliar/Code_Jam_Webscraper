/*
 * A.cpp
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
int diri[] = { 1, 1, 0};
int dirk[] = { 0, 1, 1};

#define TEST
//#define small
//#define large

int main() {
#ifdef TEST
    freopen("a.in", "rt", stdin);
	freopen("a.out" , "wt" , stdout) ;
#endif

#ifdef small
    freopen("A-small-attempt0.in", "rt", stdin);
	freopen("A-small.out" , "wt" , stdout) ;
#endif

#ifdef large
    freopen("A-large-attempt0.in", "rt", stdin);
	freopen("A-large.out" , "wt" , stdout) ;
#endif
	int t , d = 1 ;
	scanf ("%d" , &t) ;
	while (t--){
		printf ("Case #%d:\n" , d++) ;
		int r , c ;
		scanf ("%d%d" , &r , &c) ;
		vector <vector <char> > maze (r , vector <char> (c)) ;
		int cntH = 0 ;
		For (i,r){
			string s ;
			cin >> s ;
			For (k,c){
				maze[i][k] = s[k] ;
				cntH += (s[k] == '#') ;
			}
		}
		vector <vector <bool> > vis (r , vector <bool> (c , 0)) ;
		vector <pii> starts ;
		For (i,r-1){
			For (k,c-1){
				if (maze[i][k] == '#' && !vis[i][k]){
					int ni , nk ;
					bool isS = true ;
					For (l,3){
						ni = i + diri[l] ;
						nk = k + dirk[l] ;
						if (maze[ni][nk] != '#' || vis[ni][nk]){
							isS = false ;
							break ;
						}
					}
					if (isS){
						starts.push_back(MP(i,k)) ;
						For (l,3){
							ni = i + diri[l] ;
							nk = k + dirk[l] ;
							vis[ni][nk] = 1 ;
						}
					}
				}
			}
		}
		if (cntH != (int)starts.size()*4){
			printf ("Impossible\n") ;
			continue ;
		}
		For (h,starts.size()){
			int i = starts[h].first , k = starts[h].second ;
			maze[i][k] = maze[i+1][k+1] = '/' ;
			maze[i+1][k] = maze[i][k+1] = '\\' ;
		}
		For (i,r){
			For (k,c)
				cout << maze[i][k] ;
			cout << endl ;
		}


	}
    return 0;
}

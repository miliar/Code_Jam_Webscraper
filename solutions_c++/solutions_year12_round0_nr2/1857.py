/*
Author : OmarEl-Mohandes
PROG   : B
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
int al[31][2];
bool tamam(int i , int j , int k)
{
	if(abs(i-j) > 2 || abs(i-k) > 2 || abs(j-k) > 2)
		return 0;
	return 1;
}
int main()
{
	freopen("test.in" , "rt" , stdin);
	freopen("B.out" , "wt" , stdout);
	memset(al , -1 , sizeof al);
	for(int i = 0 ; i <= 10 ; i ++){
		for(int j = i ; j <= 10 ; j ++){
			for(int k = j ; k <= 10 ; k ++){
				if(!tamam(i,k,j))
					continue;
				bool f = (abs(i-j) == 2) || (abs(i-k) == 2) || (abs(j-k) == 2);
				al[i+j+k][f] = max(i , max(j , k));
			}
		}
	}
	int t , n , s , p , tt;
	scanf("%d" , &t);
	for(int it = 0 ; it < t ; it ++){
		int res = 0;
		scanf("%d%d%d" , &n , &s , &p);
		vector<pair<int , int> > v;
		for(int k = 0 ; k < n ; k ++){
			scanf("%d" , &tt);
			bool f = 0;
			if(al[tt][0] >= p)
				res ++ , f = 1;
			else if(al[tt][1] >= p && s){
				res ++ , s --;
				continue;
			}
			if(al[tt][1] != -1)
				v.pb(mp(f , -al[tt][1]));
		}
		sort(all(v));
		for(int i = 0 ; (i < v.size()) && s; i ++){
			if(v[i].first && -v[i].second < p)
				res --;
			s --;
		}
		printf("Case #%d: %d\n" , it+1 , res);
	}
	return 0;
}


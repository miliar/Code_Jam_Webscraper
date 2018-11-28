/*
Author : OmarEl-Mohandes
PROG   : A.cpp
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
	freopen("A.in" , "rt" , stdin);
	freopen("A.out" , "wt" , stdout);
	int t;
	scanf("%d" , &t);
	for(int i = 0 ; i < t ; i ++){
		int n;
		scanf("%d" , &n);
		char c ;
		int tem;
		queue<int>O , B;
		vector<pair<char , int> >al;
		for(int k = 0 ; k < n ; k ++){
			scanf(" %c%d" , &c , &tem);
			al.pb(mp(c , tem));
			if(c == 'O')
				O.push(tem);
			else
				B.push(tem);
		}
		int o= 1 , b = 1 , count = 0;
		for(int i = 0 ; i < al.size() ; i ++){
			bool f  = al[i].first == 'O';
			while(al[i].first == 'O' && o != al[i].second)
			{
				if(al[i].second < o)
					o --;
				else if(al[i].second > o)
					o ++;
				count++ ;
				if(B.size() && B.front() > b)
					b++;
				else if(B.size() && B.front() < b)
					b--;
			}
			if(f){
				count ++;
				O.pop();
				if(B.size() && B.front() > b)
					b++;
				else if(B.size() && B.front() < b)
					b--;
				continue;
			}
			while(al[i].first == 'B' && b != al[i].second)
			{
				if(al[i].second < b)
					b --;
				else if(al[i].second > b)
					b ++;
			    count++ ;
				if(O.size() && O.front() > o)
					o++;
				else if(O.size() && O.front() < o)
					o--;
			}
			count++;
			if(O.size() && O.front() > o)
				o++;
			else if(O.size() && O.front() < o)
				o--;
			B.pop();
		}
		printf("Case #%d: %d\n" , i+1 , count);
	}
	return 0;
}

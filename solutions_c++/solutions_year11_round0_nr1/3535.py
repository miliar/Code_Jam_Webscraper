#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <queue>
#include <string>
#include <cstring>
using namespace std;

#define FOR(i,a,b)   	for(int (i)=(a);(i)<(b);(i)++)
#define REP(i,a,b)   	for(int (i)=(a);(i)<=(b);(i)++)
typedef long long 		bint;

#define PB           	push_back
#define INF          	1e10
#define DEBUG(___x)     cout<<#___x<<" = ["<<___x<<"]"<<endl
#define SORT(___a)      sort(___a.begin(),___a.end())
#define RSORT(___a)     sort(___a.rbegin(),___a.rend())
#define PI           	3.141592653589793238
#define MP           	make_pair
#define PII          	pair<int,int>
#define ALL(___v)       (___v).begin(), (___v).end()
#define VS           	vector<string>
#define VI           	vector<int>
#define S            	size()
#define print(___v)     {cout<<"[";if(___v.S)cout<<___v[0];FOR(i,1,___v.S)cout<<","<<___v[i];cout<<"]\n";}

int ntm, lo, lb, ls;
VI a, b, seq;

void go(int po, int pb, int io, int ib, int is) {
	
	if(is == ls)return;
	
	if(seq[is] == 0) {
		
		if(po == a[io]) {
			
			ntm++;
			is++;
			io++;
			if(ib < lb && pb < b[ib])pb++;
			else if(ib < lb && pb > b[ib])pb--;
		}
		else if(po < a[io]) {
			
			ntm++;
			po++;
			if(ib < lb && pb < b[ib])pb++;
			else if(ib < lb && pb > b[ib])pb--;
		}
		else {
			
			ntm++;
			po--;
			if(ib < lb && pb < b[ib])pb++;
			else if(ib < lb && pb > b[ib])pb--;
		}
	}
	else {
		
		if(pb == b[ib]) {
			
			ntm++;
			is++;
			ib++;
			if(io < lo && po < a[io])po++;
			else if(io < lo && po > a[io])po--;
		}
		else if(pb < b[ib]) {
			
			ntm++;
			pb++;
			if(io < lo && po < a[io])po++;
			else if(io < lo && po > a[io])po--;
		}
		else {
			
			ntm++;
			pb--;
			if(io < lo && po < a[io])po++;
			else if(io < lo && po > a[io])po--;
		}
	}
	go(po, pb, io, ib, is);
}

int main()
{
	//freopen("A-large.in", "r", stdin);
	//freopen("A.out", "w", stdout);
	
	int T, n;
	
	cin >> T;
	
	FOR(t,0,T) {
		
		int now;
		char ch;
		ntm = 0;
		a.clear();
		b.clear();
		seq.clear();
		
		cin >> n;
		
		FOR(i,0,n) {
			
			cin >> ch >> now;
			if(ch == 'O') {
				seq.PB(0);
				a.PB(now);
			}
			else {
				
				seq.PB(1);
				b.PB(now);
			}
			//val.PB(now);
		}
		lo = a.S;
		lb = b.S;
		ls = seq.S;
		
		
		go(1,1,0,0,0);
		
		
		printf("Case #%d: %d\n",t+1, ntm );
	}
	
	
	return 0;
}


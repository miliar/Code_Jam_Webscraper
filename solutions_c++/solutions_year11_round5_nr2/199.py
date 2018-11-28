#define DBG
#include <algorithm>
#include <bitset>
#include <cassert>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <deque>
#include <iostream>
#include <list>
#include <map> 
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <utility>
#include <vector>
using namespace std;

#ifdef DBG
#define debug(fmt, ...) printf(fmt, ## __VA_ARGS__ )
#else
#define debug(fmt, ...)
#endif

int __tmp;
#define scanf __tmp = scan ## f

#define REP(ii,nn) for(int (ii)=0; (ii)<int(nn); (ii)++)
#define FOR(ii,bb,ee) for(int (ii)=(bb); (ii)<=(ee); (ii)++)
#define REPD(ii,nn) for(int (ii)=(nn)-1; (ii)>=0; (ii)--)
#define FORD(ii,ee,bb) for(int (ii)=(ee); (ii)>=(bb); (ii)--)
#define FORE(ii,vv) for(__typeof((vv).begin()) ii=(vv).begin(); (ii)!=(vv).end(); (ii)++)
#define ST first
#define ND second
#define PB push_back
#define PP pop_back
#define MP make_pair

template<typename S,typename T>
pair<S,T> operator+(const pair<S, T>& lhs, const pair<S, T>& rhs) {
	return pair<S,T>(lhs.ST + rhs.ST, lhs.ND + rhs.ND);
}
template<typename S,typename T>
pair<S,T> operator-(const pair<S, T>& lhs, const pair<S, T>& rhs) {
	return pair<S,T>(lhs.ST - rhs.ST, lhs.ND - rhs.ND);
}
template<typename S,typename T, typename K>
pair<S,T> operator*(const pair<S, T>& lhs, const K& rhs) {
	return pair<S,T>(lhs.ST * rhs, lhs.ND * rhs);
}
template<typename S,typename T>
pair<S,T>& operator+=(pair<S, T>& lhs, const pair<S, T>& rhs) {
	lhs.ST += rhs.ST;
	lhs.ND += rhs.ND;
	return lhs;
}
template<typename S,typename T>
pair<S,T>& operator-=(pair<S, T>& lhs, const pair<S, T>& rhs) {
	lhs.ST -= rhs.ST;
	lhs.ND -= rhs.ND;
	return lhs;
}
template<typename S,typename T>
const char* operator~(const pair<S, T>& rhs) {
	stringstream s; 
	s << "(" << rhs.ST << "," << rhs.ND << ")";
	string* r = new string; 
	s >> *r;
	return r->c_str();
}

const int maxn = 10100;
int cards[maxn * 100];
int t[maxn];
int helper[maxn * 100];
int n;

bool possible(int s) {
	REP(i,maxn * 2) t[i] = helper[i] = 0;
	REP(i,maxn) {
		t[i] = cards[i];
		helper[i] = 0;
	}
	REP(i,maxn) while(t[i]) {
		if(helper[i]) {
			--t[i];
			--helper[i];
			++helper[i + 1];
		} else {
			REP(j,s) {
				if(!t[i + j]) return false;
				--t[i + j];
			}
			helper[i + s]++;
		}
	}
	return true;
}

int main() {
	int z; scanf("%d", &z);
	FOR(zz,1,z) {
		scanf("%d", &n);
		REP(i,maxn) cards[i] = 0;
		REP(i,n) {
			int c; scanf("%d", &c);
			cards[c]++;
		}
		int b = 0;
		int e = n;
		while(b < e) {
			int s = (b + e + 1) / 2;
			if(possible(s)) b = s;
			else e = s - 1;
		}
		printf("Case #%d: %d\n", zz,b);
	}
	return 0;
}


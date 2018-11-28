//============================================================================
// Name        : Debug.cpp
// Author      : Yunan Luo
// Version     : 1.0.0
// Copyright   : cc
// Description : C++, Ansi-style
//============================================================================

#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <iostream>
//#include <sstream>
#include <map>
#include <set>
#include <queue>
//#include <stack>
//#include <fstream>
//#include <cstdlib>
//#include <cctype>
//#include <numeric>
//#include <iomanip>
//#include <bitset>
//#include <list>
//#include <stdexcept>
//#include <functional>
//#include <utility>
//#include <ctime>
using namespace std;
#define cpr(n) cout.precision(n);
#define PB push_back
#define MP make_pair
#define REP(i,n) for(int i=0;i<(n);++i)
#define FOR(i,l,h) for(int i=(l);i<=(h);++i)
#define FORD(i,h,l) for(int i=(h);i>=(l);--i)
#define long long LL
const int MONTH_DAY[13] = { 0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31 };
const double EPS = 1e-9;
const double PI = acos(-1.0);
const int INF = (int)(1e9 + 7.5);

inline int max(int a, int b) { return a > b ? a : b; }
inline int min(int a, int b) { return a < b ? a : b; }
inline int triangle_area(int x1, int y1, int x2, int y2, int x3, int y3) { return (x2 - x1) * (y3 - y1) - (x3 - x1) * (y2 - y1); }
int gcd(int x, int y){	if(y==0) return x;	else return gcd(y, x%y);}
//const int MAXN = 1000040;
char a[10][10];
bool row(char c){
	REP(i,4){
		int sum=0;
		REP(j,4) if(a[i][j]==c || a[i][j]=='T') sum++;
		if (sum==4) return true;
	}
	return false;
}

bool col(char c){
	REP(j,4){
		int sum=0;
		REP(i,4) if(a[i][j]==c || a[i][j]=='T') sum++;
		if (sum==4) return true;
	}
	return false;
}

bool diag(char c){
	int sum=0;
	REP(i,4) if(a[i][i]==c || a[i][i]=='T') sum++;
	if (sum==4) return true;

	sum=0;
	REP(i,4) if(a[i][3-i]==c || a[i][3-i]=='T') sum++;
	if (sum==4) return true;	
		
	return false;	
}	
int main() {
    freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int T;
	cin>>T;
	FOR(TestCase,1,T){
		cout<<"Case #"<<TestCase<<": ";
		bool complete = true;
		REP(i,4) REP(j,4) {
			cin>>a[i][j];
			if (a[i][j]=='.') complete=false;
		}
		
		if(row('X') || col('X') || diag('X')) cout<<"X won"<<endl;
		else if (row('O') || col('O') || diag('O')) cout<<"O won"<<endl;
		else if (complete) cout<<"Draw"<<endl;
		else cout<<"Game has not completed"<<endl;
	}
	fclose(stdin);
	fclose(stdout);
    return 0;
}

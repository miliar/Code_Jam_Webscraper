#include <algorithm>  
#include <iostream>  
#include <sstream>  
#include <string>  
#include <vector>  
#include <queue>  
#include <set>  
#include <map>  
#include <cstdio>  
#include <cstdlib>  
#include <cctype>  
#include <cmath>  
#include <list> 
#include <unordered_map>

using namespace std;

typedef map<char,char> dict;
typedef vector<int> VI;
typedef long long LL;
#define VLL vector<long long>
#define SZ(v) ((int)(v).size())  
#define FOR(i,a,b) for(int i=(a);i<(b);++i)  
#define REP(i,n) FOR(i,0,n)  
#define FORE(i,a,b) for(int i=(a);i<=(b);++i)  
#define REPE(i,n) FORE(i,0,n)  
#define FORSZ(i,a,v) FOR(i,a,SZ(v))  
#define REPSZ(i,v) REP(i,SZ(v))  

char buf[1024];

int ni(){
	int i;
	scanf("%d", &i);
	return i;
}

double nd(){
	double i;
	scanf("%f", &i);
	return i;
}

string ns() { 
	scanf( "%s", buf ); return buf; 
}

string nl() {
	return gets(buf);
}

string to_str(int n) {
	itoa(n, buf, 10);
	return buf;
}

template<class T>
T from_str(string s) {
	istringstream ss(s);
	T out;
	ss >> out;
	return out;
}

int base(int digit) {
	int n = 1;
	for (int i = 0; i < digit; i++) n *= 10;
	return n / 10;
}

/* 1123 -> 1231 */
int rotate(int n, int base, int offset) {
	n = n - offset;
	int s = n / base;
	n %= base;
	n *= 10;
	n += s;
	return offset + n;
}

bool found(int *ar, int n, int val)
{
	for (int i = 0; i < n; i++) {
		if (ar[i] == val) return true;
	}
	return false;
}

void solve_c(int cases)
{
	int A, B;
	int log[8];

	for (int i = 0; i < cases; i++) {
		int result = 0;
		A = ni();
		B = ni();
		int digit = to_str(A).length();
		int bs = base(digit);
		int offset = 10 * bs;
		A += offset;
		B += offset;

		for (int j = A; j <= B; j++) {
			int jr = j;
			int r = 0;

			for (int k = 0; k < digit - 1; k++) {
				jr = rotate(jr, bs, offset);
				if (jr > j && jr <= B && !found(log, r, jr)) {
					log[r++] = jr;
				}
			}
			result += r;
		}
		printf("Case #%d: %d\n", i+1, result);
	}

}

int main(void)
{
	freopen("C-large.in", "r", stdin);
	freopen("c1.out", "w", stdout);

	int cases = ni();

	solve_c(cases);
}
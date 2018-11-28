//be name oo
#include <cstdio>
#include <iostream>
#include <algorithm>
#include <set>
#include <string>
#include <map>
#include <utility>
#include <cstring>
#include <sstream>
#include <complex>
#include <vector>

#define FOR(i, n) for(int i = 0; i < (n); i++)
#define SZ(x) ((int)x.size())
#define PB push_back
#define F first
#define S second

using namespace std;
typedef pair<int, int> joft;
typedef complex<double> point;

const int MAX_N = 60 + 10;

char str[MAX_N];
int last;

long long check(){
	long long val = 0;
	
	for(int i = 0; i <= last; i++)
		val = (val * 2) + (str[i] - '0');
	
	//cerr<< str[0] << endl;
	//cerr << val << endl;
	
	long long s = 0, e = (1ll << 31);
	while(s + 1 != e){
		long long m = (s + e) / 2;
		if(m * m <= val)
			s = m;
		else	e = m;
	}
	
	
	if(s * s == val)
		return true;
	return false;
}

bool bt(int pos){
	if(str[pos] == 0){
		if(check())
			return true;
		return false;
	}
	if(str[pos] != '?')
		return bt(pos + 1);
	
	str[pos] = '0';
	if(bt(pos + 1))
		return true;
	str[pos] = '1';
	if(bt(pos + 1))
		return true;
	str[pos] = '?';
	return false;
}

int main(){
	int testN;
	cin >> testN;
	FOR(testI, testN){
		scanf(" %s", str);
		
		last = 0;
		while(str[last] != 0)
			last++;
		last--;
		
		if(!bt(0))
			cerr<< "bad\n" << endl;
		printf("Case #%d: %s\n", testI + 1, str);
	}
	return 0;
}

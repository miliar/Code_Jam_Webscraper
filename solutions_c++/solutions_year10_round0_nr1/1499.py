#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <string>
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

#define pb push_back
#define FOR(i,a,n) for(int i=a;i<n;i++)
#define REP(i,n) FOR(i,0,n)
#define DBGV(_v) { REP(_i, _v.size()) { cout << _v[_i] << "\t";} cout << endl;}
#define GI ({int _t; scanf("%d", &_t); _t;})
#define sz size()
#define DBG(x) cout << #x << ":" << x << endl;

using namespace std;

string toString(long long int n) {
	ostringstream ost;ost<<n;ost.flush();return ost.str();
}


string converttobase(long long int num, int base) {
	string res = "";
	while (num >= base) {
		res += toString(num%base);
		num /= base;
	}
 	res += toString(num);
 	reverse(res.begin(), res.end());
 	return res;
}

int main()
{
	int kases = GI;	
	FOR(kase, 1, kases+1) {
		long long int n, k;
		cin >> n >> k;
		k = k%(long long int)(pow(2, n));	
		string base2 = converttobase(k, 2);
		bool on = true;
		REP(i, base2.sz) if (base2[i] == '0') on = false;
		if (on && base2.sz == n) {
			printf("Case #%d: ON\n", kase);
		}
		else {
			printf("Case #%d: OFF\n", kase);
		}
	}	
}

#include <vector>
#include <map>
#include <set>
#include <queue>
#include <algorithm>
#include <utility>
#include <sstream>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <string>
 
using namespace std;
 
#define pb push_back
#define mp make_pair
#define vs vector<string>
#define vi vector<int>
#define pii pair<int,int>
#define vvi vector< vector<int> >
#define vpi vector< pair<int,int> >
#define LL long long

LL gcd(LL a, LL b) {
if (a == 0) return 1000;
if (a < b)
	return b%a ? gcd(a,b%a) : a;
return a%b ? gcd(a%b,b) : b;
}

int main() {
        int T; cin >> T;
        for(int iter=0;iter<T;iter++) {
  		LL N,PD,PG;
		cin >> N >> PD >> PG;
		bool f=  false;
		LL g = gcd(PD, 100);
		LL fac = 100/g;
		if (fac <= N) f = true;
		if (PG == 100 && PD != 100) f = false;
		if (PG == 0 && PD != 0) f = false;	
		if (f)
			cout<<"Case #"<<(iter+1)<<": Possible\n";
		else	
			cout<<"Case #"<<(iter+1)<<": Broken\n";	
	}
}

